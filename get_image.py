import numpy as np
import imageio
if __name__ == "__main__":
    img = imageio.imread("hide_image.png")
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
              if count < 22:
                 chars.append(str(img[r,c,0] & 1))
                 chars.append(str(img[r,c,1] & 1))
                 chars.append(str(img[r,c,2] & 1))
                 chars.append(str(img[r,c,3] & 1))
                 count += 1
      entire = "".join(chars)
      h = entire[0 : 32]
      w = entire[32 : 64]
      h = int(h, 2)
      w = int(w, 2)
      print("The height of the image is: ")
      print(h)
      print("The width of the image is: ")
      print(w)

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
      h = entire[0 : 32]
      w = entire[32 : 64]
      h = int(h, 2)
      w = int(w, 2)
      print("The height of the image is: ")
      print(h)
      print("The width of the image is: ")
      print(w)

######################################################################################################################################################################################################
######################################################################################################################################################################################################
######################################################################################################################################################################################################
    
    #transfers the message if we are not including opacity
    if allfour == 1:
      begin = 64
      end = 72
      for r in range(h):
          for c in range(w):
              img[r, c][0] = int(entire[begin : end], 2)
              begin = begin + 8
              end = end + 8

              img[r, c][1] = int(entire[begin : end], 2)
              begin = begin + 8
              end = end + 8

              img[r, c][2] = int(entire[begin : end], 2)
              begin = begin + 8
              end = end + 8
      print("check test.png for the image")
      imageio.imwrite("test.png", img)

######################################################################################################################################################################################################
######################################################################################################################################################################################################
######################################################################################################################################################################################################

    #transfers the message if we are including opacity
    else:
      begin = 64
      end = 72
      for r in range(h):
          for c in range(w):
              img[r, c][0] = int(entire[begin : end], 2)
              begin = begin + 8
              end = end + 8

              img[r, c][1] = int(entire[begin : end], 2)
              begin = begin + 8
              end = end + 8

              img[r, c][2] = int(entire[begin : end], 2)
              begin = begin + 8
              end = end + 8

              img[r, c][3] = int(entire[begin : end], 2)
              begin = begin + 8
              end = end + 8
      print("check test.png for the image")
      imageio.imwrite("test.png", img)


