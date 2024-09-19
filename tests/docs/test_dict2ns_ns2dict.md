# Guide for `dict2namespace` and `namespace2dict` Test Cases

This guide will explain how to test the `dict2namespace` and `namespace2dict` functions, which convert Python dictionaries to `SimpleNamespace` objects and vice versa. The testing framework used is `pytest`. Below is a step-by-step explanation of each test case and its purpose.

## Functions Overview

- **`dict2namespace(data)`**: This function recursively converts a dictionary or a list of dictionaries into a `SimpleNamespace` object.
  
- **`namespace2dict(ns)`**: This function converts a `SimpleNamespace` object (or a list of `SimpleNamespace` objects) back into a dictionary format.

## Installation

To run the tests, ensure that you have `pytest` installed:

```bash
pip install pytest
```

## Test Cases

### 1. `test_dict_to_namespace()`

**Purpose**: Verify the conversion of a simple dictionary to a `SimpleNamespace`.

- **Input**: `{'a': 1, 'b': 2}`
- **Expected Output**: `SimpleNamespace(a=1, b=2)`
  
### 2. `test_nested_dict_to_namespace()`

**Purpose**: Test the conversion of a nested dictionary structure.

- **Input**: `{'a': 1, 'b': {'c': 3, 'd': 4}}`
- **Expected Output**: A `SimpleNamespace` object with nested namespaces:
  ```python
  SimpleNamespace(a=1, b=SimpleNamespace(c=3, d=4))
  ```

### 3. `test_list_of_dicts_to_namespace()`

**Purpose**: Check if a list of dictionaries is correctly converted to a list of `SimpleNamespace` objects.

- **Input**: `[{'a': 1}, {'b': 2}]`
- **Expected Output**: A list of `SimpleNamespace` objects:
  ```python
  [SimpleNamespace(a=1), SimpleNamespace(b=2)]
  ```

### 4. `test_mixed_list_to_namespace()`

**Purpose**: Ensure that a list containing both dictionaries and other data types is converted correctly.

- **Input**: `[1, {'a': 2}, 3]`
- **Expected Output**: A list where the dictionary is converted to `SimpleNamespace`, and other values remain unchanged:
  ```python
  [1, SimpleNamespace(a=2), 3]
  ```

### 5. `test_empty_dict_to_namespace()`

**Purpose**: Check the behavior when an empty dictionary is passed.

- **Input**: `{}`
- **Expected Output**: An empty `SimpleNamespace` object.

### 6. `test_empty_list_to_namespace()`

**Purpose**: Test the conversion of an empty list.

- **Input**: `[]`
- **Expected Output**: An empty list.

## Running the Tests

You can run all the tests using the following command in your terminal:

```bash
pytest path/to/test_file.py
```

## Notes

- **Edge cases**: The tests cover typical use cases as well as edge cases like empty dictionaries and lists.
- **Custom handling**: If any of the input structures change (e.g., more complex data types), adjustments may be needed to ensure the code handles them properly.

## Example Test Execution

```bash
==================== test session starts ====================
platform linux -- Python 3.9.7, pytest-6.2.5
collected 6 items

test_dict2ns_ns2dict.py .......
==================== 7 passed in 0.05s ====================
```

This guide outlines how to effectively test the conversion functions and the expected outcomes.