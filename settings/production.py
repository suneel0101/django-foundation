import os
import dj_database_url

DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}

DEBUG = False

# AWS Configuration
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')

AWS_BUCKET_NAME = os.environ.get('AWS_BUCKET_NAME')

AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')


MEDIA_URL = '//s3.amazonaws.com/{}/'.format(AWS_BUCKET_NAME)

# Static asset configuration
PROJECT_PATH = os.path.dirname(os.path.dirname(__file__))
STATIC_ROOT = 'static'
STATIC_URL = '/static/'
