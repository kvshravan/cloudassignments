from secrets import access_id_key,secret_acces_key
import boto3
import os
import part1
def uploadfiles():
    client = boto3.client('s3',aws_access_key_id = access_id_key,aws_secret_access_key = secret_acces_key)
    bucket_name = 'course-reg-bucket'
    for file in os.listdir():
        if '.txt' in file:
            client.upload_file(file,bucket_name,file)
def downloadfiles():
    resource = boto3.resource('s3',aws_access_key_id = access_id_key,aws_secret_access_key = secret_acces_key)
    my_bucket = resource.Bucket('course-reg-bucket')
    for s3_object in my_bucket.objects.all():
        filename = s3_object.key
        my_bucket.download_file(filename,filename[:-4]+"_downloaded.txt")
        return filename[:-4]+"_downloaded.txt"
def main():
    #uploadfiles()
    filename = downloadfiles()
    part1.course_reg(filename)

if __name__ == '__main__':
    main()
