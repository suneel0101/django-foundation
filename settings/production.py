import dj_database_url
DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}
DEBUG = False
# Set the following variables if you want to serve static assets from S3.
# This is recommended.
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_BUCKET_NAME = ''
MEDIA_URL = 'http://s3.amazonaws.com/{}/'.format(AWS_BUCKET_NAME)
