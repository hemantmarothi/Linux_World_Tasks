import boto3

def create_ec2_instance():
    ec2_client = boto3.client("ec2", region_name="ap-south-1")  # Change the region as needed

    print("\nCreating a new EC2 instance...")

    instance_type = input("Enter instance type (e.g., t2.micro): ")
    ami_id = input("Enter AMI ID (e.g., ami-0c55b159cbfafe1f0): ")
    response = ec2_client.run_instances(
        ImageId=ami_id,
        InstanceType=instance_type,
        MinCount=1,
        MaxCount=1,
    )
    print(f"EC2 instance created successfully!")

def create_s3_bucket():
    s3_client = boto3.client("s3")

    print("\nCreating a new S3 bucket...")

    bucket_name = input("Enter the bucket name: ")

    response = s3_client.create_bucket(
        Bucket=bucket_name
    )

    print(f"S3 bucket '{bucket_name}' created successfully!")

def list_ec2_instances():
    ec2_client = boto3.client("ec2", region_name="ap-south-1")  # Change the region as needed

    print("\nListing EC2 instances...")

    response = ec2_client.describe_instances()

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            instance_type = instance["InstanceType"]
            state = instance["State"]["Name"]

            print(f"Instance ID: {instance_id}, Instance Type: {instance_type}, State: {state}")

def list_s3_buckets():
    s3_client = boto3.client("s3")

    print("\nListing S3 buckets...")

    response = s3_client.list_buckets()

    for bucket in response["Buckets"]:
        print(bucket["Name"])

def create_sns_topic():
    sns_client = boto3.client("sns")

    print("\nCreating a new SNS topic...")

    topic_name = input("Enter the SNS topic name: ")

    response = sns_client.create_topic(
        Name=topic_name
    )

    topic_arn = response["TopicArn"]
    print(f"SNS topic '{topic_name}' created with ARN: {topic_arn}")

def list_sns_topics():
    sns_client = boto3.client("sns")

    print("\nListing SNS topics...")

    response = sns_client.list_topics()

    for topic in response["Topics"]:
        print(topic["TopicArn"])

def create_iam_user():
    iam_client = boto3.client("iam")

    print("\nCreating a new IAM user...")

    user_name = input("Enter the IAM user name: ")

    response = iam_client.create_user(
        UserName=user_name
    )

    print(f"IAM user '{user_name}' created successfully!")

def create_lambda_function():
    lambda_client = boto3.client("lambda")

    print("\nCreating a new Lambda function...")

    function_name = input("Enter the Lambda function name: ")
    role_arn = input("Enter the IAM role ARN for the Lambda function: ")
    handler = input("Enter the Lambda function handler (e.g., lambda_function.handler): ")
    runtime = input("Enter the runtime (e.g., python3.8): ")
    code_path = input("Enter the local path to the Lambda deployment package (.zip): ")

    with open(code_path, "rb") as file:
        code_content = file.read()

    response = lambda_client.create_function(
        FunctionName=function_name,
        Runtime=runtime,
        Role=role_arn,
        Handler=handler,
        Code={"ZipFile": code_content}
    )

    function_arn = response["FunctionArn"]
    print(f"Lambda function '{function_name}' created with ARN: {function_arn}")

def list_lambda_functions():
    lambda_client = boto3.client("lambda")

    print("\nListing Lambda functions...")

    response = lambda_client.list_functions()

    for function in response["Functions"]:
        print(function["FunctionName"])

def main():
    while True:
        print("\nAWS Services Menu")
        print("1. Create EC2 Instance")
        print("2. Create S3 Bucket")
        print("3. List EC2 Instances")
        print("4. List S3 Buckets")
        print("5. Create SNS Topic")
        print("6. List SNS Topics")
        print("7. Create IAM User")
        print("8. Create Lambda Function")
        print("9. List Lambda Functions")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_ec2_instance()
        elif choice == "2":
            create_s3_bucket()
        elif choice == "3":
            list_ec2_instances()
        elif choice == "4":
            list_s3_buckets()
        elif choice == "5":
            create_sns_topic()
        elif choice == "6":
            list_sns_topics()
        elif choice == "7":
            create_iam_user()
        elif choice == "8":
            create_lambda_function()
        elif choice == "9":
            list_lambda_functions()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()