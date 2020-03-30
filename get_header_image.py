import numpy as np
import imageio
if __name__ == "__main__":
    img = imageio.imread("hide_image.png")
    height, width, channels = img.shape
    print("Height:", height, "Width:", width, "Number of Channels:", channels)
    #If no opacity
    if channels == 3:
      print("If it has 3 channels: ")
      chars = []
      count = 0
      for r in range(height):
          for c in range(width):
              if count < 22:
                 chars.append(str(img[r,c,0] & 1))
                 chars.append(str(img[r,c,1] & 1))
                 chars.append(str(img[r,c,2] & 1))
                 count += 1
      temp = "".join(chars)
      temp = temp[0 : 63]
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
              if count < 32:
                 chars.append(str(img[r,c,0] & 1))
                 chars.append(str(img[r,c,1] & 1))
                 chars.append(str(img[r,c,2] & 1))
                 #chars.append(str(img[r,c,3] & 1))
                 count += 1
      print(count)
      temp = "".join(chars)
      print(temp)
      h = temp[0 : 31]
      w = temp[32 : 63]
      h = int(h, 2)
      w = int(w, 2)
      print("The height of the image is: ")
      print(h)
      print("The width of the image is: ")
      print(w)


    