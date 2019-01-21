import datetime
import os

from utils import upload_file, make_tarfile

if __name__ == '__main__':
    KODI_DIR = os.path.expanduser('~/.kodi')

    tar_name = f"backup-{datetime.datetime.now().replace(microsecond=0).isoformat()}"
    tar_file = make_tarfile(tar_name, KODI_DIR, extra='gz')

    upload_file(tar_file, 'Backups')
