#!/usr/bin/env python
# pylint: disable=W0212
import json
import logging
import os
import ssl

import pika
from pydantic import BaseModel


from collections import OrderedDict
from agate.dto.profileResponse import *


def append_to_response_obj(self, statisticsType, responseObj, **kwargs):
    logging.basicConfig(level = logging.INFO, format = '%(levelname)s:%(asctime)s:%(message)s')
    print("Hello World")
    return "Hi"


