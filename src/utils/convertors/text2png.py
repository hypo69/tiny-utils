
## \file ../src/utils/convertor/text2png.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
"""Takes a text file and uses Pillow to generate PNGs of those lines of text
from https://github.com/mawillcockson/text2png/blob/master/text2png.py
скрипт читает текст из файла, генерирует изображения PNG для каждой строки текста и сохраняет их в каталоге вывода, с возможностью настройки различных аспектов изображений.

** функции**:
   - `assign_path`: Определяет правильный путь для выходных файлов PNG, при необходимости создавая каталог.
   - `center_text_position`: Рассчитывает позицию для центрирования текста на холсте.
   - `generate_png`: Создает изображение PNG с заданным текстом, шрифтом, цветами и т. д.
   - `not_comment_or_blank`: Проверяет, не является ли строка комментарием или пустой.
   - `which_exist`: Проверяет, какие имена файлов уже существуют в каталоге.
   - `get_characters`: Извлекает строки текста из входного файла или списка, фильтруя комментарии и пустые строки.
   - `parse_size`: Разбирает строку в объект `Size`.
   - `get_max_text_size`: Рассчитывает максимальный размер текста на основе шрифта и строк текста.
   - `get_font`: Определяет размер шрифта на основе размера холста и отступа.
   - `setup_logging`: Настраивает модуль логирования на основе указанного уровня журналирования.
   - `error`: Регистрирует сообщение об ошибке и вызывает исключение.

@code

async def main():
    generator = TextToImageGenerator()
    lines = ["Text 1", "Text 2", "Text 3"]
    output_dir = "./output"
    images = await generator.generate_images(lines, output_dir=output_dir)
    print(images)

>>> await main()
------
generator = TextToImageGenerator()
lines = ["Text 1", "Text 2", "Text 3"]
output_dir = "./output"
images = await generator.generate_images(lines, output_dir=output_dir)
print(images)
------
if __name__ == "__main__":
    import asyncio
    asyncio.run(main()
@endcode

"""
import logging
import math
from pathlib import Path
from typing import List, Union, Tuple
from PIL import Image, ImageDraw, ImageFont


class TextToImageGenerator:
    """
    A class for generating PNG images of characters from text.
    """

    def __init__(self):
        """
        Initializes the TextToImageGenerator class.
        """
        self.default_output_dir = Path("./output")
        self.default_canvas_size = (1024, 1024)
        self.default_padding = 0.10
        self.default_background = "white"
        self.default_text_color = "black"
        self.default_log_level = logging.WARNING

    async def generate_images(
        self,
        lines: List[str],
        output_dir: str | Path = None,
        font: str | ImageFont.ImageFont = "sans-serif",
        canvas_size: Tuple[int, int] = None,
        padding: float = None,
        background_color: str = None,
        text_color: str = None,
        log_level: int | str | bool = None,
        clobber: bool = False,
    ) -> List[Path]:
        """
        Generates PNG images of characters.

        @param lines: A list of strings containing the text to generate images from.
        @param output_dir: Directory to output pictures. Defaults to "./output".
        @param font: Font to use for text. Defaults to "sans-serif".
        @param canvas_size: Size in pixels to make all character images. Defaults to 1024x1024.
        @param padding: The percentage of the canvas dimensions to use as a blank border. Defaults to 0.10.
        @param background_color: Color for the background. Defaults to "white".
        @param text_color: Color to use for the text. Defaults to "black".
        @param log_level: Verbosity/log level. Defaults to logging.WARNING.
        @param clobber: If True, overwrites existing files; otherwise, nothing is clobbered. Defaults to False.

        @return: List of paths to the generated images.
        """
        output_directory = Path(output_dir) if output_dir else self.default_output_dir
        self.setup_logging(level=log_level)

        if not canvas_size:
            canvas_size = self.default_canvas_size

        if not padding:
            padding = self.default_padding

        if not background_color:
            background_color = self.default_background

        if not text_color:
            text_color = self.default_text_color

        images = []
        for text in lines:
            image = self.generate_png(
                text=text,
                font=font,
                canvas_size=canvas_size,
                padding=padding,
                background_color=background_color,
                text_color=text_color,
            )
            image_path = self.assign_path(text=text, output_dir=output_directory)
            image.save(fp=image_path, format="PNG")
            images.append(image_path)

        return images

    def setup_logging(self, level: int | str | bool = None) -> None:
        """
        Sets up logging configurations.

        @param level: Verbosity/log level. Defaults to logging.WARNING.
        """
        if level is False:
            return None
        elif not level:
            logging.basicConfig(format="%(message)s", level=self.default_log_level)
        else:
            logging.basicConfig(format="%(message)s", level=level)

    def assign_path(self, text: str, output_dir: str | Path) -> Path:
        """
        Assigns a path for the output image.

        @param text: The text for which the path is assigned.
        @param output_dir: Directory to output pictures.

        @return: Path to the output image.
        """
        proper_dir = Path(output_dir)
        if proper_dir.exists() and not proper_dir.is_dir():
            raise FileExistsError(f"'{proper_dir}' is not a directory")
        elif proper_dir.exists():
            proper_path = proper_dir / (text + ".png")
        else:
            proper_dir.mkdir()
            proper_path = proper_dir / (text + ".png")

        try:
            proper_path.touch()
        except OSError as err:
            raise Exception(
                "Filesystem error likely prevented using a particular filename"
            ) from err

        return proper_path.expanduser().resolve()

    def center_text_position(
        self, text_size: Tuple[int, int], canvas_size: Tuple[int, int], padding: float
    ) -> Tuple[int, int]:
        """
        Calculates the position to center the text on the canvas.

        @param text_size: The size of the text.
        @param canvas_size: The size of the canvas.
        @param padding: The percentage of the canvas dimensions to use as a blank border.

        @return: Tuple containing the x and y coordinates of the text position.
        """
        padding_width = padding * canvas_size[0] / 2
        padding_height = padding * canvas_size[1] / 2
        leftover_width = canvas_size[0] - text_size[0] - (padding_width * 2)
        leftover_height = canvas_size[1] - text_size[1] - (padding_height * 2)
        if leftover_height < 0 or leftover_width < 0:
            raise ValueError("Calculation error: text too big for canvas")

        x = math.floor((leftover_width / 2) + padding_width)
        y = math.floor((leftover_height / 2) + padding_height)
        return x, y

    def generate_png(
        self,
        text: str,
        font: str | ImageFont.ImageFont,
        canvas_size: Tuple[int, int],
        padding: float,
        background_color: str,
        text_color: str,
    ) -> Image:
        """
        Generates a PNG image with the given text.

        @param text: The text to generate the image from.
        @param font: Font to use for the text.
        @param canvas_size: Size of the canvas.
        @param padding: The percentage of the canvas dimensions to use as a blank border.
        @param background_color: Color for the background.
        @param text_color: Color to use for the text.

        @return: PIL Image object representing the generated image.
        """
        canvas = Image.new("RGBA", canvas_size, background_color)
        draw = ImageDraw.Draw(canvas)
        if isinstance(font, str):
            font = ImageFont.load_default()
        text_size = draw.textsize(text=text, font=font)
        text_position = self.center_text_position(
            text_size=text_size, canvas_size=canvas_size, padding=padding
        )
        draw.text(
            xy=text_position, text=text, fill=text_color, font=font,
        )
        return canvas




