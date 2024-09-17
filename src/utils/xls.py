## \file ../src/utils/xls.py
# -*- coding: utf-8 -*-
#! /path/to/python/interpreter
"""
Converter for Excel (`xls`) to JSON and JSON to Excel (`xls`).
This module provides functions to convert Excel files to JSON format, handle multiple sheets, and save JSON data back to Excel files.
"""

import pandas as pd
import json
from typing import List, Dict, Union
from types import SimpleNamespace

def xls2dict(
    xls_file: str,
    json_file: str = None,
    sheet_name: Union[str, int] = None
) -> Union[Dict, List[Dict], bool]:
    """
    Convert an Excel file to JSON format. Optionally, convert a specific sheet and save the result to a JSON file.

    Args:
        xls_file (str): Path to the input Excel file.
        json_file (str, optional): Path to the output JSON file. If not provided, JSON data is not saved to a file.
        sheet_name (Union[str, int], optional): The sheet name or index to convert. If not specified, all sheets are processed.

    Returns:
        Union[Dict, List[Dict], bool]: JSON data as a dictionary or list of dictionaries, or False if an error occurred.

    Example:
        >>> data = xls2dict('input.xlsx', 'output.json')
        >>> print(data)
        {'Sheet1': [{'column1': 'value1', 'column2': 'value2'}]}
    """
    try:
        # Load the Excel file
        xls = pd.ExcelFile(xls_file)
        
        if sheet_name is None:
            # Convert all sheets to JSON
            all_sheets_data = {}
            for sheet in xls.sheet_names:
                df = pd.read_excel(xls, sheet_name=sheet)
                all_sheets_data[sheet] = df.to_dict(orient='records')
            data_dict = all_sheets_data
        else:
            # Convert specified sheet to JSON
            df = pd.read_excel(xls, sheet_name=sheet_name)
            data_dict = df.to_dict(orient='records')

        if json_file:
            # Save JSON to file if path is provided
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(data_dict, f, ensure_ascii=False, indent=4)
        
        return data_dict
    
    except Exception as ex:
        print(f"Error occurred: {ex}")
        return False


def xls_to_json(xls_file: str, json_file: str = None) -> Union[Dict, List[Dict], bool]:
    """
    Convert an Excel file to JSON format and optionally save to a JSON file.

    Args:
        xls_file (str): Path to the input Excel file.
        json_file (str, optional): Path to the output JSON file. If not provided, JSON data is not saved to a file.

    Returns:
        Union[Dict, List[Dict], bool]: JSON data as a dictionary or list of dictionaries, or False if an error occurred.

    Example:
        >>> data = xls_to_json('input.xlsx', 'output.json')
        >>> print(data)
        [{'column1': 'value1', 'column2': 'value2'}]
    """
    return xls2dict(xls_file=xls_file, json_file=json_file)


def xls_to_json_all_sheets(xls_file: str, json_file: str) -> bool:
    """
    Convert all sheets in an Excel file to JSON format and save them to a single JSON file.

    Args:
        xls_file (str): Path to the input Excel file.
        json_file (str): Path to the output JSON file.

    Returns:
        bool: True if successful, else False.

    Example:
        >>> success = xls_to_json_all_sheets('input.xlsx', 'all_sheets_output.json')
        >>> print(success)
        True
    """
    try:
        all_sheets_data = xls2dict(xls_file=xls_file)
        if isinstance(all_sheets_data, dict):
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(all_sheets_data, f, ensure_ascii=False, indent=4)
            return True
        return False
    except Exception as ex:
        print(f"Error occurred: {ex}")
        return False


def json_to_xls(json_data: List[Dict[str, str]], xls_file_path: str) -> bool:
    """
    Convert JSON data to an Excel file.

    Args:
        json_data (List[Dict[str, str]]): The JSON data to be converted to Excel.
        xls_file_path (str): Path to the output Excel file.

    Returns:
        bool: True if successful, else False.

    Example:
        >>> json_data = [{'column1': 'value1', 'column2': 'value2'}]
        >>> success = json_to_xls(json_data, 'output.xlsx')
        >>> print(success)
        True
    """
    try:
        df = pd.DataFrame(json_data)
        df.to_excel(xls_file_path, index=False)
        return True
    except Exception as ex:
        print(f"Error occurred: {ex}")
        return False
