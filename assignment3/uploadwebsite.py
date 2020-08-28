from secrets import access_id_key,secret_acces_key
import boto3
import os
def uploadfiles():
    client = boto3.client('s3',aws_access_key_id = access_id_key,aws_secret_access_key = secret_acces_key)
    bucket_name = 'myportfolio-assignment'
    for root,dirs,files in os.walk('./smalldoc',topdown=True):
        for filename in files:
            local_path = os.path.join(root,filename)
            relative_path = os.path.relpath(local_path,os.getcwd()).replace("\\","/")
            print(local_path+'\t'+relative_path)
            client.upload_file(local_path,bucket_name,relative_path)
def downloadfiles():
    resource = boto3.resource('s3',aws_access_key_id = access_id_key,aws_secret_access_key = secret_acces_key)
    my_bucket = resource.Bucket('myportfolio-assignment')
    for s3_object in my_bucket.objects.all():
        filename = s3_object.key
        print(filename)
        my_bucket.download_file(filename,filename+'down')
def main():
    #uploadfiles()
    downloadfiles()
if __name__ == '__main__':
    main()
