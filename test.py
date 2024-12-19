import unittest
from collections import Counter
from huffman import HuffmanEncoder

def trueFreq(encode_text):
    return Counter(encode_text)

class TestFrequencyCalculation(unittest.TestCase):

    def setUp(self):
        self.test_file = "challenge-huffman/test.txt"
        with open(self.test_file,'r',encoding='utf-8') as f:
            self.encode_text = f.read()
        return super().setUp()
    
    def test_frequency_calculation_from_file(self):
        custom_frequency = HuffmanEncoder(self.encode_text).encode()
        counter_frequency = dict(Counter(self.encode_text))
        
        # Compare the two
        self.assertEqual(custom_frequency, counter_frequency)

        
if __name__ == "__main__":
    unittest.main()