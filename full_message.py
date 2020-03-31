import numpy as np
import imageio
if __name__ == "__main__":
    img = imageio.imread("hide_text.png")
    height, width, channels = img.shape
    print("Height:", height, "Width:", width, "Number of Channels:", channels)

    #If it searches the first 3 channels
    #If it searches the least sig bit
    #Gets the header
    print("IF IT SEARCHES THE FIRST 3 CHANNELS: ")
    chars = []
    for r in range(height):
        for c in range(width):
            chars.append(str(img[r,c,0] & 1))
            chars.append(str(img[r,c,1] & 1))
            chars.append(str(img[r,c,2] & 1))
    entire = "".join(chars)
    header = entire[0 : 32]
    header = int(header, 2)

    #Gets the message from the 
    message_binary = entire[32 : (32 + (header * 8))]
    str_data = ' '

    for i in range(0, len(message_binary), 8): 
      temp_data = message_binary[i:i + 8] 
      decimal_data = int(temp_data, 2) 
      str_data = str_data + chr(decimal_data) 
    print("-----------------------------------------------------------")
    print("THE MESSAGE FROM THE LEAST SIG BIT IS: ")
    print("-----------------------------------------------------------")
    print (str_data)

#######################################################################################

    #if it is the least 2 sig bits
    chars = []
    for r in range(height):
        for c in range(width):
               chars.append(str(img[r,c,0] & 1))
               chars.append(str(img[r,c,0] & 10))     
               chars.append(str(img[r,c,1] & 1))
               chars.append(str(img[r,c,1] & 10))
               chars.append(str(img[r,c,2] & 1))
               chars.append(str(img[r,c,2] & 10))
    entire = "".join(chars)
    header = entire[0 : 32]
    header = int(header, 2)

    #gets the message from the least 2 sig bits
    message_binary = entire[32 : (32 + (header * 8))]
    str_data = ' '

    for i in range(0, len(message_binary), 8): 
      temp_data = message_binary[i:i + 8] 
      decimal_data = int(temp_data, 2) 
      str_data = str_data + chr(decimal_data) 
    print("-----------------------------------------------------------")
    print("THE MESSAGE FROM THE TWO LEAST SIG BITS IS: ")
    print("-----------------------------------------------------------")
    print (str_data)



######################################################################################################################################################################################################
######################################################################################################################################################################################################
######################################################################################################################################################################################################


    #If it searches just the first 3 channels

    print("IF IT SEARCHES ALL 4 CHANNELS: ")
    chars = []
    for r in range(height):
        for c in range(width):
               chars.append(str(img[r,c,0] & 1))
               chars.append(str(img[r,c,1] & 1))
               chars.append(str(img[r,c,2] & 1))
               chars.append(str(img[r,c,3] & 1))
    entire = "".join(chars)
    header = entire[0 : 32]
    header = int(header, 2)
      

    message_binary = entire[32 : (32 + (header * 8))]
    str_data = ' '

    for i in range(0, len(message_binary), 8): 
      temp_data = message_binary[i:i + 8] 
      decimal_data = int(temp_data, 2) 
      str_data = str_data + chr(decimal_data) 
    print("-----------------------------------------------------------")
    print("THE MESSAGE FROM THE LEAST SIG BIT IS: ")
    print("-----------------------------------------------------------")
    print (str_data)


#######################################################################################

    #if it is the least 2 sig bits
    chars = []
    for r in range(height):
        for c in range(width):
               chars.append(str(img[r,c,0] & 1))
               chars.append(str(img[r,c,0] & 10))     
               chars.append(str(img[r,c,1] & 1))
               chars.append(str(img[r,c,1] & 10))
               chars.append(str(img[r,c,2] & 1))
               chars.append(str(img[r,c,2] & 10))
               chars.append(str(img[r,c,3] & 1))
               chars.append(str(img[r,c,3] & 10))
    entire = "".join(chars)
    h = entire[0 : 32]
    w = entire[32 : 64]
    h = int(h, 2)
    w = int(w, 2)

    #gets the message from the least 2 sig bits
    message_binary = entire[32 : (32 + (header * 8))]
    str_data = ' '

    for i in range(0, len(message_binary), 8): 
      temp_data = message_binary[i:i + 8] 
      decimal_data = int(temp_data, 2) 
      str_data = str_data + chr(decimal_data) 
    print("-----------------------------------------------------------")
    print("THE MESSAGE FROM THE TWO LEAST SIG BITS IS: ")
    print("-----------------------------------------------------------")
    print (str_data)
