""" """
## \file ../tests/test_video.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
import pytest
import aiohttp
import aiofiles
from unittest.mock import patch, mock_open, AsyncMock
from pathlib import Path
from src.utils.file.video import save_video_from_url, get_video_data


@pytest.mark.asyncio
async def test_save_video_from_url_success(monkeypatch, tmp_path):
    # Mock the URL and path for saving
    url = "https://example.com/video.mp4"
    save_path = tmp_path / "video.mp4"

    # Mock aiohttp response and content
    async def mock_get(*args, **kwargs):
        mock_resp = AsyncMock()
        mock_resp.content.read = AsyncMock(side_effect=[b"video_data", b""])
        mock_resp.raise_for_status = AsyncMock()
        return mock_resp

    # Patch aiohttp.ClientSession to use the mock_get function
    monkeypatch.setattr(aiohttp.ClientSession, "get", mock_get)

    # Mock aiofiles for writing the file
    mocked_open = mock_open()
    monkeypatch.setattr(aiofiles, "open", mocked_open)

    # Run the function
    result = await save_video_from_url(url, str(save_path))

    # Assert the save path was returned
    assert result == save_path

    # Check if the directory was created
    assert save_path.parent.exists()

    # Check if the file was written
    mocked_open.assert_called_once_with(save_path, "wb")


@pytest.mark.asyncio
async def test_save_video_from_url_failure(monkeypatch):
    # Mock the URL and invalid save path
    url = "https://example.com/video.mp4"
    save_path = "/invalid_path/video.mp4"

    # Mock aiohttp response and content
    async def mock_get(*args, **kwargs):
        mock_resp = AsyncMock()
        mock_resp.content.read = AsyncMock(side_effect=[b"", b""])
        mock_resp.raise_for_status = AsyncMock()
        return mock_resp

    # Patch aiohttp.ClientSession to use the mock_get function
    monkeypatch.setattr(aiohttp.ClientSession, "get", mock_get)

    # Patch aiofiles to raise an exception for invalid path
    monkeypatch.setattr(aiofiles, "open", AsyncMock(side_effect=OSError("Permission denied")))

    # Run the function
    result = await save_video_from_url(url, save_path)

    # Assert None is returned due to failure
    assert result is None


def test_get_video_data_success(monkeypatch, tmp_path):
    # Create a temporary file with binary data
    file_path = tmp_path / "video.mp4"
    file_data = b"video_data"
    file_path.write_bytes(file_data)

    # Call the function
    result = get_video_data(str(file_path))

    # Assert that the binary data matches
    assert result == file_data


def test_get_video_data_file_not_found():
    # Call the function with a non-existent file
    result = get_video_data("non_existent_video.mp4")

    # Assert that None is returned
    assert result is None


def test_get_video_data_read_error(monkeypatch):
    # Mock open to raise an IOError when attempting to read
    monkeypatch.setattr("builtins.open", mock_open(side_effect=OSError("Read error")))

    # Call the function with a valid path but simulating an error
    result = get_video_data("invalid_file.mp4")

    # Assert that None is returned
    assert result is None
