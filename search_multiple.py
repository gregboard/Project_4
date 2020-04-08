import numpy as np
import imageio
import sys

#Woof1
################################################################################################################
################################################################################################################
################################################################################################################


# a method to get all of the n least significant bits from each channel
# of each pixel in the image
def get_message_bits(img, height, width, num_sig_bits, uses_alpha):
    if uses_alpha != 1:
        bits = []
        count = 0
        if order == 'BGR':
            for r in range(168):
                for c in range(190):
                    if count < 100000:
                        bits.append(str(bin(img[c,r,0] & (2**num_sig_bits)-1) [2:]).zfill(num_sig_bits))
                        bits.append(str(bin(img[c,r,1] & (2**num_sig_bits)-1) [2:]).zfill(num_sig_bits))
                        bits.append(str(bin(img[c,r,2] & (2**num_sig_bits)-1) [2:]).zfill(num_sig_bits))
                        if file_name == 'output_1_0_0.png' or file_name == 'Grooming.png' or file_name == 'TheGrassIsGreener.png':
                             bits.append(str(bin(img[r,c,3] & (2**num_sig_bits)-1) [2:]).zfill(num_sig_bits))
                        count = count + 1
            return "".join(bits)
        if order == 'RGB':
            for r in range(width):
                for c in range(height):
                    if count < 100000:
                        bits.append(str(bin(img[c,r,0] & (2**num_sig_bits)-1) [2:]).zfill(num_sig_bits))
                        bits.append(str(bin(img[c,r,1] & (2**num_sig_bits)-1) [2:]).zfill(num_sig_bits))
                        bits.append(str(bin(img[c,r,2] & (2**num_sig_bits)-1) [2:]).zfill(num_sig_bits))
                        if file_name == 'WinkyFace.png' or file_name == 'Grooming.png' or file_name == 'TheGrassIsGreener.png':
                            bits.append(str(bin(img[c,r,3] & (2**num_sig_bits)-1) [2:]).zfill(num_sig_bits))
                        count = count + 1
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
    if (len(sys.argv) != 6):
        print("This program takes four arguments")
        print("1. The size of the message header")
        print("2. The number of least significant bits in each color channel that hold the message")
        print("3. A boolean declaring if the alpha channel holds some of the message or not")
        print("4. A boolean declaring if the message is skipping 1000 characters after the header or not")
        print("5. A boolean declaring the order of which pixels the program looks at")
        print("USAGE: png_message_extract.py file_name header_size num_sig_bits uses_alpha")
    #files = ['TheGrassIsGreener.png', 'StegTest.png', 'MoJoJoJoCouch.png', 'Gadget.png']
    files = ['GadgetRadiator.png']

    for i in files:

        # read in args
        file_name = i
        header_size = int(sys.argv[1])
        num_sig_bits = int(sys.argv[2])
        uses_alpha = eval(sys.argv[3])
        plus_thousand = eval(sys.argv[4])
        order = (sys.argv[5])
        # parse image and extract height, width, and number of channels
        img = imageio.imread(file_name)
        height, width, channels = img.shape

        # parse image and extract height, width, and number of channels
        img = imageio.imread(file_name)
        height, width, channels = img.shape

        # isolate the n least significant bits from each channel of each pixel
        all_message_bits = get_message_bits(img, height, width, num_sig_bits, uses_alpha)

        # isolate the header and convert it into an int
        if uses_alpha != 1:
            

            # get the final message
            if plus_thousand:
                raw_header = all_message_bits[1001 : header_size + 1001]
                message_length = int(raw_header, 2)
                #header_size = header_size + 1001
                raw_message = all_message_bits[header_size + 1001: (header_size + 1001 + (message_length * 8))]
            else:
                raw_header = all_message_bits[0 : header_size]
                message_length = int(raw_header, 2)
                raw_message = all_message_bits[header_size: (header_size + (message_length * 8))]
            print(raw_header)
            message = ''
            print(file_name)
            if message_length < 5000000:
                message = extract_message(raw_message)

                    #print the message
                print("The given argument values are:")
                print("file_name:", file_name)
                print("header_size:", header_size)
                print("num_sig_bits:", num_sig_bits)
                print("uses_alpha", uses_alpha)
                print("plus_thousand", plus_thousand)
                print("The input image has the following dimensions:")
                print("Height:", height)
                print("Width:", width)
                print("Channels:", channels)
                print("The extracted header is:")
                print(message_length)
                print("The extracted message is:")
                print()
                print(message)
            else:
                print("This file probably doenst have a message")
            print('---------------------------------------------------------------------------------')
        else:
            print("This doesnt use the alpha channel")
sys.exit()

