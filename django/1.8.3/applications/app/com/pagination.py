#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -----------------------------------------------------
#  FileName    :    urlprefix.py
#  Author      :    yangjun@
#  Project     :    hato/utils
#  Date        :    2015-06-11
#  Description :    
# -----------------------------------------------------
from app.com.exception import (
    PermissionException,
    ParamsException,
    IOException,
    SystemException
)

OPTIONAL_PAGE_NUMBER = [5, 10, 15 , 20, 50, 100]

def pagination_validate(data):
    if(not data.has_key('limit')):
        data['limit'] = OPTIONAL_PAGE_NUMBER[0]
    else:
        if(data['limit'] not in OPTIONAL_PAGE_NUMBER):
            raise ParamsException("param limit must be in " + str(OPTIONAL_PAGE_NUMBER))
    if(not data.has_key('offset')):
        data['offset'] = 0

