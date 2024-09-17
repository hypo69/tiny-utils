### Руководство для тестера

#### Введение

Этот документ предназначен для тестирования модуля `image.py`, который отвечает за сохранение изображений из URL и локальные бинарные данные. В данном руководстве описаны инструкции по тестированию функций `save_png_from_url` и `save_png`, а также приведены примеры использования тестов.

#### Установка и настройка

1. **Создайте виртуальное окружение**:
    ```bash
    python -m venv venv
    ```

2. **Активируйте виртуальное окружение**:
    - На Windows:
        ```bash
        venv\Scripts\activate
        ```
    - На MacOS/Linux:
        ```bash
        source venv/bin/activate
        ```

3. **Установите зависимости**:
    ```bash
    pip install -r requirements.txt
    pip install pytest mock pillow
    ```

#### Запуск тестов

Тесты для модуля `image.py` находятся в директории `tests`. Для запуска тестов выполните следующую команду в корневой директории проекта:

```bash
pytest tests/test_image.py
```

#### Тестируемые функции

1. **`save_png_from_url`**:
    - Скачивает изображение по URL и сохраняет его локально.
    - Принимает на вход URL изображения, имя файла для сохранения и флаг `exc_info` для логирования информации об исключениях.

2. **`save_png`**:
    - Сохраняет изображение в формате PNG из бинарных данных.
    - Принимает на вход бинарные данные изображения, имя файла для сохранения и флаг `exc_info` для логирования информации об исключениях.

#### Написание тестов

Тесты для функций написаны с использованием библиотеки `pytest` и `unittest.mock` для мокирования зависимостей и функций. Файл тестов находится по пути `tests/test_image.py`.

##### Структура тестов

1. **Импорт библиотек и функций**:
    ```python
    import pytest
    from pathlib import Path
    from src.utils.interface.image import save_png_from_url, save_png
    from unittest.mock import patch, mock_open
    from src.logger import logger
    ```

2. **Тестирование `save_png_from_url`**:
    ```python
    @patch.object(logger, 'error')
    @patch.object(logger, 'critical')
    @patch.object(logger, 'success')
    @patch.object(logger, 'debug')
    def test_save_png_from_url(mock_debug, mock_success, mock_critical, mock_error, tmp_path):
        """Test the save_png_from_url function."""

        # Mock URL and image data
        image_url = "http://example.com/image.png"
        image_data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x10\x08\x06\x00\x00\x00\x1f\xf3\xff\xa4\x00\x00\x00\x01sRGB\x00\xae\xce\x1c\xe9\x00\x00\x00'  # Sample PNG header
        filename = tmp_path / 'downloaded_image.png'

        with patch('requests.get') as mock_get:
            mock_get.return_value.content = image_data
            mock_get.return_value.raise_for_status = lambda: None

            # Test downloading and saving the image
            result = save_png_from_url(image_url, filename)
            assert result == str(filename)
            assert filename.exists()

        # Test handling of request failure
        mock_get.side_effect = Exception("Failed to download")
        result = save_png_from_url(image_url, filename)
        assert result is None
        mock_error.assert_called_once_with("Ошибка при загрузке картинки", mock_get.side_effect, exc_info=True)

        # Test handling of invalid image data
        mock_get.side_effect = None
        mock_get.return_value.content = b'invalid data'
        result = save_png_from_url(image_url, filename)
        assert result is None
        mock_critical.assert_called_once_with(f"Ошибка при обработке ответа {pprint(mock_get.return_value)}", Exception(), exc_info=True)
    ```

3. **Тестирование `save_png`**:
    ```python
    @patch.object(logger, 'critical')
    @patch.object(logger, 'success')
    @patch.object(logger, 'debug')
    def test_save_png(mock_debug, mock_success, mock_critical, tmp_path):
        """Test the save_png function."""

        # Mock image data
        image_data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x10\x08\x06\x00\x00\x00\x1f\xf3\xff\xa4\x00\x00\x00\x01sRGB\x00\xae\xce\x1c\xe9\x00\x00\x00'  # Sample PNG header
        filename = tmp_path / 'saved_image.png'

        # Test saving the image
        result = save_png(image_data, filename)
        assert result == str(filename)
        assert filename.exists()

        # Test handling of invalid image data
        invalid_data = b'invalid data'
        result = save_png(invalid_data, filename)
        assert result is None
        mock_critical.assert_called_once_with(f"Не удалось сохранить файл {filename}", Exception(), exc_info=True)
    ```

#### Заключение

Это руководство описывает процесс тестирования модуля `image.py`. Следуя этим инструкциям, вы сможете убедиться в корректной работе функций для сохранения изображений и выявить возможные ошибки в их реализации.