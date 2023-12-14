from enum import Enum


class Messages(Enum):
    OK = 0
    SECRET_TO_LONG = "Secret text to long"
    NO_BITMAP_FORMAT = "File doesn't have bitmap format"
    COMPRESSION_NOT_ZERO = "Compression not zero"
    COLOR_TABLE_NOT_ZERO = "Color table not zero"
    COLOR_DEPTH_INVALID = "Color depth invalid"
    FILE_PATH_NOT_VALID = "Filepath not valid"
