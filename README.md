''Huffman_Encoder''  

Build Your Own Compression Tool  

Step1: Count frequency and test using unittest library  
Step2: Build Huffman Tree  
Step3: Generate codes, using codes encode text, and write header(freq) + encoded_text in output file  
Step4: decode  

I was curious to find How much byte did I saved, but result was shocking:  

wc -c ./challenge-huffman/test.txt  output.txt   
3369045 ./challenge-huffman/test.txt  
14835937 output.txt  

Encoded file is taking way more space. This is because:  
Overhead in Binary-to-Text Conversion: If you store the encoded bits as a string of '0' and '1' characters (e.g., "11001010..."), each bit is stored as a full byte, significantly increasing the file size. This is common if you save the encoded output in ASCII or text format instead of binary.

Solution:
Write Encoded Data in Binary Format: Instead of writing '0' and '1' as strings, use Python's bitarray or struct to store the encoded bits directly as binary data

And result was as expected
wc -c ./challenge-huffman/test.txt output.bin    
3369045 ./challenge-huffman/test.txt
1855733 output.bin