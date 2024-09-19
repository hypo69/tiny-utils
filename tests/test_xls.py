""" """
## \file ../tests/test_printer.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
import pytest
import os
import json
import pandas as pd
from src.utils.xls import xls2dict, xls_to_json, xls_to_json_all_sheets, json_to_xls

@pytest.fixture
def example_xls(tmpdir):
    """Creates a temporary Excel file with multiple sheets for testing."""
    file_path = tmpdir.join("example.xlsx")
    
    # Creating test data for the Excel file
    df1 = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30]})
    df2 = pd.DataFrame({'City': ['New York', 'Paris'], 'Country': ['USA', 'France']})
    
    # Save to Excel with multiple sheets
    with pd.ExcelWriter(file_path) as writer:
        df1.to_excel(writer, sheet_name='Sheet1', index=False)
        df2.to_excel(writer, sheet_name='Sheet2', index=False)
    
    return file_path

@pytest.fixture
def example_json(tmpdir):
    """Creates a temporary JSON file for testing."""
    json_data = [{'Name': 'Alice', 'Age': 25}, {'Name': 'Bob', 'Age': 30}]
    json_file = tmpdir.join("output.json")
    with open(json_file, 'w') as f:
        json.dump(json_data, f, indent=4)
    return json_file

def test_xls2dict_single_sheet(example_xls):
    """Test conversion of a single sheet from Excel to a JSON dictionary."""
    result = xls2dict(str(example_xls), sheet_name='Sheet1')
    assert isinstance(result, list)
    assert result == [{'Name': 'Alice', 'Age': 25}, {'Name': 'Bob', 'Age': 30}]

def test_xls2dict_all_sheets(example_xls):
    """Test conversion of all sheets from Excel to JSON."""
    result = xls2dict(str(example_xls))
    assert isinstance(result, dict)
    assert 'Sheet1' in result and 'Sheet2' in result
    assert result['Sheet1'] == [{'Name': 'Alice', 'Age': 25}, {'Name': 'Bob', 'Age': 30}]
    assert result['Sheet2'] == [{'City': 'New York', 'Country': 'USA'}, {'City': 'Paris', 'Country': 'France'}]

def test_xls_to_json(example_xls, tmpdir):
    """Test conversion of Excel to JSON and saving the result."""
    json_file = tmpdir.join("output.json")
    result = xls_to_json(str(example_xls), str(json_file))
    
    # Check if the JSON file was saved correctly
    assert os.path.exists(json_file)
    
    with open(json_file, 'r') as f:
        saved_data = json.load(f)
    
    assert 'Sheet1' in saved_data
    assert 'Sheet2' in saved_data

def test_xls_to_json_all_sheets(example_xls, tmpdir):
    """Test conversion of all sheets in Excel to JSON and saving the result."""
    json_file = tmpdir.join("output_all_sheets.json")
    result = xls_to_json_all_sheets(str(example_xls), str(json_file))
    
    assert result == True
    assert os.path.exists(json_file)
    
    with open(json_file, 'r') as f:
        saved_data = json.load(f)
    
    assert 'Sheet1' in saved_data
    assert 'Sheet2' in saved_data

def test_json_to_xls(example_json, tmpdir):
    """Test conversion of JSON back to Excel."""
    xls_file = tmpdir.join("output.xlsx")
    with open(example_json, 'r') as f:
        json_data = json.load(f)
    
    result = json_to_xls(json_data, str(xls_file))
    
    assert result == True
    assert os.path.exists(xls_file)
    
    # Verify the Excel content
    df = pd.read_excel(xls_file)
    assert df.equals(pd.DataFrame(json_data))

def test_invalid_xls_file():
    """Test handling of an invalid or non-existent Excel file."""
    result = xls2dict("nonexistent_file.xlsx")
    assert result == False
