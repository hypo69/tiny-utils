"""! Convert Base64 encoded content to a temporary file  """
## \file ../src/utils/convertor/base64_to_tmpfile.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
...
from xml.dom.minidom import getDOMImplementation
from builtins import str
import base64
import tempfile
import mimetypes
import os


def base64_to_tmpfile(content:base64,file_name:str) -> str:
    """! Convert Base64 encoded content to a temporary file.

    This function decodes the Base64 encoded content and writes it to a temporary file with the same extension as the provided file name. 
    The path to the temporary file is returned.

    @param content: Base64 encoded content.
    @param file_name: Name of the file to extract the extension from.
    
    @return: Path to the temporary file.
    
    @code
    base64_content = "SGVsbG8gd29ybGQh"  # Base64 закодированное содержимое "Hello world!"
    file_name = "example.txt"

    tmp_file_path = base64_to_tmpfile(base64_content, file_name)
    print(f"Temporary file created at: {tmp_file_path}")
    @code
    """
    ...
    _,ext = os.path.splitext(file_name)
    path = ''
    with  tempfile.NamedTemporaryFile(delete=False,suffix=ext) as tmp:
        tmp.write(base64.b64decode(content))
        path = tmp.name

    return path

