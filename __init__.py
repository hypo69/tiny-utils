## \file ../src/utils/__init__.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

"""
! tiny_tools module — a collection of small useful utilities.

This module initializes a variety of small utilities that simplify data conversion, file handling, 
and formatted output. The utilities included in this module support operations such as converting 
data formats, managing files, and parsing JSON.

Modules included:
- `convertor`: Functions for data conversion and handling.
  - `json2csv_dict2csv`: Convert JSON and dictionary to CSV.
  - `TextToImageGenerator`: Generate images from text.
  - `version`: Manage versioning information.
  - `xls2dict`: Convert XLS files to dictionaries.
  - `xml2dict`: Convert XML data to dictionaries.
  - `base64_to_tmpfile`: Convert base64 data to a temporary file.
  - `csv2json_csv2dict`: Convert CSV to JSON and dictionary formats.
  - `dict2ns_ns2dict`: Convert dictionaries to SimpleNamespace objects and vice versa.
  - `dict2xml`: Convert dictionaries to XML.
  - `html2esc`: Convert HTML to escaped characters.

- `printer`: Functions for pretty-printing data.
  - `pprint`: Pretty-print data structures.

- `jjson`: Functions for working with JSON data.
  - `j_loads`: Load JSON data from a string.
  - `j_loads_ns`: Load JSON data from a string into SimpleNamespace objects.
  - `j_dumps`: Dump data to a JSON string.

- `file`: Utilities for file operations.
  - `get_directory_names`: Retrieve names of directories within a path.
  - `get_filenames`: Retrieve names of files within a path.
  - `read_text_file`: Read the contents of a text file.
  - `save_text_file`: Save content to a text file.
  - `recursive_get_filenames`: Recursively retrieve filenames within a directory.
  - `save_png`: Save PNG images.
  - `save_png_from_url`: Save a PNG image from a URL.
  - `save_video_from_url`: Save a video file from a URL.
"""
...
from packaging.version import Version
from .version import __version__, __doc__, __details__

from .convertor import (json2csv_dict2csv,
                        TextToImageGenerator,
                        version,
                        xls2dict,
                        xml2dict,
                        base64_to_tmpfile,
                        csv2json_csv2dict,
                        dict2ns_ns2dict,
                        dict2xml,
                        html2esc,
                        )

from .printer import  pprint
from .jjson import j_loads, j_loads_ns, j_dumps
#from .interface import ftp, smtp
from .file import (get_directory_names, 
                    get_filenames, 
                    read_text_file, 
                    save_text_file, 
                    recursive_get_filenames
                    )
from .file import save_png, save_png_from_url
from .file import save_video_from_url

#from .cursor_spinner import show_spinner, spinning_cursor
"""! """

