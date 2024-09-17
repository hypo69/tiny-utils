## \file src/utils/interface/_pytest/test_file.py
## \file ../src/utils/interface/_pytest/test_file.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
""" 
 - test_save_text_file:
        Проверяет запись данных в файл в различных форматах (текст, JSON) и в режимах w и a.
        Проверяет создание директорий при необходимости.
        
 - test_read_text_file:
        Проверяет чтение файла как списка строк и как одной строки.
        Проверяет случай отсутствия файла и неправильного типа возвращаемых данных.
        
 - test_get_filenames:
        Проверяет получение всех файлов, файлов с определенными расширениями и с одним расширением.
        Проверяет обработку недопустимого пути директории.
        
 - test_get_directory_names:
    Проверяет получение всех директорий из заданной директории.
    Проверяет обработку недопустимого пути директории.
"""
...
# \file tests/test_file.py
import pytest
from pathlib import Path
from src.utils.file import save_text_file, read_text_file, get_filenames, get_directory_names
from src.logger import logger

# Test for save_text_file function
def test_save_text_file(tmp_path):
    """Test the save_text_file function."""

    # Define test data and file path
    test_data = {'key': 'value'}
    file_name = tmp_path / 'test_file.json'

    # Test saving a dict to a JSON file
    assert save_text_file(test_data, file_name) is True
    assert file_name.exists()
    with file_name.open('r', encoding='utf-8') as f:
        assert f.read() == '{"key": "value"}'

    # Test appending text to a file
    file_name = tmp_path / 'test_file.txt'
    assert save_text_file('Initial content', file_name, 'w') is True
    assert save_text_file('\nAppended content', file_name, 'a') is True
    with file_name.open('r', encoding='utf-8') as f:
        assert f.read() == 'Initial content\nAppended content'

    # Test saving a list to a JSON file
    test_data = [1, 2, 3]
    file_name = tmp_path / 'test_file_list.json'
    assert save_text_file(test_data, file_name) is True
    with file_name.open('r', encoding='utf-8') as f:
        assert f.read() == '[1, 2, 3]'

# Test for read_text_file function
def test_read_text_file(tmp_path):
    """Test the read_text_file function."""

    # Define test data and file path
    file_name = tmp_path / 'test_file.txt'
    with file_name.open('w', encoding='utf-8') as f:
        f.write('Line 1\nLine 2\nLine 3')

    # Test reading file as a list of lines
    lines = read_text_file(file_name, list)
    assert lines == ['Line 1', 'Line 2', 'Line 3']

    # Test reading file as a single string
    content = read_text_file(file_name, str)
    assert content == 'Line 1\nLine 2\nLine 3'

    # Test reading from a non-existent file
    assert read_text_file(tmp_path / 'non_existent_file.txt', str) is None

    # Test invalid return type
    with pytest.raises(ValueError):
        read_text_file(file_name, int)

# Test for get_filenames function
def test_get_filenames(tmp_path):
    """Test the get_filenames function."""

    # Create some test files
    (tmp_path / 'test1.txt').write_text('content1')
    (tmp_path / 'test2.csv').write_text('content2')
    (tmp_path / 'test3.json').write_text('content3')
    (tmp_path / 'test4.doc').write_text('content4')

    # Test getting all filenames
    filenames = get_filenames(tmp_path, '*')
    assert sorted(filenames) == ['test1.txt', 'test2.csv', 'test3.json', 'test4.doc']

    # Test getting filenames with specific extensions
    filenames = get_filenames(tmp_path, ['txt', 'csv'])
    assert sorted(filenames) == ['test1.txt', 'test2.csv']

    # Test getting filenames with a single extension
    filenames = get_filenames(tmp_path, '.json')
    assert filenames == ['test3.json']

    # Test handling of invalid directory path
    assert get_filenames(tmp_path / 'non_existent_dir', '*') == []

# Test for get_directory_names function
def test_get_directory_names(tmp_path):
    """Test the get_directory_names function."""

    # Create some test directories
    (tmp_path / 'dir1').mkdir()
    (tmp_path / 'dir2').mkdir()
    (tmp_path / 'dir3').mkdir()

    # Create a test file
    (tmp_path / 'test_file.txt').write_text('content')

    # Test getting directory names
    directories = get_directory_names(tmp_path)
    assert sorted(directories) == ['dir1', 'dir2', 'dir3']

    # Test handling of invalid directory path
    assert get_directory_names(tmp_path / 'non_existent_dir') == []



