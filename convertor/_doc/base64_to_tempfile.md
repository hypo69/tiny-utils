
### Подробное описание

1. **Импорты:**
    ```python
    from xml.dom.minidom import getDOMImplementation
    from builtins import str
    import base64
    import tempfile
    import mimetypes
    import os
    ```
    - `getDOMImplementation`, `str`, `mimetypes` не используются в этом скрипте и могут быть удалены.
    - `base64`: используется для декодирования строки, закодированной в Base64.
    - `tempfile`: используется для создания временных файлов.
    - `os`: используется для работы с путями к файлам.

2. **Функция `base64_to_tmpfile`:**
    ```python
    def base64_to_tmpfile(content, file_name):
        _, ext = os.path.splitext(file_name)
        path = ''
        with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp:
            tmp.write(base64.b64decode(content))
            path = tmp.name

        return path
    ```

    - **Аргументы:**
        - `content`: строка, закодированная в Base64.
        - `file_name`: имя файла, из которого извлекается расширение.

    - **Описание:**
        1. `_, ext = os.path.splitext(file_name)`: Извлекает расширение файла из `file_name`. Переменная `ext` будет содержать расширение файла (например, `.txt`, `.png` и т.д.).
        2. `path = ''`: Инициализирует переменную `path` пустой строкой.
        3. `with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp`: Создает временный файл с тем же расширением, что и у `file_name`. Файл не будет удален автоматически после закрытия, так как `delete=False`.
        4. `tmp.write(base64.b64decode(content))`: Декодирует содержимое из Base64 и записывает его в временный файл.
        5. `path = tmp.name`: Сохраняет путь к временному файлу в переменной `path`.
        6. `return path`: Возвращает путь к временному файлу.

### Пример использования

```python
base64_content = "SGVsbG8gd29ybGQh"  # Base64 закодированное содержимое "Hello world!"
file_name = "example.txt"

tmp_file_path = base64_to_tmpfile(base64_content, file_name)
print(f"Temporary file created at: {tmp_file_path}")
```

Этот пример создает временный файл `example.txt` с содержимым `Hello world!` и выводит путь к этому файлу.

### Примечания
- **Безопасность**: Функция создает временные файлы, которые не удаляются автоматически. Убедитесь, что временные файлы удаляются вручную, чтобы избежать утечек ресурсов.
- **Использование Base64**: Base64 используется для кодирования двоичных данных в текстовый формат, что удобно для передачи данных через текстовые протоколы, такие как HTTP.