## \file ../src/utils/convertors/__init__.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
""" Convertors
"""
...
from packaging.version import Version
from .version import __version__, __doc__, __details__  

from .csv import (csv2dict, 
                    csv2ns,
                    )

from .dict import (dict2json, 
                    dict2ns, 
                    dict2xls, 
                    dict2xml, 
                    dict2csv,
                    dict2html
                    )

from .html import (html2escape, 
                    html2ns, 
                    html2dict, 
                    escape2html,
                    ) 
from .json import (json2csv, 
                   json2ns, 
                   json2xls, 
                   json2xml
                    )

from .ns import (ns2csv, 
                    ns2dict, 
                    ns2json, 
                    ns2xls, 
                    ns2xml
                    )

from .xml2dict import xml2dict                                                        
from .base64_to_tmpfile import base64_to_tmpfile
from .text2png import TextToImageGenerator


