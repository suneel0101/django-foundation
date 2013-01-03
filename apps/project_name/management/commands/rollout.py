from django.core.management.base import BaseCommand
from optparse import make_option
import subprocess


def run(*args, **kwargs):
    subprocess.call(*args, shell=True, **kwargs)


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--no-s3',
                    action='store_true', dest='no_s3', default=False,
                    help="Will not sync to S3"),
    )

    help = 'Bootstrap rollout script that pushes to Heroku and syncs to S3 unless you pass --no-s3'

    def handle(self, *args, **options):
        run("git push heroku master")
        if not options.get('no_s3'):
            run("heroku run python manage.py sync_media_s3")
