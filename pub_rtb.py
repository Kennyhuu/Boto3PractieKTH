import boto3


def create_pub_rtb(vpc_id):
    ec2 = boto3.client("ec2")

    # Create a public route table
    response = ec2.create_route_table(VpcId=vpc_id)
    return response


def associate_pub_rtb(rtb_id, subnet_id):
    ec2 = boto3.client("ec2")

    # Associate the public route table with the public subnet
    response = ec2.associate_route_table(RouteTableId=rtb_id, SubnetId=subnet_id)
    return response


def create_pub_route(rtb_id, igw_id):
    ec2 = boto3.client("ec2")

    # Create a route in the public route table to allow internet access
    response = ec2.create_route(
        RouteTableId=rtb_id, DestinationCidrBlock="0.0.0.0/0", GatewayId=igw_id
    )
    return response
