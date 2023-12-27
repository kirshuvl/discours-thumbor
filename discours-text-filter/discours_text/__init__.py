#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

__version__ = '0.0.1'

try:
    from discours_text.discourstext import Filter  # NOQA
except ImportError:
    logging.exception('Could not import discourstext. Probably due to setup.py installing it.')