import boto3


def create_stack():
    cloudformation = boto3.client('cloudformation', region_name='us-west-2')

    with open('/home/minds-medical/PycharmProjects/Boto3PractieKTH'
              '/CloudFormation-template.yaml') as file:
        template = file.read()
    response=cloudformation.create_stack(
        StackName='Boto3ChallengeStack',
        TemplateBody=template,
        Capabilities=['CAPABILITY_NAMED_IAM']
    )
    print(response)
    print(response['StackId'])


def wait_for_stack():
    cloudformation = boto3.client('cloudformation')

    waiter = cloudformation.get_waiter('stack_create_complete')
    print("Waiting for stack creation")
    print(waiter.wait(StackName='Boto3ChallengeStack'))
    print("Stack creation complete")


def delete_stack():
    cloudformation = boto3.client('cloudformation')

    cloudformation.delete_stack(StackName='Boto3ChallengeStack')


if __name__ == '__main__':
    create_stack()