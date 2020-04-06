import numpy as np
import imageio
import sys

# a method to get all of the n least significant bits from each channel
# of each pixel in the image
def get_message_bits(img, height, width, num_sig_bits, uses_alpha):
    bits = []
    for r in range(height):
        for c in range(width):
            bits.append(str(bin(img[r,c,0] & (2**num_sig_bits)-1)))
            bits.append(str(bin(img[r,c,1] & (2**num_sig_bits)-1)))
            bits.append(str(bin(img[r,c,2] & (2**num_sig_bits)-1)))
            if uses_alpha:
                bits.append(str(bin(img[r,c,3] & (2**num_sig_bits)-1)))
    return "".join(bits)

# a method to turn a list of bits into a string
def extract_message(raw_message):
    str_data = ""
    for i in range(0, len(raw_message), 8):
        temp_data = raw_message[i : (i + 8)]
        decimal_data = int(temp_data, 2)
        str_data += chr(decimal_data)
    return str_data

# main program starts here
# USAGE: png_message_extract.py file_name header_size num_sig_bits uses_alpha
if __name__ == "__main__":

    # check for proper number of args
    if (len(sys.argv) != 5):
        print("This program takes four arguments")
        print("1. The file name")
        print("2. The size of the message header")
        print("3. The number of least significant bits in each color channel that hold the message")
        print("4. A boolean declaring if the alpha channel holds some of the message or not")
        print("USAGE: png_message_extract.py file_name header_size num_sig_bits uses_alpha")
        sys.exit(0)

    # read in args
    file_name = sys.argv[1]
    header_size = int(sys.argv[2])
    num_sig_bits = int(sys.argv[3])
    uses_alpha = eval(sys.argv[4])

    # parse image and extract height, width, and number of channels
    img = imageio.imread(file_name)
    height, width, channels = img.shape

    # isolate the n least significant bits from each channel of each pixel
    all_message_bits = get_message_bits(img, height, width, num_sig_bits, uses_alpha)

    # isolate the header and convert it into an int
    raw_header = all_message_bits[0 : header_size]
    message_length = int(raw_header, 2)

    # get the final message
    raw_message = all_message_bits[header_size : (header_size + (message_length * 8))]
    message = extract_message(raw_message)

    #print the message
    print("The given argument values are:")
    print("file_name:", file_name)
    print("header_size:", header_size)
    print("num_sig_bits:", num_sig_bits)
    print("uses_alpha", uses_alpha)
    print("The input image has the following dimensions:")
    print("Height:", height)
    print("Width:", width)
    print("Channels:", channels)
    print("The extracted header is:")
    print(message_length)
    print("The extracted message is:")
    print()
    print(message)