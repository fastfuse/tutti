import tarfile

from jsonrpcserver import method


@method
def ping():
    return "pong"


@method
def add(a, b):
    return a + b


@method
def backup():
    """
    Method to make backups of specified dirs
    """
    pass


def make_tarfile(tar_name, *source, extra=None):
    """
    Create *.tar archive.

    :param tar_name: archive name
    :param source: data to compress
    :param extra: additional compression mode (gz of bz2)
    """

    mode = f"w:{extra}" if extra else "w"

    with tarfile.open(tar_name, mode) as tar:
        for item in source:
            tar.add(item)
