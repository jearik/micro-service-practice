#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -----------------------------------------------------
#  FileName    :    exception.py
#  Author      :    yangjun
#  Project     :
#  Date        :    2015-06-11
#  Description :
# -----------------------------------------------------
import httplib
import json

def getToken(username, password, tenantName, identity_host, identity_port):
    try:
        conn = httplib.HTTPConnection(identity_host+":"+identity_port)
        headers = {"Content-type":"application/json"}
        params = ({
            "auth": {
                "tenantName": tenantName,
                "passwordCredentials": {
                    "username": username,
                    "password": password
                }
            }
        })
        conn.request("POST", "/v2.0/tokens", body=json.JSONEncoder().encode(params), headers=headers)
        response = conn.getresponse()
        data = response.read()
        data = json.loads(data,encoding='UTF-8')
        #print data
        #token = data['access']['token']['id']
        #print token
        return data
    except Exception as e:
        logging.error(e, exc_info=1)
        raise Exception(e)
    finally:
        conn.close()

def newInstance(token, compute_host, compute_port, availability_zone, name, flavorRef, imageRef, key_name, security_groups):
    try:
        tenant_id = token['access']['token']['tenant']['id']
        conn = httplib.HTTPConnection(compute_host+":"+compute_port)
        headers = {"Content-type":"application/json","X-Auth-Token":token}
        params = ({
            "server": {
                "availability_zone": availability_zone,
                "name": name,
                "flavorRef": flavorRef,
                "imageRef": imageRef,
                "key_name": key_name,
                "security_groups": [
                    {
                        "name": "default"
                    },
                    {
                        "name": security_groups
                    }
                ]
            }
        })
        conn.request("POST", "/v2/"+tenant_id+"/servers", body=json.JSONEncoder().encode(params), headers=headers)
        #conn.request("GET", "/v2/"+tenant_id+"/flavors", body=None, headers=headers)
        response = conn.getresponse()
        data = response.read()
        data = json.loads(data,encoding='UTF-8')
        return data
    except Exception as e:
        logging.error(e, exc_info=1)
        raise Exception(e)
    finally:
        conn.close()

