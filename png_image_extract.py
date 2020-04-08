import numpy as np
import imageio
import sys

# isolate the header from the pixels of the image
def get_header_bits(img, header_size, num_sig_bits, uses_alpha, skip_1000, channel_array, num_channels):
    height, width, channels = img.shape
    bits = []
    count = 0
    if skip_1000:
        header_size += 1001

    if (not uses_alpha):
        for r in range(height):
            for c in range(width):
                if (channel_array[0] == 1):
                    bits.append(str(bin((img[r,c,0] & (2**num_sig_bits)-1))[2:]).zfill(num_sig_bits))
                if (channel_array[1] == 1):
                    bits.append(str(bin((img[r,c,1] & (2**num_sig_bits)-1))[2:]).zfill(num_sig_bits))
                if (channel_array[2] == 1):
                    bits.append(str(bin((img[r,c,2] & (2**num_sig_bits)-1))[2:]).zfill(num_sig_bits))
                count += num_sig_bits * num_channels
                if (count > header_size):
                    if skip_1000:
                        return "".join(bits)[1001:header_size]
                    else:
                        return "".join(bits)[0:header_size]

    elif (channels == 4):
        for r in range(height):
            for c in range(width):
                if (channel_array[0] == 1):
                    bits.append(str(bin((img[r,c,0] & (2**num_sig_bits)-1))[2:]).zfill(num_sig_bits))
                if (channel_array[1] == 1):
                    bits.append(str(bin((img[r,c,1] & (2**num_sig_bits)-1))[2:]).zfill(num_sig_bits))
                if (channel_array[2] == 1):
                    bits.append(str(bin((img[r,c,2] & (2**num_sig_bits)-1))[2:]).zfill(num_sig_bits))
                bits.append(str(bin((img[r,c,3] & (2**num_sig_bits)-1))[2:]).zfill(num_sig_bits))
                count += num_sig_bits * (num_channels + 1)
                if (count > header_size):
                    if skip_1000:
                        return "".join(bits)[1001:header_size]
                    else:
                        return "".join(bits)[0:header_size]

    else:
        print("Something seems to have gone wrong")
        print("You probably tried to use the alpha channel when it doesn't exist")
        sys.exit(0)

    print("For some reason the header didn't return from in a loop")
    sys.exit(0)

# isolate the message from the pixels of the image
def get_message_bits(img, message_length, header_size, num_sig_bits, uses_alpha, skip_1000, channel_array, num_channels):
    height, width, channels = img.shape
    bits = []
    count = 0
    if skip_1000:
        header_size += 1001

    if (not uses_alpha):
        for r in range(height):
            for c in range(width):
                if (channel_array[0] == 1):
                    bits.append(str(bin((img[r,c,0] & (2**num_sig_bits)-1))[2:]).zfill(num_sig_bits))
                if (channel_array[1] == 1):
                    bits.append(str(bin((img[r,c,1] & (2**num_sig_bits)-1))[2:]).zfill(num_sig_bits))
                if (channel_array[2] == 1):
                    bits.append(str(bin((img[r,c,2] & (2**num_sig_bits)-1))[2:]).zfill(num_sig_bits))
                count += num_sig_bits * num_channels
                if (count > (header_size+(message_length*24))):
                    if skip_1000:
                        return "".join(bits)[header_size:(header_size+(message_length*24))]
                    else:
                        return "".join(bits)[header_size:(header_size+(message_length*24))]

    else:
        for r in range(height):
            for c in range(width):
                if (channel_array[0] == 1):
                    bits.append(str(bin((img[r,c,0] & (2**num_sig_bits)-1))[2:]).zfill(num_sig_bits))
                if (channel_array[1] == 1):
                    bits.append(str(bin((img[r,c,1] & (2**num_sig_bits)-1))[2:]).zfill(num_sig_bits))
                if (channel_array[2] == 1):
                    bits.append(str(bin((img[r,c,2] & (2**num_sig_bits)-1))[2:]).zfill(num_sig_bits))
                bits.append(str(bin((img[r,c,3] & (2**num_sig_bits)-1))[2:]).zfill(num_sig_bits))
                count += num_sig_bits * (num_channels + 1)
                if (count > (header_size+(message_length*32))):
                    if skip_1000:
                        return "".join(bits)[header_size:(header_size+(message_length*32))]
                    else:
                        return "".join(bits)[header_size:(header_size+(message_length*32))]

    print("For some reason the message didn't return from in a loop")
    sys.exit(0)

# a method to turn a list of bits into an image
def extract_image(img, raw_message, message_height, message_width, header_size, uses_alpha, skip_1000):
    height, width, channels = img.shape
    if (not uses_alpha):
        image_data = np.ndarray((message_height, message_width, 3))
    else:
        image_data = np.ndarray((message_height, message_width, 4))
    if skip_1000:
        header_size += 1001
    # get the hidden image
    begin = header_size
    if (not uses_alpha):
        for r in range(message_height):
            for c in range(message_width):
                if ((begin + 8) < len(raw_message)):
                    image_data[r, c, 0] = int(raw_message[begin : (begin + 8)], 2)
                    begin += 8
                if ((begin + 8) < len(raw_message)):
                    image_data[r, c, 1] = int(raw_message[begin : (begin + 8)], 2)
                    begin += 8
                if ((begin + 8) < len(raw_message)):
                    image_data[r, c, 2] = int(raw_message[begin : (begin + 8)], 2)
                    begin += 8
        return image_data

    else:
        for r in range(message_height):
            for c in range(message_width):
                if ((begin + 8) < len(raw_message)):
                    image_data[r, c, 0] = int(raw_message[begin : (begin + 8)], 2)
                    begin += 8
                if ((begin + 8) < len(raw_message)):
                    image_data[r, c, 1] = int(raw_message[begin : (begin + 8)], 2)
                    begin += 8
                if ((begin + 8) < len(raw_message)):
                    image_data[r, c, 2] = int(raw_message[begin : (begin + 8)], 2)
                    begin += 8
                if ((begin + 8) < len(raw_message)):
                    image_data[r, c, 3] = int(raw_message[begin : (begin + 8)], 2)
                    begin += 8
        return image_data

# main program starts here
# USAGE: png_image_extract.py file_name header_size num_sig_bits uses_alpha skip_1000 channels_used
if __name__ == "__main__":

    # check for proper number of args
    if (len(sys.argv) != 7):
        print("This program takes five arguments")
        print("1. The file name")
        print("2. The size of the message header")
        print("3. The number of least significant bits in each color channel that hold the message")
        print("4. A boolean declaring if the message is hidden in the alpha channel or not")
        print("5. A boolean declaring if the first 1000 bits should be skipped or not")
        print("6. The color channels the message is hidden in")
        print("USAGE: png_message_extract.py file_name header_size num_sig_bits uses_alpha skip_1000")
        sys.exit(0)

    # read in args
    file_name = sys.argv[1]
    header_size = int(sys.argv[2])
    num_sig_bits = int(sys.argv[3])
    uses_alpha = eval(sys.argv[4])
    skip_1000 = eval(sys.argv[5])
    channels_used = sys.argv[6]

    # turn the channels_used input into an array that can be used later
    channel_array = []
    num_channels = 0
    if (channels_used == 'rgb'):
        channel_array = [1, 1, 1]
        num_channels = 3
    elif (channels_used == 'r'):
        channel_array = [1, 0, 0]
        num_channels = 1
    elif (channels_used == 'g'):
        channel_array = [0, 1, 0]
        num_channels = 1
    elif (channels_used == 'b'):
        channel_array = [0, 0, 1]
        num_channels = 1
    elif (channels_used == 'rg'):
        channel_array = [1, 1, 0]
        num_channels = 2
    elif (channels_used == 'rb'):
        channel_array = [1, 0, 1]
        num_channels = 2
    elif (channels_used == 'bg'):
        channel_array = [0, 1, 1]
        num_channels = 2
    else:
        print("Incorrect channels entered")
        print("Remember to use lowercase")
        print("Arguments allowed:")
        print("rgb")
        print("r")
        print("g")
        print("b")
        print("rg")
        print("rb")
        print("gb")
        sys.exit(0)

    # parse image and extract height, width, and number of channels
    img = imageio.imread(file_name)

    # isolate the header and extract the height and width from it
    raw_header = get_header_bits(img, header_size, num_sig_bits, uses_alpha, skip_1000, channel_array, num_channels)
    message_height = int(raw_header[0 : 32], 2)
    message_width = int(raw_header[32 : 64], 2)
    if (message_height > 100000 or message_width > 100000):
        print("The message height found was:", message_height)
        print("The message width found was:", message_width)
        print("This doesn't seem right")
        sys.exit(0)

    # get the image to be output
    raw_message = get_message_bits(img, (message_height*message_width), header_size, num_sig_bits, uses_alpha, skip_1000, channel_array, num_channels)
    output_image = extract_image(img, raw_message, message_height, message_width, header_size, uses_alpha, skip_1000)
    
    # write the output file
    output_name_terms = ("output", sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
    output_name_type_and_terms = (("_".join(output_name_terms)), "png")
    output_file_name = ".".join(output_name_type_and_terms)
    imageio.imwrite(output_file_name, output_image)

    #print the message
    print("The given argument values are:")
    print("file_name:", file_name)
    print("header_size:", header_size)
    print("num_sig_bits:", num_sig_bits)
    print("uses_alpha:", uses_alpha)
    print("skip_1000", skip_1000)
    print("channels_used:", channels_used)
    print("The extracted header is:")
    print("Height:", message_height)
    print("Width:", message_width)
    print("The extracted image is stored as:")
    print(output_file_name)