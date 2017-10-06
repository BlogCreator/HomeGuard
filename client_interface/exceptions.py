# -*- coding: utf-8 -*-
class RequestMethodError(RuntimeError):
    def __init__(self, arg):
        self.args = arg

class JsonError(RuntimeError):
    def __init__(self, arg):
        self.args = arg