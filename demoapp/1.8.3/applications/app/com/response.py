#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -----------------------------------------------------
#  FileName    :    response.py
#  Author      :    baojie@
#  Project     :    hato/utils
#  Date        :    2015-06-11
#  Description :    errorcode for hato
# -----------------------------------------------------

from rest_framework.response import Response
from rest_framework import status

class ResponseEntry(object):
    def __init__(self, code, msg, data=None, errs=None):
        self.code = code
        self.msg = msg
        self.data = data
        self.errs = errs

def success(data):
    return Response(ResponseEntry(0, "operation success", data=data).__dict__, status=status.HTTP_200_OK)

def permission_exception(errs, status):
    return Response(ResponseEntry(1001, "permission denied", errs=errs).__dict__, status=status)

def params_exception(errs, status):
    return Response(ResponseEntry(1002, "params exception", errs=errs).__dict__, status=status)

def io_exception(errs, status):
    return Response(ResponseEntry(1003, "io exception", errs=errs).__dict__, status=status)

def system_exception(errs, status):
    return Response(ResponseEntry(1004, "system exception", errs=errs).__dict__, status=status)
