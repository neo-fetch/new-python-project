from PIL import Image
import pillow_avif

img = Image.open('Ford-Mustang-Fox-Body-via-StanceNation.avif')
img.save('ford.png')