""" """
## \file ../tests/dict2ns_ns2dict.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python

import pytest
from types import SimpleNamespace


def dict2namespace(data) -> SimpleNamespace:
    """ Recursively convert dictionaries to `SimpleNamespace`.

    @param data: The data to convert.
    @returns: Converted data as a `SimpleNamespace`.
    """
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, dict):
                data[key] = dict2namespace(value)
            elif isinstance(value, list):
                data[key] = [dict2namespace(item) if isinstance(
                    item, dict) else item for item in value]
        return SimpleNamespace(**data)
    elif isinstance(data, list):
        return [dict2namespace(item) if isinstance(item, dict) else item for item in data]
    return data

def namespace2dict(ns: SimpleNamespace) -> dict:
    """ Recursively convert `SimpleNamespace` to dictionaries.

    @param ns: The `SimpleNamespace` to convert.
    @returns: Converted data as a dictionary.
    """
    if isinstance(ns, SimpleNamespace):
        return {key: namespace2dict(value) if isinstance(value, SimpleNamespace) or isinstance(value, list) else value
                for key, value in ns.__dict__.items()}
    elif isinstance(ns, list):
        return [namespace2dict(item) if isinstance(item, SimpleNamespace) or isinstance(item, dict) else item
                for item in ns]
    return ns

# _test_dict2namespace.py


def test_dict_to_namespace():
    """Test conversion of a simple dictionary to SimpleNamespace."""
    data = {'a': 1, 'b': 2}
    result = dict2namespace(data)
    assert isinstance(result, SimpleNamespace)
    assert result.a == 1
    assert result.b == 2


def test_nested_dict_to_namespace():
    """Test conversion of a nested dictionary to SimpleNamespace."""
    data = {'a': 1, 'b': {'c': 3, 'd': 4}}
    result = dict2namespace(data)
    assert isinstance(result, SimpleNamespace)
    assert result.b.c == 3
    assert result.b.d == 4


def test_list_of_dicts_to_namespace():
    """Test conversion of a list of dictionaries to SimpleNamespace."""
    data = [{'a': 1}, {'b': 2}]
    result = dict2namespace(data)
    assert isinstance(result, list)
    assert isinstance(result[0], SimpleNamespace)
    assert result[0].a == 1
    assert isinstance(result[1], SimpleNamespace)
    assert result[1].b == 2


def test_mixed_list_to_namespace():
    """Test conversion of a mixed list containing dictionaries and other types."""
    data = [1, {'a': 2}, 3]
    result = dict2namespace(data)
    assert isinstance(result, list)
    assert result[0] == 1
    assert isinstance(result[1], SimpleNamespace)
    assert result[1].a == 2
    assert result[2] == 3


def test_empty_dict_to_namespace():
    """Test conversion of an empty dictionary to SimpleNamespace."""
    data = {}
    result = dict2namespace(data)
    assert isinstance(result, SimpleNamespace)


def test_empty_list_to_namespace():
    """Test conversion of an empty list to SimpleNamespace."""
    data = []
    result = dict2namespace(data)
    assert result == []



def test_dict_to_namespace():
    """Test conversion of a simple dictionary to SimpleNamespace."""
    data = {'a': 1, 'b': 2}
    result = dict2namespace(data)
    assert isinstance(result, SimpleNamespace)
    assert result.a == 1
    assert result.b == 2


def test_nested_dict_to_namespace():
    """Test conversion of a nested dictionary to SimpleNamespace."""
    data = {'a': 1, 'b': {'c': 3, 'd': 4}}
    result = dict2namespace(data)
    assert isinstance(result, SimpleNamespace)
    assert result.b.c == 3
    assert result.b.d == 4


def test_list_of_dicts_to_namespace():
    """Test conversion of a list of dictionaries to SimpleNamespace."""
    data = [{'a': 1}, {'b': 2}]
    result = dict2namespace(data)
    assert isinstance(result, list)
    assert isinstance(result[0], SimpleNamespace)
    assert result[0].a == 1
    assert isinstance(result[1], SimpleNamespace)
    assert result[1].b == 2


def test_mixed_list_to_namespace():
    """Test conversion of a mixed list containing dictionaries and other types."""
    data = [{'a': 1}, 2, {'b': 3}]
    result = dict2namespace(data)
    assert isinstance(result, list)
    assert isinstance(result[0], SimpleNamespace)
    assert result[0].a == 1
    assert result[1] == 2
    assert isinstance(result[2], SimpleNamespace)
    assert result[2].b == 3


def test_empty_dict_to_namespace():
    """Test conversion of an empty dictionary to SimpleNamespace."""
    data = {}
    result = dict2namespace(data)
    assert isinstance(result, SimpleNamespace)


def test_empty_list_to_namespace():
    """Test conversion of an empty list to SimpleNamespace."""
    data = []
    result = dict2namespace(data)
    assert result == []