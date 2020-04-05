import numpy as np
import imageio
import sys

# a method to get all of the n least significant bits from each channel
# of each pixel in the image
def get_message_bits(img, height, width, num_sig_bits, uses_alpha):
    bits = []
    for r in range(height):
        for c in range(width):
            bits.append(str(img[r,c,0] & (2**num_sig_bits)-1))
            bits.append(str(img[r,c,1] & (2**num_sig_bits)-1))
            bits.append(str(img[r,c,2] & (2**num_sig_bits)-1))
            if uses_alpha:
                bits.append(str(img[r,c,3] & (2**num_sig_bits)-1))
    return "".join(bits)

# a method to turn a list of bits into an image
def extract_image(raw_message, message_height, message_width, header_size):
    image_data = np.ndarray((message_height, message_width, 4))
    # get the hidden image
    begin = header_size
    for r in range(message_height):
    	for c in range(message_width):
    		image_data[r, c][0] = int(raw_message[begin : (begin + 8)], 2)
    		begin += 8
    		image_data[r, c][1] = int(raw_message[begin : (begin + 8)], 2)
    		begin += 8
    		image_data[r, c][2] = int(raw_message[begin : (begin + 8)], 2)
    		begin += 8
    return image_data

# main program starts here
# USAGE: png_image_extract.py file_name header_size num_sig_bits uses_alpha
if __name__ == "__main__":

    # check for proper number of args
    if (len(sys.argv) != 5):
        print("This program takes four arguments")
        print("1. The file name")
        print("2. The size of the message header")
        print("3. The number of least significant bits in each color channel that hold the message")
        print("4. A boolean declaring if the alpha channel holds some of the message or not")
        print("USAGE: png_image_extract.py file_name header_size num_sig_bits uses_alpha")
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

    # isolate the header and extract the height and width from it
    raw_header = all_message_bits[0 : header_size]
    message_height = int(raw_header[0 : 32], 2)
    message_width = int(raw_header[32 : 64], 2)

    # get the image to be output
    raw_message = all_message_bits[header_size : (header_size + (message_height * message_width * 24))]
    output_image = extract_image(raw_message, message_height, message_width, header_size)
    
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