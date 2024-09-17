## \file src/utils/interface/__init__.py
## \file ../src/utils/file/__init__.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
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
...

from packaging.version import Version
from .version import __version__, __name__, __doc__, __details__, __annotations__, __examples__, __author__  


from .image import save_png, save_png_from_url
from .video import save_video_from_url
from .file import read_text_file, save_text_file,  get_directory_names, get_filenames, recursive_get_filenames
from .csv import csv_to_json, json_to_csv, save_csv_file,  read_csv_file


...

