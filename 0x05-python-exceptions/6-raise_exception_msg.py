#!/usr/bin/python3
def raise_exception_msg(message=""):
    if not message:
        message = "A NameError exception has been raised"
    raise NameError(message)
