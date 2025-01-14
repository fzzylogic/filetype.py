# -*- coding: utf-8 -*-

from __future__ import absolute_import

from . import match
from .types import TYPES


def is_extension_supported(ext):
    """
    Checks if the given extension string is
    one of the supported by the file matchers.

    Args:
        ext (str): file extension string. E.g: jpg, png, mp4, mp3

    Returns:
        True if the file extension is supported.
        Otherwise False.
    """
    for kind in TYPES:
        if kind.extension is ext:
            return True
    return False


def is_mime_supported(mime):
    """
    Checks if the given MIME type string is
    one of the supported by the file matchers.

    Args:
        mime (str): MIME string. E.g: image/jpeg, video/mpeg

    Returns:
        True if the MIME type is supported.
        Otherwise False.
    """
    for kind in TYPES:
        if kind.mime is mime:
            return True
    return False


def is_image(obj):
    """
    Checks if a given input is a supported type image.

    Args:
        obj: path to file, bytes or bytearray.

    Returns:
        True if obj is a valid image. Otherwise False.

    Raises:
        TypeError: if obj is not a supported type.
    """
    return match.image(obj) is not None


def is_archive(obj):
    """
    Checks if a given input is a supported type archive.

    Args:
        obj: path to file, bytes or bytearray.

    Returns:
        True if obj is a valid archive. Otherwise False.

    Raises:
        TypeError: if obj is not a supported type.
    """
    return match.archive(obj) is not None


def is_audio(obj):
    """
    Checks if a given input is a supported type audio.

    Args:
        obj: path to file, bytes or bytearray.

    Returns:
        True if obj is a valid audio. Otherwise False.

    Raises:
        TypeError: if obj is not a supported type.
    """
    return match.audio(obj) is not None


def is_video(obj):
    """
    Checks if a given input is a supported type video.

    Args:
        obj: path to file, bytes or bytearray.

    Returns:
        True if obj is a valid video. Otherwise False.

    Raises:
        TypeError: if obj is not a supported type.
    """
    return match.video(obj) is not None


def is_font(obj):
    """
    Checks if a given input is a supported type font.

    Args:
        obj: path to file, bytes or bytearray.

    Returns:
        True if obj is a valid font. Otherwise False.

    Raises:
        TypeError: if obj is not a supported type.
    """
    return match.font(obj) is not None


def is_application(obj):
    """
    Checks if a given input is a supported type application.

    Args:
        obj: path to file, bytes or bytearray.

    Returns:
        True if obj is a valid font. Otherwise False.

    Raises:
        TypeError: if obj is not a supported type.
    """
    return match.application(obj) is not None


def is_document(obj):
    """
    Checks if a given input is a supported type document.

    Args:
        obj: path to file, bytes or bytearray.

    Returns:
        True if obj is a valid font. Otherwise False.

    Raises:
        TypeError: if obj is not a supported type.
    """
    return match.document(obj) is not None
