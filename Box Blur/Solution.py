import numpy as np
from math import floor
def solution(image):
    
    if len(image)<3 or len(image[0])<3:
        return [[]]


    blurred_pixel = []
    for i in range(1,len(image)-1):
        for j in range(1,len(image[0])-1):
            blurred_pixel.append(floor((sum(image[i-1][j-1:j+2]) + sum(image[i][j-1:j+2]) + sum(image[i+1][j-1:j+2]))/9))

    blurred_pixel = np.reshape(blurred_pixel,((len(image)-2),len(image[0])-2))
    blurred_pixel = blurred_pixel.tolist()
    return blurred_pixel

    # image = np.array(image)
    # image_rows = np.shape(image)[0]
    # image_cols = np.shape(image)[1]

    # blurred_image = np.delete(image,[0,-1],axis=0)
    # blurred_image = np.delete(blurred_image,[0,-1],axis=-1)

    # print(np.shape(image))
    # for i in range(1,len(image)-1)
    
