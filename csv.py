# \file ../src/utils/file/csv_file.py
## \file ../src/utils/file/csv.py
# -*- coding: utf-8 -*-
"""Module for CSV file operations.

This module provides functions for saving and reading CSV files, including:
- Saving data to a CSV file.
- Reading data from a CSV file.
- Converting data from JSON to CSV and vice versa.

Functions:
    save_csv_file(data: List[Dict[str, str]], file_path: str | Path, mode: str = 'a', exc_info: bool = True) -> bool:
        Saves a list of dictionaries to a CSV file.

    read_csv_file(file_path: str | Path, exc_info: bool = True) -> List[Dict[str, str]] | None:
        Reads the content of a CSV file and returns it as a list of dictionaries.

    json_to_csv(json_data: List[Dict[str, str]], csv_file_path: str | Path, exc_info: bool = True) -> bool:
        Converts a list of dictionaries from JSON format to a CSV file.

    csv_to_json(csv_file_path: str | Path, json_file_path: str | Path, exc_info: bool = True) -> List[Dict[str, str]] | None:
        Converts a CSV file to JSON format and saves it to a JSON file.

Examples:
    >>> data = [{'role': 'user', 'content': 'Hello'}, {'role': 'assistant', 'content': 'Hi there!'}]
    >>> success = save_csv_file(data=data, file_path='dialogue_log.csv')
    >>> print(success)
    True

    >>> data = read_csv_file(file_path='dialogue_log.csv')
    >>> print(data)
    [{'role': 'user', 'content': 'Hello'}, {'role': 'assistant', 'content': 'Hi there!'}]

    >>> json_data = [{'role': 'user', 'content': 'Hello'}, {'role': 'assistant', 'content': 'Hi there!'}]
    >>> success = json_to_csv(json_data, 'dialogue_log.csv')
    >>> print(success)
    True

    >>> json_data = csv_to_json('dialogue_log.csv', 'dialogue_log.json')
    >>> print(json_data)
    [{'role': 'user', 'content': 'Hello'}, {'role': 'assistant', 'content': 'Hi there!'}]
"""
import csv
import json
from pathlib import Path
from typing import List, Dict, Union
from src.logger import logger

def save_csv_file(
    data: List[Dict[str, str]],
    file_path: str | Path,
    mode: str = 'a',
    exc_info: bool = True
) -> bool:
    """Save a list of dictionaries to a CSV file.

    Args:
        data (List[Dict[str, str]]): The data to be written to the CSV file.
        file_path (str | Path): The full path to the CSV file.
        mode (str, optional): The file mode. Defaults to 'a' (append).
        exc_info (bool, optional): If True, includes traceback information in the log. Defaults to True.

    Returns:
        bool: True if successful, else False.

    Example:
        >>> data = [{'role': 'user', 'content': 'Hello'}]
        >>> success = save_csv_file(data=data, file_path='dialogue_log.csv')
        >>> print(success)
        True
    """
    try:
        file_path = Path(file_path)
        file_exists = file_path.exists()
        file_path.parent.mkdir(parents=True, exist_ok=True)

        if data:
            fieldnames = list(data[0].keys())
        else:
            fieldnames = []

        with file_path.open(mode, newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if not file_exists and fieldnames:
                writer.writeheader()
            writer.writerows(data)
        return True
    except Exception as ex:
        logger.error(f"Failed to save CSV file {file_path}.", ex, exc_info=exc_info)
        return False

def read_csv_file(
    file_path: str | Path,
    exc_info: bool = True
) -> List[Dict[str, str]] | None:
    """Read the content of a CSV file.

    Args:
        file_path (str | Path): The path to the CSV file.
        exc_info (bool, optional): If True, includes traceback information in the log. Defaults to True.

    Returns:
        List[Dict[str, str]] | None: The CSV file content as a list of dictionaries, or None if an error occurred.

    Example:
        >>> data = read_csv_file(file_path='dialogue_log.csv')
        >>> print(data)
        [{'role': 'user', 'content': 'Hello'}, {'role': 'assistant', 'content': 'Hi there!'}]
    """
    path = Path(file_path)
    if path.is_file():
        try:
            with path.open('r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                return list(reader)
        except Exception as ex:
            if exc_info:
                logger.error(f"Failed to read CSV file {file_path}.", ex, exc_info=exc_info)
            return None
    else:
        logger.warning(f"File '{file_path}' does not exist.")
        return None

def json_to_csv(
    json_data: List[Dict[str, str]],
    csv_file_path: str | Path,
    exc_info: bool = True
) -> bool:
    """Convert a list of dictionaries from JSON format to a CSV file.

    Args:
        json_data (List[Dict[str, str]]): The JSON data to be converted to CSV.
        csv_file_path (str | Path): The path to the CSV file to write.
        exc_info (bool, optional): If True, includes traceback information in the log. Defaults to True.

    Returns:
        bool: True if successful, else False.

    Example:
        >>> json_data = [{'role': 'user', 'content': 'Hello'}]
        >>> success = json_to_csv(json_data, 'dialogue_log.csv')
        >>> print(success)
        True
    """
    return save_csv_file(data=json_data, file_path=csv_file_path, exc_info=exc_info)

def csv_to_json(
    csv_file_path: str | Path,
    json_file_path: str | Path,
    exc_info: bool = True
) -> List[Dict[str, str]] | None:
    """Convert CSV data to JSON format and save to a JSON file.

    Args:
        csv_file_path (str | Path): The path to the CSV file to read.
        json_file_path (str | Path): The path to the JSON file to write.
        exc_info (bool, optional): If True, includes traceback information in the log. Defaults to True.

    Returns:
        List[Dict[str, str]] | None: The CSV data as a list of dictionaries, or None if an error occurred.

    Example:
        >>> data = csv_to_json('dialogue_log.csv', 'dialogue_log.json')
        >>> print(data)
        [{'role': 'user', 'content': 'Hello'}, {'role': 'assistant', 'content': 'Hi there!'}]
    """
    data = read_csv_file(csv_file_path)
    if data is None:
        return None
    try:
        with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, ensure_ascii=False, indent=4)
        return data
    except Exception as ex:
        logger.error(f"Failed to write JSON file {json_file_path}.", ex, exc_info=exc_info)
        return None
