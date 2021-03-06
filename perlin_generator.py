import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise
try:
    from tqdm import tqdm
except ModuleNotFoundError:
    print("pip install tqdm for progress bars")
 

import heapq
import operator
import noise

while True:

    xpix = int(input("size of map: "))
    ypix = xpix

    scale = 100.0
    octaves = int(input("number of octaves (detail): "))
    persistence = float(input("persistance (how smooth is the terrain): "))
    lacunarity = 2.5
    amplification = float(input("amplification: "))

    pic = []
    noise_pic = []
    visited_pix = []

    for i in tqdm(range(xpix)):
        noise_row = []
        row = []
        for j in range(ypix):
            noise_val = noise.pnoise2(i/scale, 
                                        j/scale, 
                                        octaves=octaves, 
                                        persistence=persistence, 
                                        lacunarity=lacunarity, 
                                        repeatx=xpix, 
                                        repeaty=ypix, 
                                        base=1) * amplification

            noise_row.append(noise_val)
                
            if noise_val >= 0.5:
                row.append([255, 255, 255])

            if noise_val > 0.4 and noise_val < 0.5:
                row.append([50, 50, 50])

            if noise_val > 0.3 and noise_val < 0.4:
                row.append([10, 70, 20])

            if noise_val > 0.2 and noise_val < 0.3:
                row.append([20, 110, 40])

            if noise_val > 0.1 and noise_val < 0.2:
                row.append([40, 140, 80])
                
            if noise_val > 0.0 and noise_val < 0.1:
                row.append([220, 192, 139])
                
            if noise_val >= -0.1 and noise_val <= 0.0:
                row.append([46, 133, 219])

            if noise_val >= -0.5 and noise_val <= -0.1:
                row.append([30, 34, 240])

            if noise_val <= -0.5:
                row.append([12, 36, 97])
                
        pic.append(row)
        noise_pic.append(noise_row)

    plt.imshow(pic)
    plt.show()

    inp = input("make another map? [y/n]: ")

    if inp[0].lower()  == "n":
        break
