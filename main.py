import logging

from dulwich.porcelain import for_each_ref

import vpc
import igw
import pub_subnet
import priv_subnet
import priv_rtb
import pub_rtb
import webserver
import webserver_sg
import dynamoDB


def configure_logging(level=logging.INFO):
    """Configure and return a module-level logger."""
    logging.basicConfig(level=level, format="%(asctime)s %(levelname)s: %(message)s")
    return logging.getLogger(__name__)


logger = configure_logging()


def main():
    vpc_response = vpc.create_vpc()
    vpc_id = vpc_response["Vpc"]["VpcId"]
    logger.info(f"VPC created with ID: {vpc_id}")

    subnet_response = pub_subnet.create_subnet(vpc_id)
    subnet_id = subnet_response["Subnet"]["SubnetId"]
    logger.info(f"Public Subnet created with ID: {subnet_id}")

    igw_response = igw.create_igw()
    igw_id = igw_response["InternetGateway"]["InternetGatewayId"]
    logger.info(f"Internet Gateway created with ID: {igw_id}")

    igw_attach_response = igw.attach_igw_to_vpc(igw_id, vpc_id)
    logger.info(f"Internet Gateway attached to VPC: {igw_attach_response}")

    pub_rtb_response = pub_rtb.create_pub_rtb(vpc_id)
    pub_rtb_id = pub_rtb_response["RouteTable"]["RouteTableId"]
    logger.info(f"Public Route Table created with ID: {pub_rtb_id}")

    pub_rtb_assoc_response = pub_rtb.associate_pub_rtb(pub_rtb_id, subnet_id)
    logger.info(f"Public Route Table associated with Subnet: {pub_rtb_assoc_response}")
    pub_route_response = pub_rtb.create_pub_route(pub_rtb_id, igw_id)

    logger.info(f"Route created in Public Route Table: {pub_route_response}")
    priv_subnet_response = priv_subnet.create_subnet(vpc_id)
    priv_subnet_id = priv_subnet_response["Subnet"]["SubnetId"]

    logger.info(f"Private Subnet created with ID: {priv_subnet_id}")
    priv_rtb_response = priv_rtb.create_priv_rtb(vpc_id)
    priv_rtb_id = priv_rtb_response["RouteTable"]["RouteTableId"]
    logger.info(f"Private Route Table created with ID: {priv_rtb_id}")

    priv_rtb_assoc_response = priv_rtb.associate_priv_rtb_with_subnet(
        priv_rtb_id, priv_subnet_id
    )
    logger.info(
        f"Private Route Table associated with Subnet: {priv_rtb_assoc_response}"
    )

    webserver_sg_response = webserver_sg.create_webserver_security_group(vpc_id)
    webserver_sg_id = webserver_sg_response["GroupId"]
    logger.info(f"Web Server Security Group created with ID: {webserver_sg_id}")

    webserver_sg_ingress_response = webserver_sg.authorize_webserver_sg_ingress(
        webserver_sg_id
    )
    logger.info(
        f"Ingress rules added to Web Server Security Group: {webserver_sg_ingress_response}"
    )
    webserver_instance_response = webserver.create_ec2_instance(
        subnet_id, webserver_sg_id
    )
    webserver_instance_id = webserver_instance_response["Instances"][0]["InstanceId"]
    logger.info(f"Web Server EC2 instance created with ID: {webserver_instance_id}")


