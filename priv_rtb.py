import boto3


def create_priv_rtb(vpc_id):
    ec2 = boto3.client("ec2")

    # Create a route table in the specified VPC
    response = ec2.create_route_table(VpcId=vpc_id)
    return response


def associate_priv_rtb_with_subnet(route_table_id, subnet_id):
    ec2 = boto3.client("ec2")

    # Associate the route table with the private subnet
    response = ec2.associate_route_table(
        RouteTableId=route_table_id, SubnetId=subnet_id
    )
    return response
