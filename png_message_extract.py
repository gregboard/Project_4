import numpy as np
import imageio
import sys

# isolate the header from the pixels of the image
def get_header_bits(img, header_size, num_sig_bits, which_sig_bit, skip_1000, channel_array, flip):
    height, width, channels = img.shape
    uses_alpha = False
    if (channel_array[3] == 1):
        uses_alpha = True
    num_channels = get_num_channels(channel_array, uses_alpha)

    bits = []
    count = 0
    if skip_1000:
        header_size += 1001
    
    if (not flip):
        for r in range(height):
            for c in range(width):
                if (channel_array[0] == 1):
                    bits.append(str(bin((img[r,c,0] >> (which_sig_bit - num_sig_bits)) & (2**num_sig_bits)-1)[2:]).zfill(num_sig_bits))
                if (channel_array[1] == 1):
                    bits.append(str(bin((img[r,c,1] >> (which_sig_bit - num_sig_bits)) & (2**num_sig_bits)-1)[2:]).zfill(num_sig_bits))
                if (channel_array[2] == 1):
                    bits.append(str(bin((img[r,c,2] >> (which_sig_bit - num_sig_bits)) & (2**num_sig_bits)-1)[2:]).zfill(num_sig_bits))
                if ((channel_array[3] == 1) and uses_alpha):
                    bits.append(str(bin((img[r,c,3] >> (which_sig_bit - num_sig_bits)) & (2**num_sig_bits)-1)[2:]).zfill(num_sig_bits))
                count += num_sig_bits * num_channels
                if (count > header_size):
                    if skip_1000:
                        return "".join(bits)[1001:header_size]
                    else:
                        return "".join(bits)[0:header_size]

    else:
        for r in range(width):
            for c in range(height):
                if (channel_array[0] == 1):
                    bits.append(str(bin((img[c,r,0] >> (which_sig_bit - num_sig_bits)) & (2**num_sig_bits)-1)[2:]).zfill(num_sig_bits))
                if (channel_array[1] == 1):
                    bits.append(str(bin((img[c,r,1] >> (which_sig_bit - num_sig_bits)) & (2**num_sig_bits)-1)[2:]).zfill(num_sig_bits))
                if (channel_array[2] == 1):
                    bits.append(str(bin((img[c,r,2] >> (which_sig_bit - num_sig_bits)) & (2**num_sig_bits)-1)[2:]).zfill(num_sig_bits))
                if ((channel_array[3] == 1) and uses_alpha):
                    bits.append(str(bin((img[c,r,3] >> (which_sig_bit - num_sig_bits)) & (2**num_sig_bits)-1)[2:]).zfill(num_sig_bits))
                count += num_sig_bits * num_channels
                if (count > header_size):
                    if skip_1000:
                        return "".join(bits)[1001:header_size]
                    else:
                        return "".join(bits)[0:header_size]

    print("For some reason the header didn't return from in a loop")
    sys.exit(0)

# isolate the message from the pixels of the image
def get_message_bits(img, message_length, header_size, num_sig_bits, which_sig_bit, skip_1000, channel_array, flip):
    height, width, channels = img.shape
    uses_alpha = False
    if (channel_array[3] == 1):
        uses_alpha = True
    num_channels = get_num_channels(channel_array, uses_alpha)

    bits = []
    count = 0
    if skip_1000:
        header_size += 1001

    if (not flip):
        for r in range(height):
            for c in range(width):
                if (channel_array[0] == 1):
                    bits.append(str(bin((img[r,c,0] >> (which_sig_bit - num_sig_bits)) & (2**num_sig_bits)-1)[2:]).zfill(num_sig_bits))
                if (channel_array[1] == 1):
                    bits.append(str(bin((img[r,c,1] >> (which_sig_bit - num_sig_bits)) & (2**num_sig_bits)-1)[2:]).zfill(num_sig_bits))
                if (channel_array[2] == 1):
                    bits.append(str(bin((img[r,c,2] >> (which_sig_bit - num_sig_bits)) & (2**num_sig_bits)-1)[2:]).zfill(num_sig_bits))
                if ((channel_array[3] == 1) and uses_alpha):
                    bits.append(str(bin((img[r,c,3] >> (which_sig_bit - num_sig_bits)) & (2**num_sig_bits)-1)[2:]).zfill(num_sig_bits))
                count += num_sig_bits * num_channels
                if (count > (header_size+(message_length*8))):
                    return "".join(bits)[header_size:(header_size+(message_length*8))]

    else:
        for r in range(width):
            for c in range(height):
                if (channel_array[0] == 1):
                    bits.append(str(bin((img[c,r,0] >> (which_sig_bit - num_sig_bits)) & (2**num_sig_bits)-1)[2:]).zfill(num_sig_bits))
                if (channel_array[1] == 1):
                    bits.append(str(bin((img[c,r,1] >> (which_sig_bit - num_sig_bits)) & (2**num_sig_bits)-1)[2:]).zfill(num_sig_bits))
                if (channel_array[2] == 1):
                    bits.append(str(bin((img[c,r,2] >> (which_sig_bit - num_sig_bits)) & (2**num_sig_bits)-1)[2:]).zfill(num_sig_bits))
                if ((channel_array[3] == 1) and uses_alpha):
                    bits.append(str(bin((img[c,r,3] >> (which_sig_bit - num_sig_bits)) & (2**num_sig_bits)-1)[2:]).zfill(num_sig_bits))
                count += num_sig_bits * num_channels
                if (count > (header_size+(message_length*8))):
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

def set_channel_array(channels_used):
    channel_array = [0, 0, 0, 0]
    for i in range(len(channels_used)):
        if (channels_used[i] == 'r'):
            channel_array[0] = 1
        elif (channels_used[i] == 'g'):
            channel_array[1] = 1
        elif (channels_used[i] == 'b'):
            channel_array[2] = 1
        elif (channels_used[i] == 'a'):
            channel_array[3] = 1
        else:
            print("Channels appear to be entered incorrectly")
            print("Please use lowercase letters")
            print("Acceptable channels are: red, green, blue, alpha")
            print("Channel representations are: r, g, b, a")
            sys.exit(0)
    return channel_array

def get_num_channels(channel_array, uses_alpha):
    num_channels = 0
    for i in range(3):
        if (channel_array[i] == 1):
            num_channels += 1
    if ((channel_array[3] == 1) and uses_alpha):
        num_channels += 1
    return num_channels

# main program starts here
# USAGE: png_message_extract.py file_name header_size num_sig_bits which_sig_bits channels_used skip_1000 flip
if __name__ == "__main__":

    # check for proper number of args
    if (len(sys.argv) != 8):
        print("This program takes seven arguments")
        print("1. The file name")
        print("2. The size of the message header")
        print("3. The number of least significant bits in each color channel that hold the message")
        print("4. Which least significant bits to use")
        print("5. The color channels the message is hidden in")
        print("6. A boolean declaring if the first 1000 bits should be skipped or not")
        print("7. A boolean declaring if pixel order should be flipped from height, width to width, height")
        print("USAGE: png_message_extract.py file_name header_size num_sig_bits which_sig_bits channels_used skip_1000 flip")
        sys.exit(0)

    # eval() is a security risk!! figure out a better way to get a boolean
    # read in args
    file_name = sys.argv[1]
    header_size = int(sys.argv[2])
    num_sig_bits = int(sys.argv[3])
    which_sig_bits = int(sys.argv[4])
    channels_used = sys.argv[5]
    skip_1000 = eval(sys.argv[6])
    flip = eval(sys.argv[7])

    # parse image
    img = imageio.imread(file_name)

    # set the array of color channels used
    channel_array = set_channel_array(channels_used)

    # isolate the header and convert it into an int
    raw_header = get_header_bits(img, header_size, num_sig_bits, which_sig_bits, skip_1000, channel_array, flip)
    message_length = int(raw_header, 2)
    if (message_length > 100000):
        print("The message length found was:", message_length)
        print("This doesn't seem right")
        sys.exit(0)

    # isolate the message and convert it into a character string
    raw_message = get_message_bits(img, message_length, header_size, num_sig_bits, which_sig_bits, skip_1000, channel_array, flip)
    message = extract_message(raw_message)

    #print the message
    print("The given argument values are:")
    print("file_name:", file_name)
    print("header_size:", header_size)
    print("num_sig_bits:", num_sig_bits)
    print("which_sig_bits:", which_sig_bits)
    print("channels_used:", channels_used)
    print("skip_1000:", skip_1000)
    print("flip:", flip)
    print("The extracted header is:")
    print(message_length)
    print("The extracted message is:")
    print()
    print(message)