#!/usr/bin/python3.6
import boto3

class AWSClient(object):
    "Basic object for AWS services discovery"
    def __init__(self, config, account, service, region):
        "Initializes Boto3 client for specified service"

        self.client = boto3.client(service, region_name=region)
        # used for s3
        self.region = region
