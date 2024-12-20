import argparse
from huffman import HuffmanEncoder


def main():
    parser = argparse.ArgumentParser("Huffman Encoder")
    parser.add_argument("filename",type=str,nargs=3)
    args = parser.parse_args()

    try:
        input_file = open(args.filename[0], 'r', encoding='utf-8')
        try:
            encode_text = input_file.read()
            huffman = HuffmanEncoder(encode_text)
            encoded_text = huffman.encode()
            try:
                # write encoded data to output file
                output_file_encoded = open(args.filename[1],'w+',encoding="utf-8")
                output_file_encoded.write(str(encoded_text))

                # Move the file pointer back to the beginning
                output_file_encoded.seek(0)

                # read from encoded data from output file 
                encoded_text = output_file_encoded.read()

                # decode encoded text
                decoded_data = huffman.decode(encoded_text)
                output_file_encoded.close()
                try:
                    output_file_decoded = open(args.filename[2],'w',encoding="utf-8")
                    output_file_decoded.write(decoded_data)

                    output_file_decoded.close()
                except:
                    print("Unexpected error in copying decoded data to file")
            except:
                print("Unexpected error with output_file")
        except:
            print("Unexpected error during encoding")

        input_file.close()
    except:
        print("can't open input file")
    


if __name__ == '__main__':
    main()