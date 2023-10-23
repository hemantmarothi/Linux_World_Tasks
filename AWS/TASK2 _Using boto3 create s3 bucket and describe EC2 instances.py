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

def main():
    while True:
        print("\nAWS Services Menu")
        print("1. Create EC2 Instance")
        print("2. Create S3 Bucket")
        print("3. List EC2 Instances")
        print("4. List S3 Buckets")
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
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()