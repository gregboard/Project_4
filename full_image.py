import numpy as np
import imageio
if __name__ == "__main__":
    img = imageio.imread("hide_image.png")
    height, width, channels = img.shape
    print("Height:", height, "Width:", width, "Number of Channels:", channels)


######################################################################################################################################################################################################
######################################################################################################################################################################################################
######################################################################################################################################################################################################

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
    h = entire[0 : 32]
    w = entire[32 : 64]
    h = int(h, 2)
    w = int(w, 2)

    #Gets the image
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
    imageio.imwrite("IMG_LSB3.png", img) 
    print("-----------------------------------------------------------")
    print("THE IMAGE FROM THE LEAST SIG BIT IS STORED AS IMG_LSB3.png ")
    print("-----------------------------------------------------------")


#############################################################################################

    #Get the magnified image
    begin = 0
    for r in range(height):
        for c in range(width):
            if entire[begin] == '1':
              insert = '11111111'
            else:
              insert = '00000000'
            img[r, c][0] = int(insert, 2)
            begin = begin + 1

            if entire[begin] == '1':
              insert = '11111111'
            else:
              insert = '00000000'
            img[r, c][1] = int(insert, 2)
            begin = begin + 1

            if entire[begin] == '1':
              insert = '11111111'
            else:
              insert = '00000000'
            img[r, c][2] = int(insert, 2)
            begin = begin + 1
    imageio.imwrite("IMG_mag3.png", img) 
    print("-----------------------------------------------------------")
    print("THE MAGNIFIED IMAGE FOR 3 CHANNELS IS STORED AS IMG_mag3.png ")
    print("-----------------------------------------------------------")

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
    h = entire[0 : 32]
    w = entire[32 : 64]
    h = int(h, 2)
    w = int(w, 2)

    #getimage
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
    imageio.imwrite("IMG_2LSB3.png", img)
    print("-----------------------------------------------------------")
    print("THE MESSAGE FROM THE TWO LEAST SIG BITS IS STORED AS IMG_2LSB3.png: ")
    print("-----------------------------------------------------------")




######################################################################################################################################################################################################
######################################################################################################################################################################################################
######################################################################################################################################################################################################


    #If it searches all 4 channels

    print("IF IT SEARCHES ALL 4 CHANNELS: ")
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
    h = entire[0 : 32]
    w = entire[32 : 64]
    h = int(h, 2)
    w = int(w, 2)
      
    #gets image
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
    imageio.imwrite("IMG_LSB4.png", img)
    print("-----------------------------------------------------------")
    print("THE IMAGE FROM THE LEAST SIG BIT IS STORED AS IMG_LSB4.png ")
    print("-----------------------------------------------------------")

#######################################################################################

#Get the magnified image
    begin = 0
    for r in range(height):
        for c in range(width):
            if entire[begin] == '1':
              insert = '11111111'
            else:
              insert = '00000000'
            img[r, c][0] = int(insert, 2)
            begin = begin + 1

            if entire[begin] == '1':
              insert = '11111111'
            else:
              insert = '00000000'
            img[r, c][1] = int(insert, 2)
            begin = begin + 1

            if entire[begin] == '1':
              insert = '11111111'
            else:
              insert = '00000000'
            img[r, c][2] = int(insert, 2)
            begin = begin + 1

            if entire[begin] == '1':
              insert = '11111111'
            else:
              insert = '00000000'
            img[r, c][3] = int(insert, 2)
            begin = begin + 1
    imageio.imwrite("IMG_mag4.png", img) 
    print("-----------------------------------------------------------")
    print("THE MAGNIFIED IMAGE FOR 4 CHANNELS IS STORED AS IMG_mag4.png ")
    print("-----------------------------------------------------------")


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

    #gets image
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
    imageio.imwrite("IMG_2LSB4.png", img)
    print("-----------------------------------------------------------")
    print("THE IMAGE FROM THE LEAST SIG BIT IS STORED AS IMG_2LSB4.png ")
    print("-----------------------------------------------------------")

