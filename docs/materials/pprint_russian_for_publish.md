Вот обновленный текст для публикации, включающий код:

---

**10 минут кода. Улучшаем `pprint()` для печати сложных структур**

Сталкивались с трудностями при выводе на печать сложных структур данных в Python? В своих проектах я использую расширенную версию функции `pprint()` из библиотеки `pprint`, которая улучшает форматирование и упрощает отладку.

**Что нового?**

**Универсальная обработка данных:**

- **Строки:** Если строка представляет собой путь к файлу, функция читает и форматирует содержимое файла. В противном случае просто выводит строку.
- **Словари:** Преобразует объекты `Path` в строки и форматирует словарь как JSON для лучшей читаемости.
- **Списки:** Аналогично словарям, преобразует объекты `Path` в строки и выводит список.
- **Другие типы данных:** Выводит данные напрямую и, если это объект, предоставляет дополнительную информацию о классе.

**Информация о классах:**

- **Детали класса:** Функция `_print_class_info()` выводит имена классов, методы и свойства, помогая лучше понять структуру объектов.

**Как использовать?**

```python
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
```

**Почему это полезно?**

- **Улучшенная читаемость:** Форматирование данных как JSON или преобразование объектов в строки помогает быстро понять сложные структуры.
- **Эффективная отладка:** Четкий, структурированный вывод облегчает поиск проблем и проверку корректности данных.
- **Полезная информация о классах:** `_print_class_info()` предоставляет ценную информацию о экземплярах классов, упрощая отладку и разработку.

Попробуйте эту расширенную функцию `pprint()` в своих проектах и посмотрите, как она может упростить работу с данными!

Не стесняйтесь задавать вопросы или делиться своим опытом использования `pprint()`.

---