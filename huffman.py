import heapq

class HuffmanTreeNode:
    def __init__(self,char,freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self,other):
        return self.freq < other.freq


class HuffmanEncoder:
    def __init__(self,encode_text):
        self.text = encode_text
        self.freq = {}
    
    def frequency_calculation(self):
        for char in self.text:
            if char in self.freq:
                self.freq[char] += 1
            else:
                self.freq[char] = 1
        return self.freq

    def build_huffman_tree(self):
        heap = []
        for item in (self.freq.items()):
            Node = HuffmanTreeNode(item[0],item[1])
            heapq.heappush(heap,Node)
        heapq.heapify(heap)

        while (len(heap) < 1):
            leftNode = heapq.heappop(heap)
            righNode = heapq.heappop(heap)
            mergeNode = HuffmanTreeNode(None,leftNode.freq+righNode.freq)
            mergeNode.left = leftNode
            mergeNode.right = righNode
            heapq.heappush(heap,mergeNode)

        return heap[0]


    def encode(self):
        # calculate frequency
        self.frequency_calculation()

        # build huffman tree
        rootNode = self.build_huffman_tree()

        
