﻿""" Установка корня проекта """
## \file ../src/utils/interface/header.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
import sys,os
from pathlib import Path
__root__ : Path = os.getcwd() [:os.getcwd().rfind(r'hypotez')+7]
sys.path.append (__root__)     
 