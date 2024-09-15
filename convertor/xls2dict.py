"""! Converter `xls` -> `json` 
@code 
out_dict = xls_to_json('input.xlsx','output.json')
@endcode
"""
## \file ../src/utils/convertor/xls2dict.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

import pandas as pd
import json
from typing import List, Dict
from types import SimpleNamespace

def xls2dict(xls_file:str, json_file:str = None) -> SimpleNamespace | List[SimpleNamespace] | bool:
    """! Convert Excel file to JSON.
    @param input_file (str): Path to the input Excel file.
    @param output_file (str): Path to the output JSON file.
    @returns product_dict_ns `SimpleNamespace`: Словарь/список полей товара в формате
    @returns None, если был пустой список
    @returns False, в случае ошибки
    """
    ...
    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel (xls_file)
    
    # Convert DataFrame to JSON
    _ = df.to_json (orient='records')
    data_dict = json.loads(_)
    
    if json_file:
        # Сохранение JSON в файл, если указан путь
        with open(json_file, 'w') as f:
            json.dump(data_dict, f)
            
    ...
    return data_dict

