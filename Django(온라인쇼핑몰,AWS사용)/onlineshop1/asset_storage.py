from storages.backends.s3boto3 import *
class MediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False