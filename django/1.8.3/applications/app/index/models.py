#!/usr/bin/env python
#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:         models.py
# Purpose:
#
# Author:       yangjun
#
# Created:      30/03/2016
# Copyright:    (c) yangjun 2016
# Licence:      <your licence>
#-------------------------------------------------------------------------------

from django.db import models
from django.forms.models import model_to_dict

from app.com.exception import (
    PermissionException,
    ParamsException,
    IOException,
    SystemException
)

# Create your models here.
class BlogType(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, unique=True, db_index=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    description = models.TextField(null=False, blank=True)
    user = models.ForeignKey('auth.User', related_name='blog_types')

    class Meta:
        db_table = 'blog_type'

    def __unicode__(self):
        return u'id: <%d>' % self.pk

    @staticmethod
    def create(**kwargs):
        """
        exception: IOException
        """
        try:
            blog_type = BlogType.objects.create(**kwargs)
            return blog_type
        except Exception as e:
            raise IOException(str(e))

    @staticmethod
    def delete(**kwargs):
        """
        exception: IOException
        """
        try:
            blog_type = BlogType.objects.filter(**kwargs)
            matched_count = blog_type.delete()
            if(matched_count == 0):
                raise ParamsException("no matched record")
            return matched_count
        except ParamsException as e:
            raise ParamsException(str(e))
        except Exception as e:
            raise IOException(str(e))

    @staticmethod
    def update(id, **kwargs):
        """
        exception: ParamsException, IOException
        """
        try:
            matched_count = BlogType.objects.filter(id=id).update(**kwargs)
            if(matched_count == 0):
                raise ParamsException("no matched record")
            return matched_count
        except ParamsException as e:
            raise ParamsException(str(e))
        except Exception as e:
            raise IOException(str(e))

    @staticmethod
    # 主键要求必须是id
    def list(condition, offset=0, limit=5, sort=None, order=None):
        """
        exception: IOException
        """
        if(sort is None):
            sort = "id"
        if(order != None and order.lower() == "asc"):
            order_by = sort
        else:
            order_by = "-" + sort
        try:
            # blog_types = BlogType.objects.select_related("user__username").filter(**condition).order_by(order_by)[offset:(offset + limit)]
            # blog_type_list = blog_types.values()
            # return blog_type_list
            blog_types = BlogType.objects.filter(**condition).order_by(order_by)[offset:(offset + limit)]
            total = BlogType.objects.filter(**condition).count()
            return blog_types, total
        except Exception as e:
            raise IOException(str(e))

    @staticmethod
    def view(id):
        """
        exception: ParamsException, IOException
        """
        try:
            # blog_type = BlogType.objects.select_related("user__username").get(id=id)
            # blog_type_dict = model_to_dict(blog_type)
            # return blog_type_dict
            blog_type = BlogType.objects.get(id=id)
            return blog_type
        except BlogType.DoesNotExist as e:
            #blog_type_dict = {}
            raise ParamsException(str(e))
        except Exception as e:
            raise IOException(str(e))


