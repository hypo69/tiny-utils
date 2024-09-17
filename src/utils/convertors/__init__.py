## \file ../src/utils/convertor/__init__.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
""" Конвертор форматов
"""
...
from packaging.version import Version
from .version import __version__, __doc__, __details__  

from .base64_to_tmpfile import base64_to_tmpfile
from .csv2json_csv2dict import csv2dict
from .dict2xml import dict2xml
from .html2esc import html2escape
from .json2csv_dict2csv import dict2csv, json2csv 

from .xml2dict import xml2dict
from .dict2ns_ns2dict import dict2namespace, namespace2dict
from .text2png import TextToImageGenerator


