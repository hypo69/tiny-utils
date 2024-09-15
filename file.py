## \file ../src/utils/file/file.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

"""Module for file operations.

This module provides functions for importing and exporting files, including:
- Saving text to a file.
- Getting all filenames from a specified directory.
- Getting all directory names from a specified directory.

Functions:
    save_text_file(data: str | list | dict, file_path: str | Path, mode: str = 'w', exc_info: bool = True) -> bool:
        Saves the provided data to a file in the specified path.

    read_text_file(file_path: str | Path, get_list: bool = False, exc_info: bool = True) -> list | None:
        Reads the content of a text file and returns it either as a string or a list of strings.

    get_filenames(directory: str | Path, extensions: str | List[str] = '*', exc_info: bool = True) -> list[str]:
        Retrieves all filenames from the specified directory, optionally filtered by file extension.

    get_directory_names(directory: str | Path, exc_info: bool = True) -> list[str]:
        Retrieves all directory names from the specified directory.

Examples:
    >>> success: bool = save_text_file(data="Hello World", file_path="/path/to/file.txt")
    >>> file_content: str = read_text_file(file_path="/path/to/file.txt")
    >>> filenames: list[str] = get_filenames(directory="/path/to/directory")
    >>> dir_names: list[str] = get_directory_names(directory="/path/to/directory")
"""

import os
import json
import fnmatch
from typing import List, Optional, Union
from pathlib import Path
from src.logger import logger



def save_text_file(
    data: str | list | dict,
    file_path: str | Path,
    mode: str = "w",
    exc_info: bool = True,
) -> bool:
    """Saves the provided data to a file.

    Args:
        data (str | list | dict): The data to be written to the file.
        file_path (str | Path): The full path to the file.
        mode (str, optional): The writing mode. Defaults to 'w'.
            - 'w' to overwrite data.
            - 'a' to append to data.
        exc_info (bool, optional): If True, includes traceback information in the log. Defaults to True.

    Returns:
        bool: True if successful, else False.

    Example:
        >>> success: bool = save_text_file(data="Hello, World!", file_path="output.txt")
        >>> print(success)
        True

        >>> # Handling exceptions by forcing a failure (e.g., invalid file path)
        >>> success: bool = save_text_file(data="This will fail", file_path="/invalid/path/output.txt")
        >>> print(success)
        False
    """

    try:
        file_path = Path(file_path)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open(mode) as file:
            if isinstance(data, list):
                for line in data:
                    file.write(f"{line}\n")
            else:
                file.write(data)
        return True
    except Exception as ex:
        logger.error(f"Failed to save file {file_path}.", ex, exc_info=exc_info)
        return False


def read_text_file(
    file_path: str | Path, get_list: bool = False, exc_info: bool = True
) -> list | None:
    """Reads the content of a text file.

    Args:
        file_path (str | Path): The path to the text file.
        get_list (bool, optional): If True, returns the content as a list of lines. Defaults to False.
        exc_info (bool, optional): If True, includes traceback information in the log. Defaults to True.

    Returns:
        list[str] | None: A list of lines if `get_list` is True, otherwise the entire content as a single string.

    Example:
        >>> lines: list[str] = read_text_file(file_path="example.txt", get_list=True)
        >>> print(lines)
        ['Line 1', 'Line 2', 'Line 3']

        >>> content: str = read_text_file(file_path="example.txt")
        >>> print(content)
        'Line 1\nLine 2\nLine 3'
    """
    path = Path(file_path)
    if path.is_file():
        try:
            with path.open("r", encoding="utf-8") as file:
                if get_list:
                    return [line.strip() for line in file]
                else:
                    return file.read()
        except Exception as ex:
            if exc_info:
                logger.error(f"Failed to read file {file_path}.", ex, exc_info=exc_info)
            return None
    else:
        logger.warning(f"File '{file_path}' does not exist.")
        return None


def get_filenames(
    directory: str | Path, extensions: str | List[str] = "*", exc_info: bool = True
) -> list[str]:
    """Gets all filenames from the specified directory.

    Args:
        directory (str | Path): Path to the directory for getting files.
        extensions (str | List[str], optional): File extensions to filter by. Can be a single string or a list of strings. Use '*' to get all files. Defaults to '*'.
        exc_info (bool, optional): If True, includes traceback information in the log. Defaults to True.

    Returns:
        list[str]: List of filenames.

    Example:
        >>> files: list[str] = get_filenames(directory=".", extensions="*.py")
        >>> print(files)
        ['file1.py', 'file2.py']
    """
    try:
        path = Path(directory)
        if isinstance(extensions, str):
            if extensions == "*":
                extensions = []  # If '*' is specified, no filtering by extension
            else:
                extensions = [extensions]  # Convert a single extension to a list

        # Normalize extensions to have a leading dot
        extensions = [ext if ext.startswith(".") else f".{ext}" for ext in extensions]

        filenames = []
        for file in path.iterdir():
            if file.is_file() and (not extensions or file.suffix in extensions):
                filenames.append(file.name)
        return filenames
    except Exception as ex:
        if exc_info:
            logger.warning(
                f"Failed to get filenames from directory '{directory}'.",
                ex,
                exc_info=exc_info,
            )
        return []


def get_directory_names(directory: str | Path, exc_info: bool = True) -> list[str]:
    """Gets all directory names from the specified directory.

    Args:
        directory (str | Path): Path to the directory for getting directories.
        exc_info (bool, optional): If True, includes traceback information in the log. Defaults to True.

    Returns:
        list[str]: List of directory names.

    Example:
        >>> directories: list[str] = get_directory_names(directory=".")
        >>> print(directories
