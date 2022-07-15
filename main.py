import os
from PIL import Image

path_dir = 'C:/Users/Mee/Desktop/spilt_screenshot'
file_list = os.listdir(path_dir)

def crop_saver(dir, name):
    img = Image.open(f'{dir}/{name}')
    (w, h) = img.size #(3000, 1920)
    w = w-h
    #(x, y, x+자를 넓이, y+자를 높이)
    a1 = (0, 480, h, w+480)
    a2 = (h, 0, h+w, h)
    cropped_a1 = img.crop(a1)
    cropped_a2 = img.crop(a2)
    cropped_a1.save(f'{dir}/out/{name[:-4]}1.png')
    cropped_a2.save(f'{dir}/out/{name[:-4]}2.png')

# exe
for i in file_list[1:]:
    crop_saver(path_dir, i)

