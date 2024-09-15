## \file src/utils/string/formatter.py
## \file ../src/utils/string/formatter.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
"""! функции форматирвания строк
Форматирование строк:
remove_line_breaks(input_str: str) -> str
remove_htmls(input_html: str) -> str
html_escape(input_html: str) -> str
remove_non_latin_characters(input_str: str) -> str
remove_special_characters(input_str: str | list) -> str
escapes_to_html(text: str) -> str
symbols2UTF(text: str) -> str
clear_numbers(input_str: str) -> str
Преобразование данных:
convert_to_list(input: str | list[str, dict, list[dict]], delimiter: str = ',') -> list | bool
extract_value_from_parentheses_with_lead_dollar(input_str: str) -> str | list | bool
clean_url_from_protocols(url: str) -> str
"""
import re
import html
from typing import List, Dict
from urllib.parse import urlparse, parse_qs
from src.logger import logger
from .html_escapes import html_escapes

class StringFormatter:
    """!  
    StringFormatter (String Formatting):
    
    @details 
    This module provides functions for formatting strings in a specific style or using a particular template. 
    These may include tools for inserting variables into a string, changing the case of characters, removing or replacing substrings, etc.
    """
    @staticmethod
    def remove_line_breaks(input_str: str) -> str:
        """!
        Removes line breaks from the input string.
        
        @param input_str : str : input string
        @returns  str : A string with line breaks removed.
        """
        ...
    

    @staticmethod
    def remove_htmls(input_html: str) -> str:
        """!
        Removes HTML tags from the input string.
        
        @param input_html : str : input HTML string
        @returns str : A string with HTML tags removed.
        """
        ...

    @staticmethod
    def escape_html_tags(input_html: str) -> str:
        """!
        Replaces `<` and `>` with `&lt;` and `&gt;` in the input HTML string.
        
        @param input_html : str : input HTML string
        @returns str : An escaped HTML string.
        """
        return html.escape(input_html)
    
    @staticmethod
    def escape_to_html(text: str) -> str:
        """!
        Replaces non-Latin characters and digits with HTML entities.
        
        @param text : str : input text
        @returns str : Output text with non-Latin characters replaced by HTML entities
        """
        return ''.join(html_escapes[char] if char in html_escapes else char for char in text)
    
    @staticmethod
    def remove_non_latin_characters(input_str: str) -> str:
        """
        Removes non-latin characters from the input string.
        
        @param input_str : str : input string
        @returns str : A string with non-latin characters removed.
        """
        #return Ptrn.remove_non_latin_characters.sub(r' ', input_str).strip()
    
    @staticmethod
    def remove_special_characters(input_str: str | list) -> str:
        """!  
        Removes special characters not allowed in the 'name' field in Prestashop.
        f.e. `#`, `<`, `>
        
        @param input_str : str or list : input string or list of strings
        @returns str : Processed string with special characters removed.
        """
        ...
    


        
    @staticmethod
    def clear_numbers(input_str) -> str:
        """
         Clear string from not decimal numbers or points

        Parameters : 
             input_str : input string
        Returns : 
             str : clear string
            
            @code
            > input_str = 'aaa123.456 cde'
            > output_str = clear_numbers(input_str)
            > print(output_str)
            > 123.456

        """
        ...





