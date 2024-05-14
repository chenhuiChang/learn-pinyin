import unittest

from app import split_input


class TestConvertToPinyin(unittest.TestCase):

    def test_single_english_letter(self):
        self.assertEqual(["a"], split_input("a"))

    def test_single_chinese_character(self):
        self.assertEqual(["中"], split_input("中"))

    def test_mixed_english_and_chinese_characters(self):
        self.assertEqual(["Hello", "世", "界"], split_input("Hello世界"))

    def test_chinese_characters_with_english_in_between(self):
        self.assertEqual(["你", "Hello", "好"], split_input("你Hello好"))

    def test_multiple_english_words_with_chinese_characters(self):
        self.assertEqual(["Hello", "世", "界", "你", "好", "Python"], split_input("Hello 世界你好 Python"))

    def test_no_chinese_characters(self):
        self.assertEqual(["Hello", "World"], split_input("Hello World"))

    def test_no_english_characters(self):
        self.assertEqual(["你", "好", "世", "界"], split_input("你好世界"))

    def test_empty_string(self):
        self.assertEqual([], split_input(""))

    def test_punctuation_and_spaces(self):
        self.assertEqual(["Hello", "世", "界", "你", "好"], split_input("Hello 世界 你好."))

    def test_number_and_spaces(self):
        self.assertEqual(["Hello", "世", "界", "1", "你", "好"], split_input("Hello 世界1你好."))


if __name__ == '__main__':
    unittest.main()
