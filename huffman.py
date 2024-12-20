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

        while (len(heap) > 1):
            leftNode = heapq.heappop(heap)
            righNode = heapq.heappop(heap)
            mergeNode = HuffmanTreeNode(None,leftNode.freq+righNode.freq)
            mergeNode.left = leftNode
            mergeNode.right = righNode
            heapq.heappush(heap,mergeNode)

        return heap[0]

    def _dfs(self,node,codes,current_code):
        if (node == None):
            return
        
        if (node.char != None):
            codes[node.char] = current_code
            return

        # print(node.char,node.freq)
        self._dfs(node.left,codes,current_code + "0")
        self._dfs(node.right,codes,current_code + "1")


    def build_huffman_code(self,rootNode):
        codes = {}
        current_code = ""
        self._dfs(rootNode,codes,current_code)
        return codes


    def encode(self):
        # calculate frequency
        self.frequency_calculation()

        # build huffman tree
        rootNode = self.build_huffman_tree()

        #prefix-code table
        codes = self.build_huffman_code(rootNode)

        encoded_text = str(self.freq) + '\n'
        for char in self.text:
            encoded_text += str(codes[char])

        return encoded_text
        
