from builtins import bytearray

from Messages import Messages


class SteganoMethods:
    @staticmethod
    def get_bit_map_bytes_arr(path):
        bitMapBytesArr = []
        try:
            file = open(path, "rb")
            while True:
                chunk = file.read(1)
                if not chunk:
                    break
                bitMapBytesArr.append(int.from_bytes(chunk, byteorder="big"))

            return bitMapBytesArr

        except FileNotFoundError:
            return Messages.FILE_PATH_NOT_VALID

    @staticmethod
    def write_bit_map_bytes_arr(path, bit_map):
        try:
            file = open(path, "wb")
            file.write(bytearray(bit_map))
        except FileNotFoundError:
            return Messages.FILE_PATH_NOT_VALID

    @staticmethod
    def check_for_necessary_conventions(important_values_dic, secret_char_arr=""):
        if secret_char_arr != "":
            if (important_values_dic["width"] * important_values_dic["height"] * 3) < (len(secret_char_arr) * 8):
                return Messages.SECRET_TO_LONG

        if important_values_dic["first_bits"] != "BM":
            return Messages.NO_BITMAP_FORMAT

        if important_values_dic["compression"] != 0:
            return Messages.COMPRESSION_NOT_ZERO

        if important_values_dic["color_table"] != 0:
            return Messages.COLOR_TABLE_NOT_ZERO

        if important_values_dic["color_depth"] != 24:
            return Messages.COLOR_DEPTH_INVALID

        return Messages.OK

    @staticmethod
    def get_important_values(decimal_bit_map_bytes_arr):
        first_bits = SteganoMethods.convert_decimal_byte_arr_to_string(decimal_bit_map_bytes_arr[0:2])
        off_bits = SteganoMethods.convert_decimal_byte_arr_to_int(decimal_bit_map_bytes_arr[10:14], "little")
        width = SteganoMethods.convert_decimal_byte_arr_to_int(decimal_bit_map_bytes_arr[18:22], "little")
        height = SteganoMethods.convert_decimal_byte_arr_to_int(decimal_bit_map_bytes_arr[22:26], "little")
        color_depth = SteganoMethods.convert_decimal_byte_arr_to_int(decimal_bit_map_bytes_arr[28:30], "little")
        compression = SteganoMethods.convert_decimal_byte_arr_to_int(decimal_bit_map_bytes_arr[30:34], "little")
        color_table = SteganoMethods.convert_decimal_byte_arr_to_int(decimal_bit_map_bytes_arr[46:54], "little")
        row_length = SteganoMethods.resolve_row_length(width)
        return {"first_bits": first_bits, "off_bits": off_bits, "width": width, "height": height,
                "color_depth": color_depth, "compression": compression, "color_table": color_table,
                "row_length": row_length}

    @staticmethod
    def convert_decimal_byte_arr_to_int(decimal_byte_arr, byte_order="big"):
        if byte_order == "little":
            decimal_byte_arr.reverse()

        byte_arr = bytearray()
        for dB in decimal_byte_arr:
            byte_arr.extend(dB.to_bytes(1))

        return int.from_bytes(byte_arr, byteorder="big")

    @staticmethod
    def convert_decimal_byte_arr_to_string(decimal_byte_arr):
        seq = ""
        for dB in decimal_byte_arr:
            seq += chr(dB)
        return seq

    @staticmethod
    def plant_secret_in_bit_map_arr(bit_map_bytes_arr, secret_word_char_arr, important_values_dic):
        bit_map_content_bytes_arr = bit_map_bytes_arr[important_values_dic["off_bits"]:]
        decimal_char_arr = SteganoMethods.convert_char_arr_to_decimal_char_arr(secret_word_char_arr)
        eight_bit_arr = SteganoMethods.convert_decimal_char_arr_to_eight_bit_seq(decimal_char_arr)

        extended_bit_map_arr = SteganoMethods.put_eight_bit_arr_in_bit_map_content_arr(bit_map_content_bytes_arr,
                                                                                       eight_bit_arr,
                                                                                       important_values_dic[
                                                                                           "row_length"],
                                                                                       important_values_dic["width"])
        finished_bit_map_arr = SteganoMethods.put_zero_byte_in_bit_map_content_arr(extended_bit_map_arr,
                                                                                   len(secret_word_char_arr) * 8,
                                                                                   important_values_dic["row_length"],
                                                                                   important_values_dic["width"])
        finished_bit_map_arr = bit_map_bytes_arr[:important_values_dic["off_bits"]] + finished_bit_map_arr

        return finished_bit_map_arr

    @staticmethod
    def convert_decimal_char_arr_to_eight_bit_seq(decimal_char_arr):
        eight_bit_arr = []
        for dC in decimal_char_arr:
            eight_bit_arr.append('{0:08b}'.format(dC))
        return eight_bit_arr

    @staticmethod
    def convert_char_arr_to_decimal_char_arr(char_arr):
        decimal_char_arr = []
        for c in char_arr:
            decimal_char_arr.append(ord(c))
        return decimal_char_arr

    @staticmethod
    def put_eight_bit_arr_in_bit_map_content_arr(decimal_bit_map_content_arr, eight_bit_arr, row_length, width):
        index, modul = SteganoMethods.update_index_and_modul(0, width * 3, width, row_length, False)

        for byte in eight_bit_arr:
            for bit_index in range(len(byte)):

                if decimal_bit_map_content_arr[index] % 2 == 0:
                    if byte[bit_index] == '1':
                        decimal_bit_map_content_arr[index] = decimal_bit_map_content_arr[index] + 1
                    # else bit stays the same

                else:
                    if byte[bit_index] == '0':
                        decimal_bit_map_content_arr[index] = decimal_bit_map_content_arr[index] - 1
                    # else bit stays the same
                index, modul = SteganoMethods.update_index_and_modul(index, modul, width, row_length)

        return decimal_bit_map_content_arr

    @staticmethod
    def put_zero_byte_in_bit_map_content_arr(extended_bit_map_content_arr, starterIndex, row_length, width):
        index, modul = SteganoMethods.update_index_and_modul(starterIndex, width * 3, width, row_length, False)

        for i in range(8):
            if index >= len(extended_bit_map_content_arr):
                return extended_bit_map_content_arr

            if extended_bit_map_content_arr[index] % 2 != 0:
                extended_bit_map_content_arr[index] = extended_bit_map_content_arr[index] - 1

            index, modul = SteganoMethods.update_index_and_modul(index, modul, width, row_length)

        return extended_bit_map_content_arr

    @staticmethod
    def resolve_row_length(width):
        row_length = width * 3
        # row length needs to be 3x the width (RGB for every pixel) plus x so that it is modul 4 = 0
        while True:
            if row_length % 4 == 0:
                return row_length
            row_length = row_length + 1

    @staticmethod
    def read_eight_bit_arr_from_bit_map_content_arr(decimal_byte_arr, width, off_bits, row_length):
        decimal_content_byte_arr = decimal_byte_arr[off_bits:]  # cut off header
        index, modul = SteganoMethods.update_index_and_modul(0, width * 3, width, row_length, False)
        eight_bit_arr = [""]
        eight_bit_arr_index = 0

        while True:
            if decimal_content_byte_arr[index] % 2 == 0:
                eight_bit_arr[eight_bit_arr_index] = eight_bit_arr[eight_bit_arr_index] + "0"
            else:
                eight_bit_arr[eight_bit_arr_index] = eight_bit_arr[eight_bit_arr_index] + "1"

            if len(eight_bit_arr[eight_bit_arr_index]) == 8:
                if eight_bit_arr[eight_bit_arr_index] == "00000000":
                    return eight_bit_arr

                eight_bit_arr.append("")
                eight_bit_arr_index = eight_bit_arr_index + 1

            index, modul = SteganoMethods.update_index_and_modul(index, modul, width, row_length)
            if index > (len(decimal_content_byte_arr) - 1):
                return eight_bit_arr

    @staticmethod
    def update_index_and_modul(index, modul, width, row_length, default_higher_index=True):
        if default_higher_index:
            index = index + 1

        if index == 0:
            return index, modul

        bytes_per_row = width * 3
        cnt_skip_bytes = row_length - width * 3

        if index % modul == 0:
            index = index + cnt_skip_bytes
            modul = bytes_per_row + index

        return index, modul

    @staticmethod
    def remove_zero_byte_from_bit_map_arr(eight_bit_arr):
        if '1' not in eight_bit_arr[-1]:
            return eight_bit_arr[:-1]

        return eight_bit_arr[:-1]

    @staticmethod
    def convert_eight_bit_arr_to_decimal_byte_arr(eight_bit_arr):
        decimal_byte_arr = []

        for eight_bit in eight_bit_arr:
            decimal_byte_arr.append(int(eight_bit, 2))

        return decimal_byte_arr

    @staticmethod
    def convert_decimal_byte_arr_to_char_arr(decimal_byte_arr):
        char_arr = []

        for decimal_byte in decimal_byte_arr:
            char_arr.append(chr(decimal_byte))

        return char_arr

    @staticmethod
    def retrieve_secret_from_decimal_byte_arr(bit_map_decimal_bytes_arr, important_values_dic):
        eight_bit_arr = SteganoMethods.read_eight_bit_arr_from_bit_map_content_arr(bit_map_decimal_bytes_arr,
                                                                                   important_values_dic["width"],
                                                                                   important_values_dic["off_bits"],
                                                                                   important_values_dic["row_length"])
        eight_bit_arr = SteganoMethods.remove_zero_byte_from_bit_map_arr(eight_bit_arr)
        decimal_byte_arr = SteganoMethods.convert_eight_bit_arr_to_decimal_byte_arr(eight_bit_arr)
        char_arr = SteganoMethods.convert_decimal_byte_arr_to_char_arr(decimal_byte_arr)
        secret = SteganoMethods.assemble_char_arr(char_arr)
        return secret

    @staticmethod
    def assemble_char_arr(char_arr):
        string = ""
        for char in char_arr:
            string = string + char
        return string
