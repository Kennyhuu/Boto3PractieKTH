import boto3


def create_ec2_instance(subnet_id, security_group_id):
    ec2 = boto3.client("ec2")

    # Create an EC2 instance
    response = ec2.run_instances(
        ImageId="ami-029a761f237195c2c",  # Replace with a valid AMI ID
        InstanceType="t3.micro",
        MinCount=1,
        MaxCount=1,
        KeyName="vockey",  # Replace with your key pair name
        SecurityGroupIds=[security_group_id],  # Replace with your security group ID
        SubnetId=subnet_id,  # Replace with your subnet ID
    )
    return response
