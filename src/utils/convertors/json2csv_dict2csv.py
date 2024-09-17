"""
@rst
.. module:: json2csv_dict2csv
   :platform: Unix
   :synopsis: A module for converting JSON data to CSV format and saving dictionaries to CSV files.
.. moduleauthor:: Your Name <your.email@example.com>

Convert JSON data to CSV format with a comma delimiter.

:param json_data: JSON data as a string, list of dictionaries, or file path to a JSON file.
:param csv_file: Path to the CSV file to write.
:raises Exception: If unable to parse JSON or write CSV.

Save a list of dictionaries to a CSV file.

:param data: List of dictionaries where each dictionary represents a row in the CSV.
:param csv_file: Path to the CSV file where the data will be saved.
:raises ValueError: If the data list is empty.

**Example:**
    ::
        sample_data = [
            {'role': 'user', 'content': 'How can I save this dictionary to CSV?'},
            {'role': 'assistant', 'content': 'You can use the csv module in Python.', 'sentiment': 'neutral'},
            {'role': 'user', 'content': 'What if some fields are missing?'}
        ]
        dict2csv(sample_data, 'output.csv')
@endrst

@code
# Example usage:

# Using JSON list of dictionaries
json_data_list = [{"name": "John", "age": 30, "city": "New York"}, {"name": "Alice", "age": 25, "city": "Los Angeles"}]

# Convert JSON to CSV
json2csv(json_data_list, 'data.csv')

# Convert CSV back to JSON
csv2json('data.csv', 'data.json')
@endcode
"""

## \file ../src/utils/convertor/json2csv_dict2csv.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
import header   
import json
import csv
from types import SimpleNamespace
from pathlib import Path
from typing import Tuple, List, Dict
from src.logger import logger

def json2csv(json_data: str | list | dict | Path, csv_file: str | Path) -> None:
    """
    Convert JSON data or JSON file to CSV format with a comma delimiter.

    @param json_data: JSON data as a string, list of dictionaries, or file path to a JSON file.
    @param csv_file: Path to the CSV file to write.

    @throws Exception: If unable to parse JSON or write CSV.
    """
    try:
        # Load JSON data
        if isinstance(json_data, dict):
            data = [json_data]
        elif isinstance(json_data, str):
            data = json.loads(json_data)
        elif isinstance(json_data, list):
            data = json_data
        elif isinstance(json_data, Path):
            with open(json_data, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
        else:
            raise ValueError("Unsupported type for json_data")

        # Extract column headers from the first dictionary in the list
        headers = list(data[0].keys())

        # Write data to CSV with a comma delimiter
        with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
    except Exception as ex:
        # Handle errors and log them
        logger.error("Failed to convert JSON to CSV", ex)
        raise

def dict2csv(data: list[dict] | SimpleNamespace, csv_file: str | Path) -> None:
    """
    Save a list of dictionaries to a CSV file.

    @param data: List of dictionaries where each dictionary represents a row in the CSV.
    @param csv_file: Path to the CSV file where the data will be saved.

    @throws ValueError: If the data list is empty.
    """
    if not data:
        raise ValueError("The data list is empty.")

    # Determine the unique fieldnames across all dictionaries
    fieldnames = set()
    for entry in data:
        fieldnames.update(entry.keys())
    fieldnames = list(fieldnames)  # Convert to list for DictWriter

    try:
        # Write the data to CSV
        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Write the header
            writer.writeheader()

            # Write the data rows
            writer.writerows(data)

    except Exception as ex:
        # Log any exceptions that occur
        logger.error(f"Error with csv_file: {csv_file}", ex)
        ...
