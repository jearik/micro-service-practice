#!/usr/bin/env python
#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:         serializers.py
# Purpose:
#
# Author:       yangjun
#
# Created:      30/03/2016
# Copyright:    (c) yangjun 2016
# Licence:      <your licence>
#-------------------------------------------------------------------------------

from django.contrib.auth.models import User, Group

from rest_framework import serializers
from .validators import utctimestamp_v

from app import models

class BlogTypeSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset=User.objects.all(), many=False, slug_field='username', allow_null=True)

    class Meta:
        model = models.BlogType
        fields = ('id', 'name', 'create_time', 'update_time', 'description','user')

class BlogTypeQuerySerializer(serializers.Serializer):
    start_time = serializers.IntegerField(validators=[utctimestamp_v], required=False)
    end_time = serializers.IntegerField(validators=[utctimestamp_v], required=False)
    offset = serializers.IntegerField(default=0, min_value=0, required=False)
    limit = serializers.IntegerField(default=10, min_value=0, max_value=100, required=False)
    sort = serializers.CharField(max_length=128, required=False)
    order = serializers.CharField(max_length=128, required=False)

    def validate(self, data):
        if 'start_time' in data and 'end_time' in data:
            if data['start_time'] > data['end_time']:
                raise serializers.ValidationError('end_time must occur after start_time')
        return data

class BlogTypeCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128, required=True, allow_blank=False)
    description = serializers.CharField(required=False)

class BlogTypeUpdateSerializer(serializers.Serializer):
    description = serializers.CharField(required=False)


'''class UserSerializer(serializers.ModelSerializer):
    blog_types = serializers.PrimaryKeyRelatedField(queryset=models.BlogType.objects.all(), many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'blog_types')'''

