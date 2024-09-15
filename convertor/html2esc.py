"""! HTML to escape sequences converter
@rst
from src.utils.convertor.html2esc import html2escape
.. module:: html2esc
   :synopsis: A module for converting HTML to escape sequences.

.. function:: html2escape(input_str: str) -> str

   Converts HTML code into escape sequences.

   :param input_str: The HTML code to be converted.
   :returns: The HTML converted into escape sequences.

ASCII Workflow Algorithm:

+--------------------+
|       Start        |
+--------------------+
         |
         v
+--------------------+
|  Receive input     |
|  (HTML string)     |
+--------------------+
         |
         v
+--------------------+
|  Call html2escape  |
|  function          |
+--------------------+
         |
         v
+--------------------+
|  Convert HTML      |
|  to escape         |
|  sequences         |
+--------------------+
         |
         v
+--------------------+
|  Return result     |
|  (escape string)   |
+--------------------+
         |
         v
+--------------------+
|       End          |
+--------------------+
@endrst
@code
# Example usage of the html2escape function
html_code = "<div>Hello, World!</div>"
escaped_code = html2escape(html_code)
print(escaped_code)  # Output: &lt;div&gt;Hello, World!&lt;/div&gt;
@endcode
"""
# \file ../src/utils/convertor/html2esc.py
## \file ../src/utils/convertor/html2esc.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

from src.utils.string import StringFormatter

def html2escape(input_str: str) -> str:
    """! Converts HTML to escape sequences
    @param input_str: The HTML code
    @returns: HTML converted into escape sequences
    """
    ...
    return StringFormatter.escape_html_tags(input_str)
