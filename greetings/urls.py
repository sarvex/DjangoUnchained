# coding=utf-8
from greetings.views import hello

__author__ = 'Sarvex Jatasra'

from django.conf.urls import url

urlpatterns = [
    url(r'^$', hello),
]
