Конечно! Вот обновленный текст:

```markdown
# Enhanced Print Formatting Module

## Overview

The `printer.py` module provides enhanced print formatting for better readability of data structures. It supports pretty-printing of dictionaries, lists, and objects, with customization for handling `Path` objects and displaying class information. It also includes functionality to read and print lines from text files.

## Module Code

```python
# -*- coding: utf-8 -*-
"""! Module for enhanced print formatting for better readability of structures

@todo Check here: https://prettyprinter.readthedocs.io/en/latest/index.html#
@code
# Example usage
example_data = {
    "path": Path("C:/example/path"),
    "name": "example"
}

pprint(example_data)

class A:
    def __init__(self, var_1: str, var_2: bool = False):
        ...

pprint(A)

# Example of reading and printing from a file
pprint('example_list.txt')
@code
"""

import json
from pathlib import Path
from pprint import pprint as pretty_print

def pprint(print_data=None, end: str = '\n'):
    """Pretty print output formatting"""
    if not print_data:
        return
    
    if isinstance(print_data, str):
        # Check if the string is a file path
        if Path(print_data).exists():
            try:
                with open(print_data, 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                print(''.join(lines), end=end)
            except Exception as e:
                print(f"Error reading file {print_data}: {e}", end=end)
        else:
            print(print_data, end=end)
        return
    
    try:
        if isinstance(print_data, dict):
            # Convert Path objects to strings for correct JSON serialization
            print_data = {key: str(value) if isinstance(value, Path) else value for key, value in print_data.items()}
            print(json.dumps(print_data, indent=4, ensure_ascii=False), end=end)
        elif isinstance(print_data, list):
            # Convert Path objects to strings in lists
            print_data = [str(item) if isinstance(item, Path) else item for item in print_data]
            pretty_print(print_data, end=end)
        else:
            pretty_print(print_data, end=end)
            if hasattr(print_data, '__class__'):
                class_name = print_data.__class__.__name__
                class_bases = print_data.__class__.__bases__
                print(f"Class: {class_name}", end=end)
                if class_bases:
                    print(f"Bases: {pretty_print([base.__name__ for base in class_bases], end=end)}", end=end)

                attributes_and_methods = dir(print_data)
                methods = []
                properties = []

                for attr in attributes_and_methods:
                    if not attr.startswith('__'):
                        try:
                            value = getattr(print_data, attr)
                        except Exception as ex:
                            value = f"Error getting attribute {attr}: {ex}"
                        if callable(value):
                            methods.append(f"{attr}()")
                        else:
                            properties.append(f"{attr} = {value}")

                print("Methods:", end=end)
                for method in sorted(methods):
                    print(method, end=end)
                print("Properties:", end=end)
                for prop in sorted(properties):
                    print(prop, end=end)
    except Exception as ex:
        print(f"Error in pprint function: {ex}", end=end)
        print(print_data, end=end)
```

## Usage

### Example Data

```python
import json
from pathlib import Path

# Example JSON data
example_json = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "skills": ["Python", "JavaScript", "SQL"]
}
pprint(example_json)
```

### Example Data with Path Objects

```python
from pathlib import Path

example_data = {
    "path": Path("C:/example/path"),
    "name": "example"
}
pprint(example_data)
```

### Example Class

```python
class MyClass:
    def __init__(self, var_1: str, var_2: bool = False):
        self.var_1 = var_1
        self.var_2 = var_2

    def method(self):
        pass

pprint(MyClass)
```

### Example File Reading

Assuming you have a file named `example_list.txt` with some content:

```plaintext
Line 1: Hello, World!
Line 2: This is an example file.
Line 3: It contains multiple lines.
```

You can print its contents using:

```python
pprint('example_list.txt')
```

## Features

- **String Data**: Directly prints string data.
- **Dictionaries**: Converts `Path` objects to strings and prints JSON-formatted dictionaries.
- **Lists**: Converts `Path` objects to strings in lists and uses pretty-print.
- **Objects**: Prints class information, including class name, bases, methods, and properties.
- **File Reading**: Reads and prints contents from text files.

## Notes

- Убедись, что библиотека `prettyprinter` установлена для улучшенного форматирования.
- Функция `pprint` обрабатывает различные типы данных и форматирует вывод соответствующим образом.
```