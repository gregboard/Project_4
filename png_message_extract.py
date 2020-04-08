import numpy as np
import imageio
import sys

# isolate the header from the pixels of the image
def get_header_bits(img, header_size, num_sig_bits, uses_alpha, skip_1000):
    height, width, channels = img.shape
    bits = []
    count = 0
    if skip_1000:
        header_size += 1001

    if (not uses_alpha):
        for r in range(height):
            for c in range(width):
                bits.append(str(bin((img[r,c,0] & (2**num_sig_bits)-1))[2:]).zfill(num_sig_bits))
                bits.append(str(bin((img[r,c,1] & (2**num_sig_bits)-1))[2:]).zfill(num_sig_bits))
                bits.append(str(bin((img[r,c,2] & (2**num_sig_bits)-1))[2:]).zfill(num_sig_bits))
                count += num_sig_bits * 3
                if (count > header_size):
                    if skip_1000:
                        return "".join(bits)[1001:header_size]
                    else:
                        return "".join(bits)[0:header_size]

    elif (channels == 4):
        for r in range(height):
            for c in range(width):
                bits.append(str(bin((img[r,c,0] & (2**num_sig_bits)-1))[2:]).zfill(num_sig_bits))
                bits.append(str(bin((img[r,c,1] & (2**num_sig_bits)-1))[2:]).zfill(num_sig_bits))
                bits.append(str(bin((img[r,c,2] & (2**num_sig_bits)-1))[2:]).zfill(num_sig_bits))
                bits.append(str(bin((img[r,c,3] & (2**num_sig_bits)-1))[2:]).zfill(num_sig_bits))
                count += num_sig_bits * 4
                if (count > header_size):
                    if skip_1000:
                        return "".join(bits)[1001:header_size]
                    else:
                        return "".join(bits)[0:header_size]

    else:
        print("Something seems to have gone wrong")
        print("You probably tried to use the alpha channel when there isn't one")
        sys.exit(0)

    print("For some reason the header didn't return from in a loop")
    sys.exit(0)

# isolate the message from the pixels of the image
def get_message_bits(img, message_length, header_size, num_sig_bits, uses_alpha, skip_1000):
    height, width, channels = img.shape
    bits = []
    count = 0
    if skip_1000:
        header_size += 1001

    if (not uses_alpha):
        for r in range(height):
            for c in range(width):
                bits.append(str(bin((img[r,c,0] & (2**num_sig_bits)-1))[2:]).zfill(num_sig_bits))
                bits.append(str(bin((img[r,c,1] & (2**num_sig_bits)-1))[2:]).zfill(num_sig_bits))
                bits.append(str(bin((img[r,c,2] & (2**num_sig_bits)-1))[2:]).zfill(num_sig_bits))
                count += num_sig_bits * 3
                if (count > (header_size+(message_length*8))):
                    if skip_1000:
                        return "".join(bits)[header_size:(header_size+(message_length*8))]
                    else:
                        return "".join(bits)[header_size:(header_size+(message_length*8))]

    else:
        for r in range(height):
            for c in range(width):
                bits.append(str(bin((img[r,c,0] & (2**num_sig_bits)-1))[2:]).zfill(num_sig_bits))
                bits.append(str(bin((img[r,c,1] & (2**num_sig_bits)-1))[2:]).zfill(num_sig_bits))
                bits.append(str(bin((img[r,c,2] & (2**num_sig_bits)-1))[2:]).zfill(num_sig_bits))
                bits.append(str(bin((img[r,c,3] & (2**num_sig_bits)-1))[2:]).zfill(num_sig_bits))
                count += num_sig_bits * 4
                if (count > (header_size+(message_length*8))):
                    if skip_1000:
                        return "".join(bits)[header_size:(header_size+(message_length*8))]
                    else:
                        return "".join(bits)[header_size:(header_size+(message_length*8))]

    print("For some reason the message didn't return from in a loop")
    sys.exit(0)

# a method to turn a list of bits into a string
def extract_message(raw_message):
    str_data = ""
    for i in range(0, len(raw_message), 8):
        temp_data = raw_message[i : (i + 8)]
        decimal_data = int(temp_data, 2)
        str_data += chr(decimal_data)
    return str_data

# main program starts here
# USAGE: png_message_extract.py file_name header_size num_sig_bits uses_alpha skip_1000
if __name__ == "__main__":

    # check for proper number of args
    if (len(sys.argv) != 6):
        print("This program takes five arguments")
        print("1. The file name")
        print("2. The size of the message header")
        print("3. The number of least significant bits in each color channel that hold the message")
        print("4. A boolean declaring if the message is hidden in the alpha channel or not")
        print("5. A boolean declaring if the first 1000 bits should be skipped or not")
        print("USAGE: png_message_extract.py file_name header_size num_sig_bits uses_alpha skip_1000")
        sys.exit(0)

    # read in args
    file_name = sys.argv[1]
    header_size = int(sys.argv[2])
    num_sig_bits = int(sys.argv[3])
    uses_alpha = eval(sys.argv[4])
    skip_1000 = eval(sys.argv[5])

    # parse image and extract height, width, and number of channels
    img = imageio.imread(file_name)

    # isolate the header and convert it into an int
    raw_header = get_header_bits(img, header_size, num_sig_bits, uses_alpha, skip_1000)
    message_length = int(raw_header, 2)
    if (message_length > 100000):
        print("The message length found was:", message_length)
        print("This doesn't seem right")
        sys.exit(0)

    # isolate the message and convert it into a character string
    raw_message = get_message_bits(img, message_length, header_size, num_sig_bits, uses_alpha, skip_1000)
    message = extract_message(raw_message)

    #print the message
    print("The given argument values are:")
    print("file_name:", file_name)
    print("header_size:", header_size)
    print("num_sig_bits:", num_sig_bits)
    print("uses_alpha:", uses_alpha)
    print("skip_1000:", skip_1000)
    print("The extracted header is:")
    print(message_length)
    print("The extracted message is:")
    print()
    print(message)