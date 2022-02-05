from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    location = 'media'
    file_overwrite = True
    default_acl = "public-read"
    custom_domain = settings.AWS_S3_CUSTOM_DOMAIN



class StaticStorage(S3Boto3Storage):
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    location = 'static'
    file_overwrite = True
    default_acl = "public-read"
    custom_domain = settings.AWS_S3_CUSTOM_DOMAIN