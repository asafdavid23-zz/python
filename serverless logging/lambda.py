import boto3
import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# This Function will get the function name to bo logged.
def get_lambda_function(function_arn):
    """
    :param funciton_arn: Serverless Application ARN
    :return: resp['Configuration']['FunctionName']
    """
    lambda_client = boto3.client('lambda')
    resp = lambda_client.get_function(
        FunctionName=function_arn
    )
    return resp['Configuration']['FunctionName']

# This function will delete the CFN Stack in case of false tag.
def delete_cfn_stack(stack_name):
    """
    :param stack_name: CFN Stack Name
    """
    cfn_client = boto3.client('cloudformation')
    # Get CFN Stacks list
    stacks_list = cfn_client.list_stacks(
        StackStatusFilter=['UPDATE_COMPLETE', 'CREATE_COMPLETE', 'CREATE_FAILED', 'ROLLBACK_FAILED', 'ROLLBACK_COMPLETE', 'UPDATE_ROLLBACK_COMPLETE', 'DELETE_FAILED']
    )

    for stack in stacks_list['StackSummaries']:
        if stack['StackName'] == stack_name:
            logger.warning("Deleting CFN Stack " + stack_name + ", this lambda logs will not be shipped into 'Logz.io'")
            cfn_client.delete_stack(
                StackName=stack_name
            )

# This function will update the CFN Stack in case of existing.
def update_cfn_stack(stack_name, template_url, function_name, cfn_tags, secret_name, region):
    """
    :param stack_name:    CFN Stack Name
    :param template_url:  CFN Template S3 Url
    :param function_name: Serverless Application Name
    :param secret_name: AWS Secrets Name
    """
    cfn_client = boto3.client('cloudformation')

    # Get CFN Stacks List
    stacks_list = cfn_client.list_stacks(
        StackStatusFilter=['UPDATE_COMPLETE', 'CREATE_COMPLETE']
    )
    for stack in stacks_list['StackSummaries']:
        if stack['StackName'] == stack_name:
            logger.info('Updating CFN Stack ' + stack_name)
            cfn_client.update_stack(
                StackName=stack_name,
                UsePreviousTemplate=True,
                Capabilities=['CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM', 'CAPABILITY_AUTO_EXPAND'],
                Parameters = [
                    {
                        'ParameterKey' : 'functionName',
                        'UsePreviousValue' : True
                    },
                    {
                        'ParameterKey' : 'secretName',
                        'UsePreviousValue' : True
                    },
                    {
                        'ParameterKey' : 'region',
                        'UsePreviousValue' : True
                    }
                ],
                Tags=cfn_tags
            )

# This function will handle the CFN Stack creation, In case of stack is already exist, it will call the 'update_cfn_stack' function.
def create_cfn_stack(stack_name, template_url, function_name, cfn_tags, secret_name, region):
    """
    :param stack_name:    CFN Stack Name
    :param template_url:  CFN Template S3 Url
    :param function_name: Serverless Application Name
    :param secret_name: AWS Secrets Name
    """
    cfn_client = boto3.client('cloudformation')
    # Creating new CFN Stack.
    logger.info('Creating CFN Stack.')
    cfn_client.create_stack(
        StackName=stack_name,
        TemplateURL=template_url,
        Capabilities=['CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM', 'CAPABILITY_AUTO_EXPAND'],
        Parameters=[
            {
                'ParameterKey' : 'functionName',
                'ParameterValue' : function_name
            },
            {
                'ParameterKey' : 'secretName',
                'ParameterValue' : secret_name
            },
            {
                'ParameterKey' : 'region',
                'ParameterValue' : region
            },
        ],
        Tags=cfn_tags
    )

def lambda_handler(event, context):
    """
    :param event:   CloudWatch Event JSON Output
    :param context: Lambda Context
    """
    ### Events Handler ###
    new_tag_event = False
    if event['detail']['eventName'] == "TagResource20170331v2":
        new_tag_event = True

    new_lambda_event = False
    if event['detail']['eventName'] == "CreateFunction20150331":
        new_lambda_event = True

    detail = event['detail']
    logger.info('Event: ' + str(event))
    event_tags = detail['requestParameters']['tags']
    template_url = os.environ['CFN_TEMPLATE']
    secret_name = os.environ['SECRET_NAME']
    region = os.environ['REGION']
    function_arn = ""
    cfn_tags = []
    try:
        if new_tag_event:
            function_arn = detail['requestParameters']['resource']
            lambda_name = get_lambda_function(function_arn)
            stack_name = lambda_name + "-logzio-shipper"
        elif new_lambda_event:
            lambda_name = detail['responseElements']['functionName']
            stack_name = lambda_name + "-logzio-shipper"

        for k, v in event_tags.items():
            if k.startswith('aws:'):
                continue
                logger.info('Skipping AWS Tags Restrictions')                                                                       # Iterate over tags dict to find logging:true
            elif k == 'LogzIO' and v == 'True':
                logzio = True
            elif k == 'LogzIO' and v == 'False':
                logzio = False
            else:
                cfn_tags.append({ 'Key': k, 'Value': v })

        if logzio == True:
            logger.info("logzio tag is exist, this lambda logs will be shipped into 'Logz.IO'")
            logger.info('Deploying CFN Stack')
            create_cfn_stack(stack_name, template_url, lambda_name, cfn_tags, secret_name, region)                                 # Create the CFN Stack.
        elif logzio == False:
            delete_cfn_stack(stack_name)
        else:
            update_cfn_stack(stack_name, template_url, lambda_name, cfn_tags, secret_name, region)

        return True
    except Exception as e:
        logger.error('Something went wrong: ' + str(e))
        return False
