from django.shortcuts import render
from zhihuUser.models import ZhihuUser
from zhihuUser.serializers import ZhihuUserSerializer
from rest_framework import generics


class ZhihuUserList(generics.ListCreateAPIView):
    queryset = ZhihuUser.objects.all()
    serializer_class = zhihuUseSererializer


class ZhihuUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ZhihuUser.objects.all()
    serializer_class = zhihuUseSererializer
