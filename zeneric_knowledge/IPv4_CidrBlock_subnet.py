'''
Each resource has an IP address not the each request between resources. Request uses source resource and target resources IP address.

IPv4: Internet Protocol version 4 - addresses like 192.168.0.1


CIDR block: Defines the range of IP addresses available that we can use inside private AWS network VPC. 


It uses the format A.B.C.D/Prefix.

    Example: 10.0.0.0/16

    The /16 means the first 16 bits are fixed, leaving the rest for host addresses.



1. How Each IP Address in the Range is Used?
A. Every EC2 instance, Lambda function (when placed in a VPC), Neptune node, or other service inside my VPC gets an IP from this pool.

   These IPs allow our resources to talk to each other securely inside the VPC.


Example: If my VPC is 10.0.0.0/16, then EC2 instances might get 10.0.1.5, Neptune might get 10.0.2.10


Here in A.B.C.D/Prefix

    Prefix is number of bits that are fixed in the IP address.

    IPv4 address is 32 bits long (written as 4 numbers separated by dots, e.g., 10.0.0.1)


Q. What is meant by First 16 Bits means in case of 10.0.0.0/16?
A. /16 means the first 16 bits are fixed for the network.

    10.0 is fixed -> this defines the network

    The remaining 16 bits (0.0 to 255.255) are available for hosts.

In case of 10.0.0.0/24, First 24 bits (10.0.0) is fixed, only last 8 bits left which can be (0 to 255) so total 256 IPs will be available if we create VPC with this CIDR block.

--------------------------------------------------------------------------------------------------------------------------------------------------------


Subnet: A subnet is a smaller slice of your VPC's IP range.

Example: If my VPC is 10.0.0.0/16, we can carve out 10.0.1.0/24 as one subnet.

* Subnets are tied to Availabilty Zones (AZs). We usually create at least two subnets in different AZs for redundancy.


Q. Why Subnets are needed, even though VPC itself is private ?
A. A VPC(10.0.0.0/16) is a big pool of addresses - 65,536 in total.

    If we dump everything into one gaint pool, we lose:
        Organization clarity: we can't separate workloads (databases vs web servers)



--------------------------------------------------------------------------------------------------------------------------------------------------------


Availability Zone (Az)

Region: A geographic area (e.g., Mumbai = ap-south-1)

Availability Zones (AZs): Each Region has multiple AZs, like ap-south-1a, ap-south-1b, ap-south-1c.



When we create a VPC, it spans the entire region. It's not tied to one AZ - it covers all AZs in that region.

A subnet is created inside a VPC, but it must be placed in one specific AZ.

Example: Subnet A (10.0.1.0/24) in ap-south-1a, Subnet B (10.0.2.0/24) in ap-south-1b

--------------------------------------------------------------------------------------------------------


Public and Private Subnets:


All subnets (public or private) are always inside a VPC. There is no such thing as a subnet outside a VPC.


The difference between public and private subnets is not location, but internet accessibility (who can access the resources inside subnet)



Public Subnet

* A public subnet is a subnet inside VPC that has a route to the Internet Gateway (IGW)














'''