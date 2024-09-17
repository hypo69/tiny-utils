## \file ../src/utils/interface/_pytest/test_image.py
## \file src/utils/interface/_pytest/test_image.py
# \file tests/test_image.py
import pytest
from pathlib import Path
from src.utils.interface.image import save_png_from_url, save_png
from unittest.mock import patch, mock_open

# Mock logger to avoid actual logging during tests
from src.logger import logger

# Mock logger to avoid actual logging during tests
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

