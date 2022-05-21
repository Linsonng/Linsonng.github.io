import cv2
import numpy as np
# import matplotlib.pyplot as plt
import os

images_path = "test_ex/person/"  # original datasets
flip_path = "test_ex/1"  # path to save results
i = 0  # count
temp = 0

list = sorted(os.listdir(images_path))
for m in list:
    i += 1
    print(m)  # print the name of current image
    img = cv2.imread(images_path + "/" + m)
    a1 = img.shape[0]
    b1 = img.shape[1]
    c1 = img.shape[2]

    if i%6 == 0:
        print(i,m)
        for a in range(a1):
            for c in range(c1):
                for b in range(int(b1 / 2)):
                    temp = img[a, b, c]
                    img[a, b, c] = img[a, b1 - b - 1, c]
                    img[a, b1 - b - 1, c] = temp

    if i%6 == 1:
        print(i ,m)
        for a in range(a1):
            for c in range(c1):
                for b in range(b1 - 10):
                    img[a, b, c] = img[a, b+10, c]
                img[a,b1-11:b1,c] = 0

    if i%6 == 2:
        print(i ,m)
        for b in range(b1):
            for c in range(c1):
                for a in range(a1 - 10):
                    img[a, b, c] = img[a+10, b, c]
                img[a1 - 11:a1, b, c] = 0


    if i%6 == 3:
        print(i ,m)
        img = cv2.imread(images_path + "/" + m, cv2.IMREAD_GRAYSCALE)

    if i%6 == 4:
        print(i ,m)
        for b in range(b1):
            for a in range(a1):
                for c in range(c1):
                    img[a, b, c] = 0.6 * img[a, b, c]

    if i%6 == 5:
        print(i ,m)
        img = cv2.resize(img, (int(b1/2),int(a1/2)))



    cv2.imwrite(flip_path + '/' + m[:-4] + '_flip.png', img)

print("There are ", i, "images prosessed and the results are saved in", flip_path)


