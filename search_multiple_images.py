import numpy as np
import imageio
import sys


#Woof1
##################################################################################################################################
##################################################################################################################################
##################################################################################################################################

# a method to get all of the n least significant bits from each channel
# of each pixel in the image
def get_message_bits(img, height, width, num_sig_bits, uses_alpha):
    bits = []
    count = 0
    if uses_alpha != 1:
        if order == 'BGR':
            for r in range(height):
                for c in range(width):
                    if count < 100000:
                        bits.append(bin(img[r,c,0] & (128)) [2:])
                        #bits.append(bin(img[r,c,1] & (4)) [2:])
                        #bits.append(bin(img[r,c,2] & (4)) [2:])

                        #if file_name == 'WinkyFace.png' or file_name == 'Grooming.png' or file_name == 'TheGrassIsGreener.png':
                           # bits.append(bin(img[r,c,3] & (4)) [2:])

                        count = count + 1
            return "".join(bits)
        if order == 'RGB':
            for r in range(height):
                for c in range(width):
                    if count < 100000:
                        bits.append(bin(img[r,c,0] & (2**num_sig_bits)-1) [2:])
                        bits.append(bin(img[r,c,1] & (2**num_sig_bits)-1) [2:])
                        bits.append(bin(img[r,c,2] & (2**num_sig_bits)-1) [2:])
                        if file_name == 'WinkyFace.png' or file_name == 'Grooming.png' or file_name == 'TheGrassIsGreener.png':
                            bits.append(bin(img[r,c,3] & (2**num_sig_bits)-1) [2:])
                        count = count + 1
            return "".join(bits)


# a method to turn a list of bits into an image
def extract_image(raw_message, message_height, message_width, header_size, img):
    image_data = img#np.ndarray((message_height, message_width, 4))
    # get the hidden image
    begin = header_size
    for r in range(message_height):
    	for c in range(message_width):
            if begin + 8 < len(raw_message):
                image_data[r, c][0] = int(raw_message[begin : (begin + 8)], 2)
                begin += 8
            if begin + 8 < len(raw_message):
                image_data[r, c][1] = int(raw_message[begin : (begin + 8)], 2)
                begin += 8
            if begin + 8 < len(raw_message):
                image_data[r, c][2] = int(raw_message[begin : (begin + 8)], 2)
                begin += 8
    return image_data

# main program starts here
# USAGE: png_image_extract.py file_name header_size num_sig_bits uses_alpha
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
        sys.exit(0)
    files = ['Woof1.png', 'WinkyFace.png', 'TheGrassIsGreener.png', 'StegTest.png', 'MoJoJoJoCouch.png', 'LastBastionOfRadiance.png', 'Grooming.png', 'Gadget.png']
    #files = ['LastBastionOfRadiance.png']

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

        print(height)
        print(width)

        # isolate the n least significant bits from each channel of each pixel
        all_message_bits = get_message_bits(img, height, width, num_sig_bits, uses_alpha)


        if uses_alpha != 1:
            # isolate the header and extract the height and width from it
            if plus_thousand:
                raw_header = all_message_bits[1001 : (header_size + 1001)]
            else:
                raw_header = all_message_bits[0 : (header_size)]
            print(raw_header)
            check_header = int(raw_header, 2)
            message_height = int(raw_header[0 : 32], 2)
            message_width = int(raw_header[32 : 64], 2)
            print(message_height)
            print(message_width)

            # get the image to be output
            message = ''
            print(file_name)
            print(len(all_message_bits))
            if message_height < 50000:
                if plus_thousand:
                    raw_message = all_message_bits[header_size + 1001: len(all_message_bits)]#(header_size +1001 + (message_height * message_width * 240000000000000000))]
                else:
                    raw_message = all_message_bits[header_size : (header_size + (message_height * message_width * 24))]
                output_image = extract_image(raw_message, message_height, message_width, header_size, img)

                # write the output file
                output_name_terms = ("output", sys.argv[2], sys.argv[3], sys.argv[4])
                output_name_type_and_terms = (("_".join(output_name_terms)), "png")
                output_file_name = ".".join(output_name_type_and_terms)
                imageio.imwrite(output_file_name, output_image)


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
                print("Height:", message_height)
                print("Width:", message_width)
                print("The extracted image is stored as:")
                print(output_file_name)
            else:
                print("This file probably doenst have a message")
        else:
            print("This doesnt use the alpha channel")
        print('---------------------------------------------------------------------------------')


