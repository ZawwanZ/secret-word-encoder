import argparse

# Define a fixed substitution cipher key
SUBSTITUTION_CIPHER = {'a': 't', 'b': '2', 'c': 'j', 'd': 'i', 'e': 'f', 'f': 'z', 'g': 'F', 'h': 'c', 'i': 'J', 'j': 'P', 'k': 'Q', 'l': 'a', 'm': 'u', 'n': 'S', 'o': '8', 'p': 'R', 'q': '1', 'r': 'm', 's': 'x', 't': 'B', 'u': 'g', 'v': 'U', 'w': 'k', 'x': 'v', 'y': 'r', 'z': '6', 'A': '9', 'B': 'Z', 'C': 'M', 'D': 'O', 'E': 'D', 'F': '7', 'G': 'H', 'H': 'X', 'I': '4', 'J': 'N', 'K': '0', 'L': 'I', 'M': 'n', 'N': 'C', 'O': 'b', 'P': 'h', 'Q': '3', 'R': 'Y', 'S': 'y', 'T': ' ', 'U': 'W', 'V': 'p', 'W': '5', 'X': 'q', 'Y': 'T', 'Z': 'E', '0': 'A', '1': 'w', '2': 'o', '3': 'L', '4': 'G', '5': 'l', '6': 'e', '7': 'V', '8': 'K', '9': 'd', ' ': 's'}

# Create a reverse mapping for decryption
REVERSE_SUBSTITUTION_CIPHER = {v: k for k, v in SUBSTITUTION_CIPHER.items()}

def encode(word):
    encoded_word = ''
    for char in word:
        if char in SUBSTITUTION_CIPHER:
            encoded_word += SUBSTITUTION_CIPHER[char]
        else:
            encoded_word += char
    return encoded_word

def decode(encoded_word):
    decoded_word = ''
    for char in encoded_word:
        if char in REVERSE_SUBSTITUTION_CIPHER:
            decoded_word += REVERSE_SUBSTITUTION_CIPHER[char]
        else:
            decoded_word += char
    return decoded_word

def encode_file(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
            for line in input_file:
                encoded_line = encode(line)
                output_file.write(encoded_line)
    except FileNotFoundError:
        print("Input file not found.")
    except Exception as e:
        print("An error occurred:", str(e))

def decode_file(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
            for line in input_file:
                decoded_line = decode(line)
                output_file.write(decoded_line)
    except FileNotFoundError:
        print("Input file not found.")
    except Exception as e:
        print("An error occurred:", str(e))

def main():
    parser = argparse.ArgumentParser(description="Secret Word Encoder/Decoder")
    parser.add_argument("-e", "--encode", action="store_true", help="Encode the input file")
    parser.add_argument("-d", "--decode", action="store_true", help="Decode the input file")
    parser.add_argument("-i", "--input", required=True, help="Input file path")
    parser.add_argument("-o", "--output", required=True, help="Output file path")

    args = parser.parse_args()

    if args.encode:
        encode_file(args.input, args.output)
        print("File encoded successfully!")
    elif args.decode:
        decode_file(args.input, args.output)
        print("File decoded successfully!")

if __name__ == "__main__":
    main()
