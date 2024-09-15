## \file ../src/utils/convertor/csv2json_csv2dict.py
## \file ../src/utils/convertor/csv2json_csv2dict.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
"""!
@code
# Example usage:

# Using JSON list of dictionaries
json_data_list = [{"name": "John", "age": 30, "city": "New York"}, {"name": "Alice", "age": 25, "city": "Los Angeles"}]
json_file_path = 'data.json'
csv_file_path = 'data.csv'

# Convert JSON to CSV
json2csv.json2csv(json_data_list, csv_file_path)

# Convert CSV back to JSON
csv_data = csv2json(csv_file_path, json_file_path)
if csv_data:
    if isinstance(csv_data, list):
        if isinstance(csv_data[0], dict):
            print("CSV data (list of dictionaries):")
        else:
            print("CSV data (list of values):")
        print(csv_data)
    else:
        print("Failed to read CSV data.")
@endcode
"""

import json
import csv
from pathlib import Path
from typing import Union
from src.logger import logger

def csv2dict(csv_file: str | Path) -> Union[dict, bool]:
    """
    Convert CSV data to JSON format and return the data as a list of dictionaries or list of values.

    @param csv_file: Path to the CSV file to read.

    @return: Dictionary containing the data from CSV converted to JSON format,
             or False if conversion failed.

    @throws Exception: If unable to read CSV.
    """
    try:
        with open(csv_file, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            rows = [row for row in reader]

        if len(rows[0]) == 1:
            # If there is only one column, return a list of values
            return {"data": [row[0] for row in rows]}
        else:
            # Otherwise, assume multiple columns and return a list of dictionaries
            headers = rows[0]
            data = [dict(zip(headers, row)) for row in rows[1:]]
            return {"data": data}
    except Exception as ex:
        logger.error("Failed to convert CSV to JSON", ex)
        return False

def csv2json(csv_file: str | Path, json_file: str | Path) -> dict:
    """!
    Convert CSV data to JSON format and save to a JSON file.

    @param csv_file: Path to the CSV file to read.
    @param json_file: Path to the JSON file to write.

    @return: Dictionary containing the data from CSV converted to JSON format,
             or False if conversion failed.

    @throws Exception: If unable to read CSV or write JSON.
    """
    data = csv2dict(csv_file)
    if data is False:
        return {"error": "Failed to convert CSV to JSON"}

    try:
        with open(json_file, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, ensure_ascii=False, indent=4)
        return data
    except Exception as ex:
        logger.error("Failed to write JSON file", ex)
        return {"error": "Failed to write JSON file"}


