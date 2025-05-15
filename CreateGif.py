from PIL import Image
import imageio.v3 as iio 
import numpy as np
filesname = ['nyan-cat1.png', 'nyan-cat2.png', 'nyan-cat3.png']
images = []
target_size = (1500,1000)
for filename in filesname:
    with Image.open(filename) as img:
        img = img.convert("RGB")
        img = img.resize(target_size)
        images.append(np.array(img))
iio.imwrite('GIF.gif', images, duration = 500, loop = 0)

