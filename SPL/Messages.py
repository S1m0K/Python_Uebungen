from enum import Enum


class Messages(Enum):
    OK = 0
    SECRET_TO_LONG = 1
    NO_BITMAP_FORMAT = 2
    COMPRESSION_NOT_ZERO = 3
    COLOR_TABLE_NOT_ZERO = 4
    COLOR_DEPTH_INVALID = 5
