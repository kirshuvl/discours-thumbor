#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import ImageDraw
from thumbor.filters import BaseFilter, filter_method
from .filter import DiscoursFilter


class Filter(BaseFilter, DiscoursFilter):
    @filter_method(
        BaseFilter.String,
        BaseFilter.String,
        BaseFilter.String,
    )
    async def discourstext(self, text, category, author):
        self.image = self.engine.image.convert('RGBA')

        self.draw = ImageDraw.Draw(self.image)
        self.crop_image()
        self.filter_image()
        self.add_text(text, category, author)
        self.add_logo()

        self.engine.image = self.image
