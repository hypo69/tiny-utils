## \file ../src/utils/file/image.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

"""Сохранение изображений."""

import aiohttp
import aiofiles
from PIL import Image
from pathlib import Path
import asyncio
from src.logger import logger
from src.utils import pprint


async def save_png_from_url(
    image_url: str, filename: str | Path
) -> str | None:
    """Скачивает изображение по URL и сохраняет его локально асинхронно.

    Args:
        image_url (str): URL для скачивания изображения.
        filename (str | Path): Имя файла для сохранения.

    Returns:
        str | None: Путь к сохраненному файлу или `None` в случае неудачи.

    Example:
        >>> asyncio.run(save_png_from_url("https://example.com/image.png", "local_image.png"))
        'local_image.png'
    """
    ...
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(image_url) as response:
                response.raise_for_status()
                image_data = await response.read()
    except Exception as ex:
        logger.error("Ошибка при загрузке картинки", ex, exc_info=True)
        return

    return await save_png(image_data, filename)


async def save_png(image_data: bytes, file_name: str | Path) -> str | None:
    """Сохраняет изображение в формате PNG асинхронно.

    Args:
        image_data (bytes): Бинарные данные изображения.
        file_name (str | Path): Имя файла для сохранения.

    Returns:
        str | None: Путь к сохраненному файлу или `None` в случае неудачи.

    Example:
        >>> with open("example_image.png", "rb") as f:
        ...     image_data = f.read()
        >>> asyncio.run(save_png(image_data, "saved_image.png"))
        'saved_image.png'
    """
    ...
    file_path = Path(file_name)

    try:
        # Создание необходимых директорий
        file_path.parent.mkdir(parents=True, exist_ok=True)

        # Запись файла
        async with aiofiles.open(file_path, "wb") as file:
            await file.write(image_data)

        # Проверка записи файла
        if not file_path.exists():
            logger.error(f"Файл {file_path=} не был записан.")
            return

        # Открытие и сохранение изображения
        image = Image.open(file_path)
        image.save(file_path, "PNG")

        # Проверка сохранения
        if file_path.stat().st_size == 0:
            logger.error(f"Файл {file_path=} сохранен, но его размер равен 0 байт.")
            return

    except Exception as ex:
        logger.critical(f"Не удалось сохранить файл {file_path=}", ex, exc_info=True)
        return

    return str(file_path)


def get_file_data(file_name: str | Path) -> bytes | None:
    """Получает бинарные данные файла, если файл существует.

    Args:
        file_name (str | Path): Имя файла для чтения.

    Returns:
        bytes | None: Бинарные данные файла, если файл существует, или `None`, если файл не найден или произошла ошибка.

    Example:
        >>> get_file_data("saved_image.png")
        b'\x89PNG\r\n...'
    """
    file_path = Path(file_name)

    if not file_path.exists():
        logger.error(f"Файл {file_path} не существует.")
        return

    try:
        with open(file_path, "rb") as file:
            return file.read()
    except Exception as ex:
        logger.error(f"Ошибка при чтении файла {file_path=}", ex, exc_info=True)
        return
