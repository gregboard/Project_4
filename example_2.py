import numpy as np
import imageio
if __name__ == "__main__":
    img = imageio.imread("hide_text.png")
    height, width, channels = img.shape
    print("Height:", height, "Width:", width, "Number of Channels:", channels)
    
    for r in range(height):
        for c in range(width):
            img[r, c][0] = 0
            img[r, c][1] = img[r, c, 1]
            img[r, c][2] = 0 
    imageio.imwrite("altered_py.png", img)