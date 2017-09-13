# -*- coding: utf-8 -*-from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.

import datetime
import time


f = open('/home/ubuntu/PycharmProjects/untitled/untitled/memory', 'w')
f.write(datetime.datetime.now().strftime(('%H:%M:%S')))
f.close()