from secrets import access_id_key,secret_acces_key,password
import boto3
rdsClient = boto3.client('rds',aws_access_key_id=access_id_key,aws_secret_access_key=secret_acces_key,region_name='us-east-2')
response = rdsClient.create_db_instance(
    AllocatedStorage=5,
    DBInstanceClass='db.t2.micro',
    DBInstanceIdentifier='mymysqlinstance',
    Engine='MySQL',
    MasterUserPassword=password,
    VpcSecurityGroupIds=['sg-0117784967fd8a89b'],
    MasterUsername='Shravan',
)
ec2 = boto3.resource('ec2',aws_access_key_id=access_id_key,aws_secret_access_key=secret_acces_key,region_name='us-east-2')
instances = ec2.create_instances(
ImageId = 'ami-07c8bc5c1ce9598c3',
MinCount = 1,
MaxCount = 1,
InstanceType='t2.micro',
KeyName='my-keypair',
SecurityGroupIds=['sg-0117784967fd8a89b'],
UserData=open('startup_script.sh').read()
)
print(instances)
instance = instances[0]
instance.wait_until_running()
instance.load()
print(instance.public_dns_name)
