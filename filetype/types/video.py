# -*- coding: utf-8 -*-

from __future__ import absolute_import

from .base import Type
from .isobmff import IsoBmff


class M4v(Type):
    """
    Implements the M4V video type matcher.
    """
    MIME = 'video/x-m4v'
    EXTENSION = 'm4v'

    def __init__(self):
        super(M4v, self).__init__(
            mime=M4v.MIME,
            extension=M4v.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 10 and
                buf[0] == 0x0 and buf[1] == 0x0 and
                buf[2] == 0x0 and buf[3] == 0x1C and
                buf[4] == 0x66 and buf[5] == 0x74 and
                buf[6] == 0x79 and buf[7] == 0x70 and
                buf[8] == 0x4D and buf[9] == 0x34 and
                buf[10] == 0x56)


class Mkv(Type):
    """
    Implements the MKV video type matcher.
    """
    MIME = 'video/x-matroska'
    EXTENSION = 'mkv'

    def __init__(self):
        super(Mkv, self).__init__(
            mime=Mkv.MIME,
            extension=Mkv.EXTENSION
        )

    def match(self, buf):
        # todo: GO source checks first 4 bytes, then searches next 4096 for 'matroska',
        # and finally checks if bytes 5 & 6 below are located prior to 'matroska'.
        return ((len(buf) > 15 and
                buf[0] == 0x1A and buf[1] == 0x45 and
                buf[2] == 0xDF and buf[3] == 0xA3 and
                buf[4] == 0x93 and buf[5] == 0x42 and
                buf[6] == 0x82 and buf[7] == 0x88 and
                buf[8] == 0x6D and buf[9] == 0x61 and
                buf[10] == 0x74 and buf[11] == 0x72 and
                buf[12] == 0x6F and buf[13] == 0x73 and
                buf[14] == 0x6B and buf[15] == 0x61) or
                (len(buf) > 38 and
                    buf[31] == 0x6D and buf[32] == 0x61 and
                    buf[33] == 0x74 and buf[34] == 0x72 and
                    buf[35] == 0x6f and buf[36] == 0x73 and
                    buf[37] == 0x6B and buf[38] == 0x61))


class Webm(Type):
    """
    Implements the WebM video type matcher.
    """
    MIME = 'video/webm'
    EXTENSION = 'webm'

    def __init__(self):
        super(Webm, self).__init__(
            mime=Webm.MIME,
            extension=Webm.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 3 and
                buf[0] == 0x1A and
                buf[1] == 0x45 and
                buf[2] == 0xDF and
                buf[3] == 0xA3)


class Mov(IsoBmff):
    """
    Implements the MOV video type matcher.
    """
    MIME = 'video/quicktime'
    EXTENSION = 'mov'

    def __init__(self):
        super(Mov, self).__init__(
            mime=Mov.MIME,
            extension=Mov.EXTENSION
        )

    def match(self, buf):
        if not self._is_isobmff(buf):
            return False

        major_brand, minor_version, compatible_brands = self._get_ftyp(buf)
        return major_brand == 'qt  '


class Avi(Type):
    """
    Implements the AVI video type matcher.
    """
    MIME = 'video/x-msvideo'
    EXTENSION = 'avi'

    def __init__(self):
        super(Avi, self).__init__(
            mime=Avi.MIME,
            extension=Avi.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 10 and
                buf[0] == 0x52 and
                buf[1] == 0x49 and
                buf[2] == 0x46 and
                buf[3] == 0x46 and
                buf[8] == 0x41 and
                buf[9] == 0x56 and
                buf[10] == 0x49)


class Wmv(Type):
    """
    Implements the WMV video type matcher.
    """
    MIME = 'video/x-ms-wmv'
    EXTENSION = 'wmv'

    def __init__(self):
        super(Wmv, self).__init__(
            mime=Wmv.MIME,
            extension=Wmv.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 9 and
                buf[0] == 0x30 and
                buf[1] == 0x26 and
                buf[2] == 0xB2 and
                buf[3] == 0x75 and
                buf[4] == 0x8E and
                buf[5] == 0x66 and
                buf[6] == 0xCF and
                buf[7] == 0x11 and
                buf[8] == 0xA6 and
                buf[9] == 0xD9)


class Mpeg(Type):
    """
    Implements the MPEG video type matcher.
    """
    MIME = 'video/mpeg'
    EXTENSION = 'mpg'

    def __init__(self):
        super(Mpeg, self).__init__(
            mime=Mpeg.MIME,
            extension=Mpeg.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 3 and
                buf[0] == 0x0 and
                buf[1] == 0x0 and
                buf[2] == 0x1 and
                buf[3] >= 0xb0 and
                buf[3] <= 0xbf)


class Flv(Type):
    """
    Implements the FLV video type matcher.
    """
    MIME = 'video/x-flv'
    EXTENSION = 'flv'

    def __init__(self):
        super(Flv, self).__init__(
            mime=Flv.MIME,
            extension=Flv.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 3 and
                buf[0] == 0x46 and
                buf[1] == 0x4C and
                buf[2] == 0x56 and
                buf[3] == 0x01)


class Mp4(IsoBmff):
    """
    Implements the MP4 video type matcher.
    """
    MIME = 'video/mp4'
    EXTENSION = 'mp4'

    def __init__(self):
        super(Mp4, self).__init__(
            mime=Mp4.MIME,
            extension=Mp4.EXTENSION
        )

    def match(self, buf):
        if not self._is_isobmff(buf):
            return False

        major_brand, minor_version, compatible_brands = self._get_ftyp(buf)
        return major_brand in ['mp41', 'mp42']


class Match3gp(Type):
    """
    Implements the 3GB video type matcher.
    """
    MIME = 'video/3gpp'
    EXTENSION = '3gp'

    def __init__(self):
        super(Match3gp, self).__init__(
            mime=Match3gp.MIME,
            extension=Match3gp.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 10 and
                buf[4] == 0x66 and
                buf[5] == 0x74 and
                buf[6] == 0x79 and
                buf[7] == 0x70 and
                buf[8] == 0x33 and
                buf[9] == 0x67 and
                buf[10] == 0x70)
