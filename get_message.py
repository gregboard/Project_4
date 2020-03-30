import numpy as np
import imageio
if __name__ == "__main__":
    img = imageio.imread("hide_text.png")
    height, width, channels = img.shape
    print("Height:", height, "Width:", width, "Number of Channels:", channels)
    allfour = 1


    #If it searches all 4 channels
    if allfour == 0:
      print("If it seraches all 4 channels: ")
      chars = []
      count = 0
      for r in range(height):
          for c in range(width):
                 chars.append(str(img[r,c,0] & 1))
                 chars.append(str(img[r,c,1] & 1))
                 chars.append(str(img[r,c,2] & 1))
                 chars.append(str(img[r,c,3] & 1))
                 count += 1
      entire = "".join(chars)
      header = entire[0 : 32]
      header = int(header, 2)


######################################################################################################################################################################################################
######################################################################################################################################################################################################
######################################################################################################################################################################################################


    #If it searches just the first 3 channels
    else:
      print("If it searches first 3 channels: ")
      chars = []
      count = 0
      for r in range(height):
          for c in range(width):
                 chars.append(str(img[r,c,0] & 1))
                 chars.append(str(img[r,c,1] & 1))
                 chars.append(str(img[r,c,2] & 1))
                 count += 1
      entire = "".join(chars)
      header = entire[0 : 32]
      header = int(header, 2)


######################################################################################################################################################################################################
######################################################################################################################################################################################################
######################################################################################################################################################################################################


    message_binary = entire[32 : (32 + (header * 8))]
    str_data = ' '

    for i in range(0, len(message_binary), 8): 
      temp_data = message_binary[i:i + 8] 
      decimal_data = int(temp_data, 2) 
      str_data = str_data + chr(decimal_data) 
    print("The message is: ")
    print (str_data)