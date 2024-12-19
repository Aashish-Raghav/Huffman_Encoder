class HuffmanEncoder:
    def __init__(self,encode_text):
        self.text = encode_text
        self.freq = {}
    
    def encode(self):
        for char in self.text:
            if char in self.freq:
                self.freq[char] += 1
            else:
                self.freq[char] = 1
        return self.freq

