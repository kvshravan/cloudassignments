#!/usr/bin/python
import os
os.system('sudo yum install -y python python-dev python-pip')
os.system('sudo pip install boto3')
import boto3
cmd = 'sudo yum install -y httpd'
cmd2 = ' sudo service httpd start'
os.system(cmd)
os.system(cmd2)
access_id_key = ""
secret_acces_key = ""
bucket_name = 'course-reg-bucket'
client = boto3.client('s3',aws_access_key_id = access_id_key,aws_secret_access_key = secret_acces_key)
client.download_file(bucket_name,'index.html','index.html')
os.system('sudo cp index.html /var/www/html/')
