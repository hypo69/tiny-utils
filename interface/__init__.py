"""!   input/output interfaces, such as `file`, `ftp`, `smtp`  
  Модуль ввода/вывода
@details Интерфейсы подключения к внешним службам `file`, `ftp`, `smtp` итп

 
@section libs imports:
- .jjson (local)
- .jjson (local)
- .jjson (local)
- .file (local)
- .ftp (local)
- .smtp (local)
  

"""
## \file ../src/utils/interface/__init__.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

from packaging.version import Version
from .version import __version__, __name__, __doc__, __details__, __annotations__,  __author__  

from .ftp import send, receive
from .smtp import send

