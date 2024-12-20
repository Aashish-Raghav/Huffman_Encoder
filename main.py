import argparse
from huffman import HuffmanEncoder
from bitarray import bitarray
import json

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

                # Example of saving encoded data in binary
                with open("output.bin", "wb") as file:
                    bit_data = bitarray(encode_text)  # Convert encoded bits to bitarray
                    bit_data.tofile(file)  # Save as binary
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


    try:
        # Example of saving encoded data in binary
        with open("output.txt",'r',encoding="utf-8") as file:
            encoded_text = file.read()

        freq,bin_data = encoded_text.split('\n')

        with open("output.bin", "wb") as file:
            json_data = json.dumps(freq)
            file.write(json_data.encode('utf-8'))  # Write as binary data (UTF-8 encoded)

            # Separate with a newline (or another delimiter)
            file.write(b'\n')

            # Convert the encoded bits (string of '0' and '1') to bitarray and write as binary
            bits = bitarray()
            bits.extend(bin_data)  # Convert the string of '0' and '1' to a bitarray
            bits.tofile(file)
    except:
        print("Unexpected error writing to binary file")



if __name__ == '__main__':
    main()