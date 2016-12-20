class InputError(Exception):
    msg = "fff"

    def __init__(self, msg):
        self.msg = msg
