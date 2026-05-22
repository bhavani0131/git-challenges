import boto3

# Initialize the EC2 client
ec2 = boto3.client('ec2', region_name='us-west-2')

# Launch a single t2.micro instance
response = ec2.run_instances(
    ImageId='ami-0c7217cdde317cfec',  # Must match your region
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1
)

print(f"Launched instance: {response['Instances'][0]['InstanceId']}")
