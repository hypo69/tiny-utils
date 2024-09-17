## \file ../src/utils/convertors/dicst2ns_ns2dict.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
"""Converter for converting between dict and SimpleNamespace objects.

This module contains functions to recursively convert dictionaries to SimpleNamespace
objects and vice versa.
"""

from types import SimpleNamespace
from typing import Any, Dict, List, Union

def dict2ns(data: Union[Dict[str, Any], List[Any]]) -> Any:
    """Recursively convert dictionaries to SimpleNamespace.

    Args:
        data (Union[Dict[str, Any], List[Any]]): The data to convert.

    Returns:
        Any: Converted data as a SimpleNamespace or list of SimpleNamespace.
    """
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, dict):
                data[key] = dict2ns(value)
            elif isinstance(value, list):
                data[key] = [dict2ns(item) if isinstance(item, dict) else item for item in value]
        return SimpleNamespace(**data)
    elif isinstance(data, list):
        return [dict2ns(item) if isinstance(item, dict) else item for item in data]
    return data

def ns2dict(data: Any) -> Union[Dict[str, Any], List[Any]]:
    """Recursively convert SimpleNamespace objects to dictionaries.

    Args:
        data (Any): The data to convert.

    Returns:
        Union[Dict[str, Any], List[Any]]: Converted data as a dictionary or list of dictionaries.
    """
    if isinstance(data, SimpleNamespace):
        return {key: ns2dict(value) for key, value in vars(data).items()}
    elif isinstance(data, list):
        return [ns2dict(item) for item in data]
    return data
