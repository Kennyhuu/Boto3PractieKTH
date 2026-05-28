import boto3


def create_webserver_security_group(vpc_id):
    ec2 = boto3.client("ec2")

    # Create a security group for the web server
    response = ec2.create_security_group(
        GroupName="WebServerSG",
        Description="Security group for web server",
        VpcId=vpc_id,
    )
    return response


def authorize_webserver_sg_ingress(security_group_id):
    ec2 = boto3.client("ec2")

    # Authorize inbound traffic to the web server security group
    response = ec2.authorize_security_group_ingress(
        GroupId=security_group_id,
        IpPermissions=[
            {
                "IpProtocol": "tcp",
                "FromPort": 80,
                "ToPort": 80,
                "IpRanges": [{"CidrIp": "0.0.0.0/0"}],
            },
            {
                "IpProtocol": "tcp",
                "FromPort": 22,
                "ToPort": 22,
                "IpRanges": [{"CidrIp": "0.0.0.0/0"}],
            },
        ],
    )
    return response
