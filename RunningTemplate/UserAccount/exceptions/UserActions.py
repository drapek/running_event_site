# -*- coding: utf-8 -*-
class InvalidPassword(Exception):
    msg = "Hasło jest niepoprawne"

    def __init__(self, msg):
        self.msg = msg
