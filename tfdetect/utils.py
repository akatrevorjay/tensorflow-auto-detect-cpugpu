import sys


class _PyInfo(object):
    PY2 = sys.version_info[0] == 2
    PY3 = sys.version_info[0] == 3

    if PY3:
        string_types = str,
        text_type = str
        binary_type = bytes
    else:  # PY2
        string_types = basestring,
        text_type = unicode
        binary_type = str


def ensure_encoded_bytes(s, encoding='utf-8', errors='strict', allowed_types=(bytes, bytearray, memoryview)):
    """
    Ensure string is encoded as byteslike; convert using specified parameters if we have to.

    :param str|bytes|bytesarray|memoryview s: string/byteslike
    :param str encoding: Decode using this encoding
    :param str errors: How to handle errors
    :return bytes|bytesarray|memoryview: Encoded string as str
    """
    if isinstance(s, allowed_types):
        return s
    else:
        return s.encode(encoding=encoding, errors=errors)


def ensure_decoded_text(s, encoding='utf-8', errors='strict', allowed_types=(_PyInfo.text_type,)):
    """
    Ensure string is decoded (eg unicode); convert using specified parameters if we have to.

    :param str|bytes|bytesarray|memoryview s: string/bytes
    :param str encoding: Decode using this encoding
    :param str errors: How to handle errors
    :return bytes|bytesarray|memoryview: Decoded string as bytes

    :return: Encoded string
    :rtype: bytes
    """
    if not isinstance(s, allowed_types):
        return s.decode(encoding=encoding, errors=errors)
    else:
        return s
