import datetime
import os

from rpc.utils import upload_file, make_tarfile

if __name__ == '__main__':

    print(os.path.abspath(__file__))

    # tar_name = f"backup-{datetime.datetime.now().replace(microsecond=0).isoformat()}"

    # tar_file = make_tarfile(tar_name, 'Dockerfile', 'README.md', 'app.py', 'requirements.txt', extra='gz')

    # upload_file(tar_file, 'Backups')
