## \file ../src/utils/file/video.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
"""Сохранение видео."""

import aiohttp
import aiofiles
from pathlib import Path
from typing import Optional
import asyncio
from src.logger import logger

async def save_video_from_url(url: str, save_path: str) -> Optional[Path]:
    """Скачивает видео по URL и сохраняет его локально асинхронно.

    Args:
        url (str): URL для скачивания видео.
        save_path (str): Путь для сохранения видео.

    Returns:
        Optional[Path]: Путь к сохраненному файлу или `None` в случае неудачи.

    Example:
        >>> asyncio.run(save_video_from_url("https://example.com/video.mp4", "local_video.mp4"))
        PosixPath('local_video.mp4')
    """
    save_path = Path(save_path)

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()  # Проверка на успешное выполнение запроса

                save_path.parent.mkdir(parents=True, exist_ok=True)

                async with aiofiles.open(save_path, "wb") as file:
                    # Чтение данных из ответа по частям
                    while True:
                        chunk = await response.content.read(8192)
                        if not chunk:
                            break
                        await file.write(chunk)

        # Проверка записи файла
        if not save_path.exists():
            logger.error(f"Файл {save_path=} не был записан.")
            return

        # Проверка сохранения
        if save_path.stat().st_size == 0:
            logger.error(f"Файл {save_path=} сохранен, но его размер равен 0 байт.")
            return

    except Exception as ex:
        logger.error(
            f"Произошла ошибка при сохранении видео {save_path=}:", ex, exc_info=True
        )
        return

    return save_path


def get_video_data(file_name: str) -> Optional[bytes]:
    """Получает бинарные данные видеофайла, если файл существует.

    Args:
        file_name (str): Путь к видеофайлу для чтения.

    Returns:
        Optional[bytes]: Бинарные данные файла, если файл существует, или `None`, если файл не найден или произошла ошибка.

    Example:
        >>> get_video_data("local_video.mp4")
        b'\x00\x00\x00...'
    """
    file_path = Path(file_name)

    if not file_path.exists():
        logger.error(f"Файл {file_path=} не существует.")
        return

    try:
        with open(file_path, "rb") as file:
            return file.read()
    except Exception as ex:
        logger.error(f"Ошибка при чтении файла {file_path=}", ex, exc_info=True)
        return


def main():
    url = "https://example.com/video.mp4"
    save_path = "local_video.mp4"
    asyncio.run(save_video_from_url(url, save_path))


if __name__ == "__main__":
    main()
