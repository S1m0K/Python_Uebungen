import unittest

from Messages import Messages
from SteganoMethods import SteganoMethods


class Tests(unittest.TestCase):
    def test_convert_decimal_byte_arr_to_int(self):
        decimal_byte_arr1 = [1, 1, 1, 1]
        value1 = SteganoMethods.convert_decimal_byte_arr_to_int(decimal_byte_arr1, "little")
        self.assertEqual(16843009, value1)

        decimal_byte_arr2 = [1, 0, 0, 0]
        value2 = SteganoMethods.convert_decimal_byte_arr_to_int(decimal_byte_arr2, "little")
        self.assertEqual(1, value2)

        decimal_byte_arr3 = [255, 0, 0, 0]
        value3 = SteganoMethods.convert_decimal_byte_arr_to_int(decimal_byte_arr3, "little")
        self.assertEqual(255, value3)

        decimal_byte_arr4 = [1, 255, 255, 0]
        value4 = SteganoMethods.convert_decimal_byte_arr_to_int(decimal_byte_arr4, "little")
        self.assertEqual(16776961, value4)

    def test_convert_decimal_byte_arr_to_string(self):
        decimal_byte_arr1 = [66, 77]
        value1 = SteganoMethods.convert_decimal_byte_arr_to_string(decimal_byte_arr1)
        self.assertEqual("BM", value1)

        decimal_byte_arr2 = [76, 117, 100, 119, 105, 103]
        value2 = SteganoMethods.convert_decimal_byte_arr_to_string(decimal_byte_arr2)
        self.assertEqual("Ludwig", value2)

    def test_get_important_values(self):
        decimal_byte_arr = [65, 77, 90, 0, 0, 0, 0, 0, 0, 0, 25, 0, 0, 0, 40, 0, 0, 0, 7, 0, 0, 0, 3, 0, 0, 0, 1, 0, 24,
                            0, 0, 0, 0, 0, 36, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 249, 254,
                            175, 116, 144, 138, 124, 146, 0, 0, 0, 14, 201, 255, 127, 127, 127, 76, 177, 34, 0, 0, 0,
                            56, 53, 196, 110, 174, 55, 191, 185, 203, 0, 0, 0]
        values = SteganoMethods.get_important_values(decimal_byte_arr)

        self.assertEqual({"first_bits": "AM", "off_bits": 25, "width": 7, "height": 3,
                          "color_depth": 24, "compression": 0, "color_table": 0, "row_length": 24}, values)

    def test_convert_char_arr_to_bit_seq(self):
        decimal_char_arr = [76, 117, 100, 119, 105, 103]
        eight_bit_arr = SteganoMethods.convert_decimal_char_arr_to_eight_bit_seq(decimal_char_arr)
        self.assertEqual(["01001100", "01110101", "01100100", "01110111", "01101001", "01100111"], eight_bit_arr)

    def test_convert_char_arr_to_decimal_char_arr(self):
        char_arr = ['L', 'u', 'd', 'w', 'i', 'g']
        decimal_byte_arr = SteganoMethods.convert_char_arr_to_decimal_char_arr(char_arr)
        self.assertEqual([76, 117, 100, 119, 105, 103], decimal_byte_arr)

    def test_put_eight_bit_arr_in_bit_map_content_arr(self):
        decimal_byte_arr = [255, 249, 254, 175, 116, 144, 138, 124, 146, 0, 0, 0, 14, 201, 255, 127, 127, 127, 76, 176,
                            34, 0, 0, 0, 56, 53, 196, 110, 174, 55, 191, 185, 203, 0, 0, 0]
        eight_bit_arr = ["01000001", "11111111"]
        extended_decimal_byte_arr = SteganoMethods.put_eight_bit_arr_in_bit_map_content_arr(decimal_byte_arr,
                                                                                            eight_bit_arr, 12, 3)
        extended_decimal_byte_arr_expected = [254, 249, 254, 174, 116, 144, 138, 125, 147, 0, 0, 0, 15, 201, 255, 127,
                                              127, 127, 77, 176, 34, 0, 0, 0, 56, 53, 196, 110, 174, 55, 191, 185, 203,
                                              0, 0, 0]
        self.assertEqual(extended_decimal_byte_arr_expected, extended_decimal_byte_arr)

    def test_put_zero_byte_in_bit_map_content_arr(self):
        extended_decimal_byte_arr = [254, 249, 254, 174, 116, 144, 138, 125, 146, 0, 0, 0, 14, 201, 255, 127,
                                     127, 127, 76, 177, 34, 0, 0, 0, 56, 53, 196, 110, 174, 55, 191, 185, 203,
                                     0, 0, 0]

        decimal_byte_arr_containing_zero_byte = SteganoMethods.put_zero_byte_in_bit_map_content_arr(
            extended_decimal_byte_arr, 8, 12, 3)

        extended_decimal_byte_arr_expected = [254, 249, 254, 174, 116, 144, 138, 125, 146, 0, 0, 0, 14, 200, 254, 126,
                                              126, 126, 76, 177, 34, 0, 0, 0, 56, 53, 196, 110, 174, 55, 191, 185, 203,
                                              0, 0, 0]
        self.assertEqual(extended_decimal_byte_arr_expected, decimal_byte_arr_containing_zero_byte)

    def test_resolve_row_length(self):
        width = 6
        row_length = SteganoMethods.resolve_row_length(width)
        self.assertEqual(20, row_length)

    def test_read_eight_bit_arr_from_bit_map_content_arr(self):
        decimal_byte_arr = [1, 254, 249, 254, 174, 116, 144, 138, 125, 146, 0, 0, 0, 14, 201, 255, 127,
                            127, 127, 76, 177, 34, 0, 0, 0, 56, 53, 196, 110, 174, 55, 190, 184, 202,
                            0, 0, 0]

        eight_bit_arr = SteganoMethods.read_eight_bit_arr_from_bit_map_content_arr(decimal_byte_arr, 3, 1, 12)
        self.assertEqual(["01000001", "00111110", "10010001", "000"], eight_bit_arr)

    def test_read_eight_bit_arr_from_bit_map_content_arr_with_stop_byte(self):
        decimal_byte_arr = [1, 254, 249, 254, 174, 116, 144, 138, 125, 146, 0, 0, 0, 14, 200, 254, 126,
                            126, 126, 76, 177, 34, 0, 0, 0, 56, 53, 196, 110, 174, 55, 190, 184, 202,
                            0, 0, 0]

        eight_bit_arr = SteganoMethods.read_eight_bit_arr_from_bit_map_content_arr(decimal_byte_arr, 3, 1, 12)
        self.assertEqual(["01000001", "00000000"], eight_bit_arr)

    def test_update_index(self):
        index = 7
        width = 3
        modul = width * 3
        updated_index, updated_modul = SteganoMethods.update_index_and_modul(index, modul, width, 12)
        self.assertEqual(8, updated_index)
        self.assertEqual(9, updated_modul)

        index = 8
        width = 3
        modul = width * 3
        updated_index, updated_modul = SteganoMethods.update_index_and_modul(index, modul, width, 12)
        self.assertEqual(12, updated_index)
        self.assertEqual(21, updated_modul)

        index = 14
        width = 5
        modul = width * 3
        updated_index, updated_modul = SteganoMethods.update_index_and_modul(index, modul, width, 16)
        self.assertEqual(16, updated_index)
        self.assertEqual(15 + 16, updated_modul)

        index = 0
        width = 5
        modul = width * 3
        updated_index, updated_modul = SteganoMethods.update_index_and_modul(index, modul, width, 16, False)
        self.assertEqual(0, updated_index)
        self.assertEqual(modul, updated_modul)

    def test_remove_zero_byte_from_bit_map_arr(self):
        eight_bit_arr = ["01000001", "00111110", "01110001", "000"]

        updated_eight_bit_arr = SteganoMethods.remove_zero_byte_from_bit_map_arr(eight_bit_arr)
        self.assertEqual(["01000001", "00111110", "01110001"], updated_eight_bit_arr)

    def test_convert_eight_bit_arr_to_decimal_byte_arr(self):
        eight_bit_arr = ["01011011", "00111110", "01110001"]

        decimal_byte_arr = SteganoMethods.convert_eight_bit_arr_to_decimal_byte_arr(eight_bit_arr)
        self.assertEqual([91, 62, 113], decimal_byte_arr)

    def test_convert_decimal_byte_arr_to_char_arr(self):
        decimal_byte_arr = [65, 80, 113]
        char_arr = SteganoMethods.convert_decimal_byte_arr_to_char_arr(decimal_byte_arr)
        self.assertEqual(['A', 'P', 'q'], char_arr)

    def test_check_for_necessary_conventions(self):
        important_values_dic = {"first_bits": "AM", "off_bits": 25, "width": 7, "height": 3,
                                "color_depth": 24, "compression": 0, "color_table": 1, "row_length": 24}
        char_arr = ['L', 'u', 'd', 'w', 'i', 'g']
        message = SteganoMethods.check_for_necessary_conventions(important_values_dic, char_arr)
        self.assertTrue(Messages.COLOR_TABLE_NOT_ZERO, message)

        important_values_dic = {"first_bits": "AM", "off_bits": 25, "width": 7, "height": 3,
                                "color_depth": 20, "compression": 0, "color_table": 0, "row_length": 24}
        char_arr = ['L', 'u', 'd', 'w', 'i', 'g']
        message = SteganoMethods.check_for_necessary_conventions(important_values_dic, char_arr)
        self.assertTrue(Messages.COLOR_DEPTH_INVALID, message)

        important_values_dic = {"first_bits": "AM", "off_bits": 25, "width": 7, "height": 3,
                                "color_depth": 24, "compression": 0, "color_table": 0, "row_length": 24}
        char_arr = ['L', 'u', 'd', 'w', 'i', 'g']
        message = SteganoMethods.check_for_necessary_conventions(important_values_dic, char_arr)
        self.assertTrue(Messages.OK, message)

        important_values_dic = {"first_bits": "CX", "off_bits": 25, "width": 7, "height": 3,
                                "color_depth": 24, "compression": 0, "color_table": 0, "row_length": 24}
        char_arr = ['L', 'u', 'd', 'w', 'i', 'g']
        message = SteganoMethods.check_for_necessary_conventions(important_values_dic, char_arr)
        self.assertTrue(Messages.NO_BITMAP_FORMAT, message)

        important_values_dic = {"first_bits": "AM", "off_bits": 25, "width": 2, "height": 2,
                                "color_depth": 24, "compression": 0, "color_table": 0, "row_length": 24}
        char_arr = ['L', 'u', 'd', 'w', 'i', 'g', 'L', 'u', 'd', 'w', 'i', 'g']
        message = SteganoMethods.check_for_necessary_conventions(important_values_dic, char_arr)
        self.assertTrue(Messages.SECRET_TO_LONG, message)

    def test_assemble_char_arr(self):
        char_arr = ['L', 'u', 'd', 'w', 'i', 'g']
        output = SteganoMethods.assemble_char_arr(char_arr)
        self.assertEqual("Ludwig", output)


if __name__ == '__main__':
    unittest.main()
