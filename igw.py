import boto3


def create_igw():
    ec2 = boto3.client("ec2")

    # Create an Internet Gateway
    response = ec2.create_internet_gateway()
    return response


def attach_igw_to_vpc(igw_id, vpc_id):
    ec2 = boto3.client("ec2")

    # Attach the Internet Gateway to the VPC
    response = ec2.attach_internet_gateway(InternetGatewayId=igw_id, VpcId=vpc_id)
    return response
