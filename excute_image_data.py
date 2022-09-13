# -*- coding: utf-8 -*- 
# @Time : 2022/9/13 下午4:02 
# @Author : qu hao 
# @File : excute_image_data.py

import os


def excute_image(root_path, label):
    image_path = root_path+label+'_image'
    label_path = root_path+label+'_label'
    image = os.listdir(image_path)
    for i in image:
        # 命名格式
        txt_path = i[:-4] + '.txt'
        full_path = os.path.join(label_path, txt_path)
        file = open(full_path, 'w')
        # 写入的语句
        file.write(label)

    print('成功写入-'+label+'-：'+str(len(image)))


def main():
    # txt文件的存放路径
    root_path = "data/train/"
    excute_image(root_path, 'ants')
    excute_image(root_path, 'bees')


if __name__ == '__main__':
    main()