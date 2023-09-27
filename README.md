# Secret Word Encoder/Decoder

This Python script allows you to encode and decode text using a substitution cipher. You can use it to secure your messages or files by transforming characters based on a predefined cipher.

## Features

- Encode text or files using a custom substitution cipher.
- Decode encoded text or files back to their original form.
- Command-line interface for easy usage.

## Getting Started
cd secret-word-encoder
pip install -r requirements.txt
python3 secrect_love_letter.py -e -i input.txt -o encoded_output.txt
python3 secrect_love_letter.py -d -i encoded_output.txt -o decoded_output.txt


### Prerequisites

Make sure you have Python 3.11.XX installed on your system.

### Creating Own Chiper
by using SUBSTITUTION_CIPHER.py,You can creat your own encode or decode method.
```bash
python3 SUBSTITUTION_CIPHER.py
```
and copy the output and replace in secrect_love_letter.py's SUBSTITUTION_CIPHER variable
Now only you have key and value for decode and encode 


### Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/ZawwanZ/secret-word-encoder.git
