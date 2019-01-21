import datetime

from utils import upload_file, make_tarfile

if __name__ == '__main__':

    tar_name = f"backup-{datetime.datetime.now().replace(microsecond=0).isoformat()}"
    tar_file = make_tarfile(tar_name, 'README.md', 'requirements.txt', extra='gz')

    upload_file(tar_file, 'Backups')
