## \file ./utils/printer.py
# -*- coding: utf-8 -*-
"""
This module provides enhanced print formatting for better readability of data structures.
It supports pretty-printing of dictionaries, lists, and objects, with customization for handling
`Path` objects and displaying class information. It also includes functionality for reading and printing lines from text files.

To view various examples of how to use the `pprint` function, open the `examples/pprint.ipynb` file. 
Here are the steps to open the file:
1. **Navigate to the `examples` directory**: Locate the `examples` folder within the project directory.
2. **Open the Jupyter Notebook**: Launch Jupyter Notebook or JupyterLab. If you don't have Jupyter installed, you can install it using `pip install notebook` and then start it with the command `jupyter notebook` or `jupyter lab`.
3. **Find the `pprint.ipynb` file**: In the Jupyter interface, browse to the `examples` directory and click on `pprint.ipynb` to open it.
4. **Explore the Examples**: The notebook contains code cells with different examples and explanations demonstrating how to use the `pprint` function and its features.

Following these steps will help you understand how to leverage the `pprint` function effectively in various scenarios.
"""
...
import json
from pathlib import Path
from typing import Any
from pprint import pprint as pretty_print


def pprint(print_data: str | list | dict | Any = None, *args, **kwargs) -> None:
    """ Pretty prints the given data in a formatted way.

    The function handles various data types and structures such as strings, dictionaries, lists, and objects.
    It also supports file reading if a file path is passed as a string.

    Args:
        print_data (Optional[any]): The data to be printed. It can be a string, dictionary, list, object, or file path. Defaults to `None`.
        *args: Additional positional arguments passed to the print or pretty_print function.
        **kwargs: Additional keyword arguments passed to the print or pretty_print function.

    Returns:
        None: The function prints the formatted output and does not return any value.

    Raises:
        Exception: If there is an error while reading the file or formatting the data.

    Example:
        >>> from pathlib import Path
        >>> pprint({'path': Path('/example/path'), 'name': 'example'})
        {
            "path": "/example/path",
            "name": "example"
        }
    """
    if not print_data:
        return

    if isinstance(print_data, str):
        # Check if the string is a file path
        if Path(print_data).exists():
            try:
                with open(print_data, 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                pretty_print(''.join(lines), *args, **kwargs)
            except Exception:
                # If an error occurs, just print the file path
                pretty_print(print_data, *args, **kwargs)
        else:
            pretty_print(print_data, *args, **kwargs)
        return

    try:
        if isinstance(print_data, dict):
            # Convert Path objects to strings for correct JSON serialization
            print_data = {key: str(value) if isinstance(value, Path) else value for key, value in print_data.items()}
            pretty_print(json.dumps(print_data, indent=4, ensure_ascii=False), *args, **kwargs)
        elif isinstance(print_data, list):
            # Convert Path objects to strings in lists
            print_data = [str(item) if isinstance(item, Path) else item for item in print_data]
            pretty_print(print_data, *args, **kwargs)
        else:
            pretty_print(print_data, *args, **kwargs)
            if hasattr(print_data, '__class__'):
                _print_class_info(print_data, *args, **kwargs)
    except Exception:
        # If an error occurs, just print the data
        pretty_print(print_data, *args, **kwargs)


def _print_class_info(instance: Any, *args, **kwargs) -> None:
    """ Prints class information including class name, bases, methods, and properties.

    This function is used internally by `pprint` to display detailed information about class instances.

    Args:
        instance (any): The class instance whose information is to be printed.
        *args: Additional positional arguments passed to the print function.
        **kwargs: Additional keyword arguments passed to the print function.

    Returns:
        None: The function prints the class information and does not return any value.

    Example:
        >>> class MyClass:
        ...     def __init__(self, var1: str, var2: bool = False):
        ...         self.var1 = var1
        ...         self.var2 = var2
        ...
        >>> obj = MyClass("value1", True)
        >>> _print_class_info(obj)
        Class: MyClass
        Methods:
        Properties:
        var1 = value1
        var2 = True
    """
    class_name = instance.__class__.__name__
    class_bases = instance.__class__.__bases__

    print(f"Class: {class_name}", *args, **kwargs)
    if class_bases:
        pretty_print([base.__name__ for base in class_bases], *args, **kwargs)

    attributes_and_methods = dir(instance)
    methods = []
    properties = []

    for attr in attributes_and_methods:
        if not attr.startswith('__'):
            try:
                value = getattr(instance, attr)
            except Exception:
                value = "Error getting attribute"
            if callable(value):
                methods.append(f"{attr}()")
            else:
                properties.append(f"{attr} = {value}")

    print("Methods:", *args, **kwargs)
    for method in sorted(methods):
        print(method, *args, **kwargs)
    print("Properties:", *args, **kwargs)
    for prop in sorted(properties):
        print(prop, *args, **kwargs)
