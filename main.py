import argparse
from huffman import HuffmanEncoder


def main():
    parser = argparse.ArgumentParser("Huffman Encoder")
    parser.add_argument("filename",type=str,nargs=1)
    args = parser.parse_args()

    try:
        file_handle = open(args.filename[0], 'r', encoding='utf-8')
        try:
            encode_text = file_handle.read()
            huffman = HuffmanEncoder(encode_text)
            huffman.encode()

        except:
            print("Can't read from file")
    except:
        print("can't open file")
    


if __name__ == '__main__':
    main()