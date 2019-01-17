import tarfile

import os.path
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']


def get_credentials():
    """
    Get oauth2 credentials
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server()

        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds


def upload_file(file_name, dest_folder=""):
    """
    Upload local file to Google Drive.

    :param file_name: file name
    :param dest_folder: desired drive folder
    """
    creds = get_credentials()
    service = build('drive', 'v3', credentials=creds)

    file_metadata = {"name": file_name}

    if dest_folder:
        folders = service.files().list(q="mimeType='application/vnd.google-apps.folder'").execute()
        destination_folder = [folder for folder in folders['files'] if folder['name'] == 'Backups'][0]

        file_metadata.update(parents=[destination_folder['id']])

    media = MediaFileUpload(file_name)

    file = service.files().create(body=file_metadata,
                                  media_body=media).execute()
    return file['id']


def make_tarfile(name, *source, extra=None):
    """
    Create *.tar archive.

    :param name: archive name
    :param source: data to compress
    :param extra: additional compression mode (gz of bz2)
    """

    tar_name = f"{name}.tar" if not extra else f"{name}.tar.{extra}"
    mode = f"w:{extra}" if extra else "w"

    with tarfile.open(tar_name, mode) as tar:
        for item in source:
            tar.add(item)

    return tar_name
