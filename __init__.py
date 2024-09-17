## \file ../src/utils/__init__.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python

"""
# tiny_tools Module

The `tiny_tools` module is a collection of small, useful utilities designed to simplify common programming tasks. It includes tools for data conversion, file handling, and formatted output. This module is intended to help streamline your coding process by providing straightforward and reusable functions.

## Overview

### Modules Included

#### `convertor`
Functions for data conversion and handling.
- **`json2csv_dict2csv`**: Convert JSON and dictionaries to CSV format.
- **`TextToImageGenerator`**: Generate images from text.
- **`version`**: Manage versioning information.
- **`xls2dict`**: Convert XLS files to dictionaries.
- **`xml2dict`**: Convert XML data to dictionaries.
- **`base64_to_tmpfile`**: Convert base64 encoded data to a temporary file.
- **`csv2json_csv2dict`**: Convert CSV files to JSON and dictionary formats.
- **`dict2ns_ns2dict`**: Convert dictionaries to SimpleNamespace objects and vice versa.
- **`dict2xml`**: Convert dictionaries to XML format.
- **`html2esc`**: Convert HTML to escaped characters.

#### `printer`
Functions for pretty-printing data structures.
- **`pprint`**: Pretty-print complex data structures for easier readability.

#### `jjson`
Functions for working with JSON data.
- **`j_loads`**: Load JSON data from a string.
- **`j_loads_ns`**: Load JSON data from a string into SimpleNamespace objects.
- **`j_dumps`**: Dump data to a JSON string.

#### `file`
Utilities for file operations.
- **`get_directory_names`**: Retrieve names of directories within a given path.
- **`get_filenames`**: Retrieve names of files within a given path.
- **`read_text_file`**: Read the contents of a text file.
- **`save_text_file`**: Save content to a text file.
- **`recursive_get_filenames`**: Recursively retrieve filenames within a directory.
- **`save_png`**: Save PNG images.
- **`save_png_from_url`**: Save a PNG image from a URL.
- **`save_video_from_url`**: Save a video file from a URL.

## Usage

The `tiny_tools` module is designed for ease of use. 

(WIKI:)[https://github.com/hypo69/tiny-utils/wiki] 
"""
...
from .version import __version__, __doc__, __details__

from src.logger import logger
from src.utils.convertors import (json2csv_dict2csv,
                        TextToImageGenerator,
                        xls2dict,
                        xml2dict,
                        base64_to_tmpfile,
                        csv2json_csv2dict,
                        dict2ns_ns2dict,
                        dict2xml,
                        html2esc,
                        )

from src.utils.printer import  pprint
from src.utils.jjson import j_loads, j_loads_ns, j_dumps
#from src.interface import ftp, smtp, check_port
from src.utils.file import (get_directory_names, 
                    get_filenames, 
                    read_text_file, 
                    save_text_file, 
                    recursive_get_filenames
                    )
from src.utils.file import save_png, save_png_from_url
from src.utils.file import save_video_from_url

#from .cursor_spinner import show_spinner, spinning_cursor

