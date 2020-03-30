import numpy as np
import imageio
if __name__ == "__main__":
    img = imageio.imread("hide_text.png")
    height, width, channels = img.shape
    print("Height:", height, "Width:", width, "Number of Channels:", channels)
    #If no opacity
    if channels == 3:
      print("If it has 3 channels: ")
      chars = []
      count = 0
      for r in range(height):
          for c in range(width):
                 chars.append(str(img[r,c,0] & 1))
                 chars.append(str(img[r,c,1] & 1))
                 chars.append(str(img[r,c,2] & 1))
                 count += 1
      temp = "".join(chars)
      header = int(temp, 2)
      print("The length of the message is: ")
      print(header)


    #If opacity is added
    else:
      print("If it has 4 channels: ")
      chars = []
      count = 0
      for r in range(height):
          for c in range(width):
                 chars.append(str(img[r,c,0] & 1))
                 chars.append(str(img[r,c,1] & 1))
                 chars.append(str(img[r,c,2] & 1))
                 #chars.append(str(img[r,c,3] & 1))
                 count += 1
      temp = "".join(chars)
      temp2 = temp[0 : 32]
      print(temp2)
      header = int(temp2, 2)
      print("The length of the message is: ")
      print(header)

    message_binary = temp[32 : (32 + (header * 8))]

    print(message_binary)

    str_data = ' '

    for i in range(0, len(message_binary), 8): 
      temp_data = message_binary[i:i + 8] 
      decimal_data = int(temp_data, 2) 
      str_data = str_data + chr(decimal_data) 

    #message = "".join([chr(int(binary, 2)) for binary in message_binary.split(" ")])
    print("The message is: ")
    print (str_data)