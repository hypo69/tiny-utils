
# `pprint` Function

The `pprint` function is designed for enhanced data output formatting to improve readability. It allows for "pretty-printing" 
various data types such as dictionaries, lists, strings, and objects, as well as reading and printing the contents of text files including CSV and XLS/XLSX files.

Pretty-print complex data **structures** for easier readability.

  **String Data**: Prints strings directly or reads and prints file contents if        the string represents a file path.
   - *Dictionaries*: Pretty-prints dictionaries in a readable JSON format, converting Path objects to strings for compatibility.
   - *Lists*: Formats and prints lists, ensuring Path objects are converted to strings.
   - *Objects*: Prints detailed information about objects, including class name, base classes, methods, and properties.
  *File Handling:*
   - *Text Files*: Reads and prints the content of .txt files.
   - *CSV Files*: Reads and prints the first few lines of .csv files.
   - *XLS/XLSX Files*: Reads and prints the first few rows of .xls and .xlsx files.
 *Error Handling*: Outputs error messages for issues encountered while reading files or printing data, allowing for graceful error management.
## How the function works:

1. **String Data Printing**: If the provided argument is a string, the function checks whether it represents a file path. If it does, the function reads the file's contents and prints them. If the string is not a file path, the function simply prints the string.

2. **Dictionary Printing**: If the argument is a dictionary, the function converts all `Path` objects to strings to ensure correct JSON serialization. It then prints the dictionary in a JSON format with indents to enhance readability.

3. **List Printing**: If the argument is a list, the function converts all `Path` objects in the list to strings and uses the standard `pprint` function to format the list.

4. **Object Printing**: If the argument is an object, the function uses `pprint` to print the object along with additional information about its class, methods, and properties. The function outputs the class name, its base classes, and lists the object's methods and properties, simplifying the analysis of its structure.

5. **File Handling**:
   - **Text Files**: For `.txt` files, it reads the contents and prints them.
   - **CSV Files**: For `.csv` files, it reads and prints the first few lines.
   - **XLS/XLSX Files**: For `.xls` and `.xlsx` files, it reads and prints the first few rows.

6. **Error Handling**: If an error occurs while reading a file or printing data, the function outputs an error message and continues printing the data.

## Examples of `pprint` usage:

### Example 1: String Data

```python
# Printing a simple string
pprint("Hello, World!")
```

**Output**:

```
Hello, World!
```

### Example 2: Lists

```python
from pathlib import Path

example_list = [
    "Hello, World!",
    Path("C:/example/path"),
    42,
    {"key": "value"}
]

pprint(example_list)
```

**Output**:

```
[
    "Hello, World!",
    "C:/example/path",
    42,
    {
        "key": "value"
    }
]
```

### Example 3: Dictionaries

```python
from pathlib import Path
import json

example_dict = {
    "name": "Alice",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "Wonderland"
    },
    "files": [Path("C:/file1.txt"), Path("C:/file2.txt")]
}

pprint(example_dict)
```

**Output**:

```json
{
    "name": "Alice",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "Wonderland"
    },
    "files": [
        "C:/file1.txt",
        "C:/file2.txt"
    ]
}
```

### Example 4: Objects of Class `MyClass`

```python
class MyClass:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def display(self):
        return f"{self.name} has value {self.value}"

# Create an instance of the class
obj = MyClass(name="TestObject", value=100)

# Print object information
pprint(obj)
```

**Output**:

```
Class: MyClass
Bases: ('object',)
Methods:
display()
Properties:
name = TestObject
value = 100
```

### Example 5: Printing from a JSON File

**Contents of `example.json`**:

```json
{
    "name": "Bob",
    "age": 25,
    "city": "New York",
    "skills": ["Python", "Data Science"]
}
```

```python
pprint('example.json')
```

**Output**:

```json
{
    "name": "Bob",
    "age": 25,
    "city": "New York",
    "skills": [
        "Python",
        "Data Science"
    ]
}
```

### Example 6: Printing from a TXT File

**Contents of `example_list.txt`**:

```plaintext
Line 1: This is a line from the file.
Line 2: Here's another line.
Line 3: And one more for good measure.
```

```python
pprint('example_list.txt')
```

**Output**:

```
Line 1: This is a line from the file.
Line 2: Here's another line.
Line 3: And one more for good measure.
```

### Example 7: Printing from a CSV File

**Contents of `example.csv`**:

```csv
name,age,city
Alice,30,Wonderland
Bob,25,New York
Charlie,35,Paris
```

```python
pprint('example.csv', max_lines=2)
```

**Output**:

```
CSV Header: ['name', 'age', 'city']
Row 1: ['Alice', '30', 'Wonderland']
Row 2: ['Bob', '25', 'New York']
```

### Example 8: Printing from an XLSX File

**Contents of `example.xlsx`**:

```
| name    | age | city       |
|---------|-----|------------|
| Alice   | 30  | Wonderland |
| Bob     | 25  | New York   |
| Charlie | 35  | Paris      |
```

```python
pprint('example.xlsx', max_lines=2)
```

**Output**:

```
   name  age         city
0  Alice   30  Wonderland
1    Bob   25    New York
```

### Example 9: Handling Unsupported File Formats

```python
# Attempting to read an unsupported file format
pprint('data.txt')
```

**Output**:

```
Unsupported file format: .txt
```

### Example 10: Handling Errors

```python
# Attempting to read from a non-existent file
pprint('non_existent_file.csv')
```

**Output**:

```
Error reading CSV file: [Error details]
```
