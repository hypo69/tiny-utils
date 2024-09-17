"""   input/output interfaces, such as `file`, `ftp`, `smtp`  
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
# /path/to/interpreter/python

from packaging.version import Version
from .version import __version__, __doc__, __details__  

from .ftp import send, receive
from .smtp import send

