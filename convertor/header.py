"""! Установка корня проекта """
## \file ../src/utils/convertor/header.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
import sys,os
from pathlib import Path
__root__ : Path = os.getcwd() [:os.getcwd().rfind(r'hypotez')+7]
sys.path.append (__root__)     
 