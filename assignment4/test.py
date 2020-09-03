import boto3
from secrets import access_id_key,secret_acces_key
auto_s = boto3.client('autoscaling',aws_access_key_id=access_id_key,aws_secret_access_key=secret_acces_key,region_name='us-east-2')
lc=auto_s.create_launch_configuration(
LaunchConfigurationName='my-launch-config',
InstanceType='t2.micro',
KeyName='my-keypair',
ImageId = 'ami-07c8bc5c1ce9598c3',
SecurityGroups=['sg-0117784967fd8a89b'],
UserData=open('startup_script.sh').read()
)
auto_s.create_auto_scaling_group(
AutoScalingGroupName='my-auto-scaling-group',
LaunchConfigurationName='my-launch-config',
AvailabilityZones=['us-east-2c'],
MaxSize=3,
MinSize=1
)
scale_up_policy=auto_s.put_scaling_policy(
AdjustmentType='ChangeInCapacity',
AutoScalingGroupName='my-auto-scaling-group',
PolicyName='scale_up',
ScalingAdjustment=1
)
scale_down_policy=auto_s.put_scaling_policy(
AdjustmentType='ChangeInCapacity',
AutoScalingGroupName='my-auto-scaling-group',
PolicyName='scale_down',
ScalingAdjustment=-1
)
cloud_w = boto3.client('cloudwatch',aws_access_key_id=access_id_key,aws_secret_access_key=secret_acces_key,region_name='us-east-2')
cloud_w.put_metric_alarm(
AlarmName='up_alarm',
Namespace='AWS/EC2',
MetricName='CPUUtilization',
Statistic='Average',
ComparisonOperator='GreaterThanThreshold',
Threshold=70,
Period=60,
EvaluationPeriods=2,
AlarmActions=[scale_up_policy['PolicyARN']]
)
cloud_w.put_metric_alarm(
AlarmName='down_alarm',
Namespace='AWS/EC2',
MetricName='CPUUtilization',
Statistic='Average',
ComparisonOperator='LessThanThreshold',
Threshold=40,
Period=60,
EvaluationPeriods=2,
AlarmActions=[scale_down_policy['PolicyARN']]
)
import time
time.sleep(30)
response = auto_s.describe_auto_scaling_groups(
AutoScalingGroupNames=['my-auto-scaling-group'],
)
list_auto = response['AutoScalingGroups']
req_instance_id = (((list_auto[0])['Instances'])[0])['InstanceId']
print(req_instance_id)
ec2 = boto3.resource('ec2',aws_access_key_id=access_id_key,aws_secret_access_key=secret_acces_key,region_name='us-east-2')
instance = ec2.Instance(id=req_instance_id)
instance.wait_until_running()
instance.load()
print(instance.public_dns_name)
