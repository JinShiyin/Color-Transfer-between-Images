'''
Description: 
Author: JinShiyin
Email: shiyinjin@foxmail.com
Date: 2021-11-24 13:52:35
'''
import os
import cv2
from color_transfer import color_transfer

# 2. 笛卡尔积
root_dir = '/data/jsy/code/WCT2/examples/2021-11-22-REST-2'
categroy_list = os.listdir(root_dir)
categroy_list.sort()
out_dir = 'results/2021-11-22-REST-2/'
os.makedirs(out_dir, exist_ok=True)
for category_name in categroy_list:
    c_dir = os.path.join(root_dir, category_name, 'content')
    s_dir = os.path.join(root_dir, category_name, 'style')
    out_dir_ = os.path.join(out_dir, category_name)
    os.makedirs(out_dir_, exist_ok=True)
    print(f'content_dir={c_dir}, style_dir={s_dir}, output={out_dir_}...')

    c_name_list = os.listdir(c_dir)
    c_name_list.sort()
    s_name_list = os.listdir(s_dir)
    s_name_list.sort()

    for i in range(len(c_name_list)):
        for j in range(len(s_name_list)):
            c_path = os.path.join(c_dir, c_name_list[i])
            c_basename = os.path.splitext(c_name_list[i])[0]
            s_path = os.path.join(s_dir, s_name_list[j])
            s_basename = os.path.splitext(s_name_list[j])[0]
            out_path = os.path.join(out_dir_, f'{c_basename}_{s_basename}.png')
            print(f'processing [{c_path}] and [{s_path}]')
            out_img = color_transfer(c_path, s_path)
            cv2.imwrite(out_path, out_img)
            print(f'[{out_path}] saved...')
