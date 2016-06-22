#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -----------------------------------------------------
#  FileName    :    response.py
#  Author      :    baojie@
#  Project     :    hato/utils
#  Date        :    2015-06-11
#  Description :    errorcode for hato
# -----------------------------------------------------

from rest_framework import status
from rest_framework.response import Response

class ResponseEntry(object):
    def __init__(self, code, msg, data=None, errs=None):
        self.code = code
        self.msg = msg
        self.data = data
        self.errs = errs

def success(data):
    return Response(ResponseEntry(0, "operation success", data=data).__dict__)

def permission_exception(errs):
    return Response(ResponseEntry(1001, "permission denied", errs=errs).__dict__, status=status.HTTP_403_FORBIDDEN)

def params_exception(errs):
    return Response(ResponseEntry(1002, "params exception", errs=errs).__dict__)

def io_exception(errs):
    return Response(ResponseEntry(1003, "io exception", errs=errs).__dict__)

def system_exception(errs):
    return Response(ResponseEntry(1004, "system exception", errs=errs).__dict__)


