#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -----------------------------------------------------
#  FileName    :    response.py
#  Author      :    baojie@
#  Project     :    hato/utils
#  Date        :    2015-06-11
#  Description :    errorcode for hato
# -----------------------------------------------------
import logging

from rest_framework import status
from rest_framework.views import exception_handler
from rest_framework import exceptions
from rest_framework.exceptions import APIException
import response
from exception import (
    PermissionException,
    ParamsException,
    IOException,
    SystemException
)

logger = logging.getLogger(__name__)

def common_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    # resp = exception_handler(exc, context)
    #logger.info(resp)
    #logger.info(exc)
    #logger.info(context)
    # Now add the HTTP status code to the response.
    #if resp is not None:
        #resp.data['status_code'] = resp.status_code
        #resp.data['test'] = 'test'
    if isinstance(exc, PermissionException):
        logger.error(exc, exc_info=1)
        return response.permission_exception(str(exc), status=status.HTTP_403_FORBIDDEN)
    elif isinstance(exc, ParamsException):
        logger.error(exc, exc_info=1)
        return response.params_exception(str(exc), status=status.HTTP_400_BAD_REQUEST)
    elif isinstance(exc, IOException):
        logger.error(exc, exc_info=1)
        return response.io_exception(str(exc), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif isinstance(exc, SystemException):
        logger.error(exc, exc_info=1)
        return response.system_exception(str(exc), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    elif isinstance(exc, exceptions.APIException):
        logger.error(exc, exc_info=1)
        return response.system_exception(str(exc), status=exc.status_code)
    else:
        logger.error(exc, exc_info=1)
        return response.system_exception(str(exc), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

