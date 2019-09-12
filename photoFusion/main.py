# encoding utf-8
from PIL import Image
# pip install opencv-python
import cv2
import os

src_main = cv2.imread('start.jpg')
height, width, channels = src_main.shape


unit_size = 60

y_index = height//unit_size
x_index = width//unit_size

print(height)
print(width)

temp_img = Image.new('RGB', (width, height), '#FFFFFF')

pic_list = []

for item in os.listdir('picture'):
    if item.endswith('.jpg') or item.endswith('.JPG'):
        pic_list.append(item)
total = len(pic_list)

x = 0
y = 0

for i in range(int(x_index*y_index)):
    # print(f'目前进度{i}/{x_index*y_index}')
    # print('--------------------第 %s 个---------------------------' %i)
    # print(i)
    # print(total)
    # print(i%total)
    temp = Image.open('picture\\' + pic_list[i%total]).resize((unit_size,unit_size), Image.ANTIALIAS)
    temp_img.paste(temp, (x*unit_size, y*unit_size))
    x += 1
    if x == x_index:
        x = 0
        y += 1

print('素材合成完成')
temp_img.save('temp.jpg', quality=100)

src_temp = cv2.imread('temp.jpg')

result = cv2.addWeighted(src_main, 0.6, src_temp, 0.4, 0)
cv2.imwrite('result.jpg', result)