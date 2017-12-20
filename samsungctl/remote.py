from . import exceptions
from .remote_legacy import RemoteLegacy
from .remote_websocket import RemoteWebsocket
from .remote_pin import RemotePin

class Remote:
    def __init__(self, config):
        if config["method"] == "legacy":
            self.remote = RemoteLegacy(config)
        elif config["method"] == "websocket":
            self.remote = RemoteWebsocket(config)
        elif config["method"] == "pin":
            self.remote = RemotePin(config)
        else:
            raise exceptions.UnknownMethod()

    def __enter__(self):
        return self.remote.__enter__()

    def __exit__(self, type, value, traceback):
        self.remote.__exit__(type, value, traceback)

    def close(self):
        return self.remote.close()

    def control(self, key):
        return self.remote.control(key)
