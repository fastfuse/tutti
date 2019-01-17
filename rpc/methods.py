from jsonrpcserver import method


@method
def ping():
    return "pong"


@method
def add(a, b):
    return a + b
