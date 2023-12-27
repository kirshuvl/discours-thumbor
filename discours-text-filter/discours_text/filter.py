import os
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter, ImageFont
import textwrap


final_width = int(os.getenv('FINAL_WIDTH', 1200))
final_height = int(os.getenv('FINAL_HEIGHT', 630))
brightness_ratio = float(os.getenv('BRIGHTNESS_RATIO', 0.65))

    
logo_width = int(os.getenv('LOGO_WIDTH', 80))
logo_height = int(os.getenv('LOGO_HEIGHT', 80))
logo_left = int(os.getenv('LOGO_LEFT', 40))
logo_top = int(os.getenv('LOGO_TOP', 35))

author_left = int(os.getenv('AUTHOR_LEFT', 57))
author_top = int(os.getenv('AUTHOR_TOP', 198))
author_font_size = int(os.getenv('AUTHOR_FONT_SIZE', 34))
author_font_name = os.getenv('AUTHOR_FONT_NAME', "Muller-Regular.otf")

category_left = int(os.getenv('CATEGORY_LEFT', 116))
category_top = int(os.getenv('CATEGORY_TOP', 53))
category_font_size = int(os.getenv('CATEGORY_FONT_SIZE', 30))
category_font_name = os.getenv('CATEGORY_FONT_NAME', "Muller-Bold.otf")

title_top = int(os.getenv('TITLE_TOP', 265))
title_left = int(os.getenv('TITLE_LEFT', 57))
title_right = int(os.getenv('TITLE_RIGHT', 100))
title_leading = int(os.getenv('TITLE_LEADING', 60))

title_font_size = int(os.getenv('TITLE_FONT_SIZE', 56))
title_font_name = os.getenv('TITLE_FONT_NAME', "Muller-Bold.otf")
title_text_width = int(os.getenv('TITLE_TEXT_WIDTH', 34))
title_margin = int(os.getenv('TITLE_MARGIN', 90))


class ImageError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class DiscoursFilter():
    def test(self, category, author, title):
        self.image = Image.open('test.webp').convert('RGBA')
        self.draw = ImageDraw.Draw(self.image)
        self.crop_image()
        self.filter_image()
        self.add_text(category, author, title)
        self.add_logo()

    def crop_image(self):
        width, height = self.image.size
        if width < final_width:
            raise ImageError('Image is too small')

        real_height = height * final_width / width

        if real_height < final_height:
            raise ImageError('Image is too small')

        final_size = (final_width, final_height)
        self.image = self.image.resize(final_size, Image.Resampling.LANCZOS)

    def filter_image(self):
        self.image = ImageEnhance.Brightness(self.image)
        self.image = self.image.enhance(brightness_ratio)

    def add_text(self, category, author, title):
        category_font = ImageFont.truetype(
            category_font_name, category_font_size)
        self._draw_text(category.lower(), category_left,
                        category_top, category_font)

        author_font = ImageFont.truetype(author_font_name, author_font_size)
        self._draw_text(author, author_left, author_top, author_font)

        lines = textwrap.wrap(title, width=title_text_width)
        i = 1
        while len(lines) > 3:
            lines = textwrap.wrap(title, width=title_text_width + i)
            i += 1

        _title_font_size = title_font_size

        title_font = ImageFont.truetype(title_font_name, _title_font_size)
        for line in lines:
            while title_font.getbbox(line)[2] - title_font.getbbox(line)[0] > final_width - title_right - title_left:

                _title_font_size -= 1
                title_font = ImageFont.truetype(
                    title_font_name, _title_font_size)

        y_title = title_top
        for line in lines:
            self._draw_text(line, title_left, y_title, title_font)
            y_title += title_leading

    def _draw_text(self,  text, left, top, font: ImageFont.FreeTypeFont):
        font_box = font.getbbox(text)
        # TODO: понять, почему вторая формула 3 + 1
        text_image_size = font_box[2] - font_box[0] + \
            10, font_box[3] + font_box[1] + 10

        text_image = Image.new("RGBA", text_image_size, color=0)

        text_draw = ImageDraw.Draw(text_image)
        text_draw.text((0, 5), text, font=font,)

        shadow_image = self._text_shadow(text, font, text_image_size)

        box = (left, top, left + text_image_size[0], top + text_image_size[1])
        im = self.image.crop(box)
        im = Image.alpha_composite(im, shadow_image)
        im = Image.alpha_composite(im, text_image)
        self.image.paste(im, (left, top))

    def _text_shadow(self, text, font, size):
        image = Image.new("RGBA", size, color=(0, 0, 0, 0))
        draw = ImageDraw.Draw(image, "RGBA")

        draw.text((1, 4), text, font=font, fill=(0, 0, 0, 250))
        # draw.text((2, 3), text, font=font, fill=(0,0,0,230))
        # draw.text((3, 2), text, font=font, fill=(0,0,0,200))

        image = image.filter(ImageFilter.BLUR)

        return image

    def add_logo(self):
        self.image_logo = Image.open('logo.png').convert('RGBA')
        size = logo_width, logo_height
        self.image_logo.thumbnail(size, Image.Resampling.LANCZOS)
        box = (logo_left, logo_top, logo_left +
               self.image_logo.size[0], logo_top + self.image_logo.size[1])
        image_box = self.image.crop(box)
        image_box = Image.alpha_composite(image_box, self.image_logo)
        self.image.paste(image_box, (logo_left, logo_top))

    def save_image(self, file_name):
        self.image.save(file_name)


if __name__ == "__main__":
    my_filter = DiscoursFilter()
    my_filter.test('Общество',
                   'Иван Иванов',
                   '«Мой ребенок сидит за несовершенное преступление». Мама канского подростка Никиты Уварова о приговоре и принципах сына ')
    my_filter.save_image('output.webp')
