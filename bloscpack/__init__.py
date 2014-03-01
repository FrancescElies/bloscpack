#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim :set ft=py:

""" Command line interface to Blosc via python-blosc """

from .version import __version__  # pragma: no cover

from api import (pack_file,
                 unpack_file,
                 pack_ndarray_file,
                 unpack_ndarray_file,
                 pack_ndarray_str,
                 unpack_ndarray_str,
                 )
