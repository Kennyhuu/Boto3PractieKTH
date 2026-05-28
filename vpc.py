import boto3

def create_vpc():
    ec2 = boto3.client('ec2')
    
    # Create a VPC
    response = ec2.create_vpc(CidrBlock='10.0.0.0/24')
    return response

