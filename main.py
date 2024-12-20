import argparse
from huffman import HuffmanEncoder


def main():
    parser = argparse.ArgumentParser("Huffman Encoder")
    parser.add_argument("filename",type=str,nargs=2)
    args = parser.parse_args()

    try:
        input_file = open(args.filename[0], 'r', encoding='utf-8')
        try:
            encode_text = input_file.read()
            huffman = HuffmanEncoder(encode_text)
            encoded_text = huffman.encode()
            try:
                output_file = open(args.filename[1],'w',encoding="utf-8")
                output_file.write(str(encoded_text))
            except:
                print("Can't open output file")



        except:
            print("Unexpected error occur during encoding")
    except:
        print("can't open input file")
    


if __name__ == '__main__':
    main()