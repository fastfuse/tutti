import tarfile

from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']

class FolderSearchFailure(Exception):
    pass


def get_credentialsntials():
    """
    Get oauth2 credentials
    """
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    store = file.Storage('token.json')
    creds = store.get()

    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)

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
        try:
            folders = service.files().list(q="mimeType='application/vnd.google-apps.folder'").execute()
            destination_folder = [folder for folder in folders['files'] if folder['name'] == dest_folder][0]

            file_metadata.update(parents=[destination_folder['id']])

        except IndexError:
            raise FolderSearchFailure(f"Failed to get folder '{dest_folder}'")

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
            tar.add(item, arcname='aaa')

    return tar_name
