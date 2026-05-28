import boto3


def create_subnet(vpc_id):
    ec2 = boto3.client("ec2")

    # Create a subnet in the specified VPC
    response = ec2.create_subnet(
        VpcId=vpc_id,
        CidrBlock="10.0.0.64/26",  # Replace with your desired CIDR block for the private subnet
    )
    return response
