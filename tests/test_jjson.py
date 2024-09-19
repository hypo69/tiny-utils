""" """
## \file ../tests/test_jjson.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
import pytest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch, mock_open
import json
from src.utils.jjson.jjson import j_dumps, j_loads, j_loads_ns

# Test data
json_data = {"key": "value"}
namespace_data = SimpleNamespace(key="value")
json_str = '{"key": "value"}'
list_of_dicts = [{"key1": "value1"}, {"key2": "value2"}]
invalid_json_str = '{"key": "value"'
csv_data = [{"column1": "value1", "column2": "value2"}]


# Test j_dumps
@patch("builtins.open", new_callable=mock_open)
@patch("json.dump")
def test_j_dumps_json(mock_json_dump, mock_open_file):
    # Test JSON dumping to a file
    path = Path("test.json")
    result = j_dumps(json_data, path)
    mock_open_file.assert_called_once_with(path, "w", encoding="utf-8")
    mock_json_dump.assert_called_once_with(json_data, mock_open_file(), ensure_ascii=False)
    assert result == json_data


def test_j_dumps_return_data():
    # Test returning the JSON data as dictionary
    result = j_dumps(json_data)
    assert result == json_data


def test_j_dumps_namespace():
    # Test converting SimpleNamespace to dict and dumping
    result = j_dumps(namespace_data)
    assert result == {"key": "value"}


# Test j_loads
@patch("builtins.open", new_callable=mock_open, read_data=json_str)
@patch("json.load", return_value=json_data)
def test_j_loads_json(mock_json_load, mock_open_file):
    path = Path("test.json")
    result = j_loads(path)
    mock_open_file.assert_called_once_with(path, "r", encoding="utf-8")
    mock_json_load.assert_called_once()
    assert result == json_data


def test_j_loads_from_string():
    # Test loading from JSON string
    result = j_loads(json_str)
    assert result == json_data


@patch("src.utils.jjson.jjson._load_csv_from_file", return_value=csv_data)
def test_j_loads_csv(mock_load_csv):
    path = Path("test.csv")
    result = j_loads(path)
    mock_load_csv.assert_called_once_with(path)
    assert result == csv_data


def test_j_loads_invalid_json():
    # Test loading invalid JSON string
    with patch("json.loads", side_effect=json.JSONDecodeError("Expecting value", invalid_json_str, 0)):
        result = j_loads(invalid_json_str)
        assert result is False


# Test j_loads_ns
@patch("src.utils.jjson.jjson.j_loads", return_value=json_data)
@patch("src.utils.convertors.dict2namespace", return_value=namespace_data)
def test_j_loads_ns(mock_dict2namespace, mock_j_loads):
    path = Path("test.json")
    result = j_loads_ns(path)
    mock_j_loads.assert_called_once_with(path, ordered=False, exc_info=True)
    mock_dict2namespace.assert_called_once_with(json_data)
    assert result == namespace_data


@pytest.mark.parametrize("input_data, expected", [
    (json_str, SimpleNamespace(key="value")),
    ({"key": "value"}, SimpleNamespace(key="value")),
])
@patch("src.utils.convertors.dict2namespace", return_value=namespace_data)
def test_j_loads_ns_from_string(mock_dict2namespace, input_data, expected):
    result = j_loads_ns(input_data)
    mock_dict2namespace.assert_called_once()
    assert result == expected
