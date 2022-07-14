import glob
import os
import json
import cv2
import numpy as np
from decimal import Decimal
import shutil
import uuid
import datetime
import argparse

def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data-path', type=str, default='', help='labelme data path')
    parser.add_argument('--convert-save-path', type=str, default='', help='convert data save path')
    parser.add_argument('--enable-classid', nargs='+', type=int, help='target labelme classid convert to coco')
    parser.add_argument('--train-list-save-path', type=str, default='', help='save all training data to a list file')
    opt = parser.parse_args()

    return opt

def check_files(opt):
    all_dir =  glob.glob(os.path.join(opt.data_path, '*/*'))
    done_dir = glob.glob(os.path.join(opt.data_path, '*/*_done'))
    new_dir = list(set(all_dir) - set(done_dir))
    if len(new_dir) == 0:
        print('没有找到新增训练数据，请上传新增数据至: ' +  opt.data_path)
        return
        # raise RuntimeError('没有找到新增训练数据，请上传新增数据至: ' +  opt.data_path)
    dir_exists = []
    for dir_name in new_dir:
        if dir_name + '_done' in done_dir:
            dir_exists.append(dir_name)
    if len(dir_exists) != 0:
        print(dir_exists)
        raise RuntimeError('file exists: ', dir_exists)
    else:
        print('check_done')

def main(opt):
    opt.data_path = 'C:/Ddisk/package_for_test/good'
    opt.convert_save_path = 'C:/Ddisk/package_for_test/coco_for_good'
    random_str = str(uuid.uuid1())
    time_str = datetime.date.today().strftime('%Y%m%d')
    #创建前景路径
    convert_path = os.path.join(opt.convert_save_path, time_str + '_' + random_str + '_fg') 
    img_path = os.path.join(convert_path, 'images')
    label_path = os.path.join(convert_path, 'labels')
    #处理前景图片   
    done_dir_path_set = set() 
    label_files = glob.glob(os.path.join(opt.data_path, '*.json'))
    if len(label_files) != 0:
        if not os.path.exists(img_path):
            os.makedirs(img_path)
        if not os.path.exists(label_path):
            os.makedirs(label_path)
    try:
        for label_file in label_files:
            with open(label_file) as f:
                label_data = json.load(f)
            img_file = label_file.replace('.json', '.jpg')
            if not os.path.exists(img_file):
                continue
            shutil.copyfile(img_file, os.path.join(img_path, os.path.basename(label_file.replace('.json', '.jpg'))))
            img = cv2.imread(img_file)
            img_h, img_w, _ = img.shape
            f.close()
            with open(os.path.join(label_path, os.path.splitext(os.path.basename(label_file))[0] + '.txt'), 'w') as f:
                for shape in label_data['shapes']:
                    class_id = 0
                    rect_points = [(p[0], p[1]) for p in shape['points']]
                    center_x = Decimal(np.clip((rect_points[0][0] +  rect_points[1][0]) / 2, 0, img_w - 1) / img_w).quantize(Decimal('0.000000'))
                    center_y = Decimal(np.clip((rect_points[0][1] +  rect_points[1][1]) / 2, 0, img_h - 1) / img_h).quantize(Decimal('0.000000'))
                    width = Decimal(np.clip(abs(rect_points[1][0] -  rect_points[0][0]), 0, img_w) / img_w).quantize(Decimal('0.000000'))
                    height = Decimal(np.clip(abs(rect_points[1][1] -  rect_points[0][1]), 0, img_h) / img_h).quantize(Decimal('0.000000'))
                    f.write(str(class_id) + ' ' + str(center_x) + ' ' + str(center_y) + ' ' + str(width) + ' ' + str(height) + '\n')
            f.close()
            done_dir_path_set.add(os.path.dirname(label_file))
        if len(label_files) != 0:
            with open(os.path.join(convert_path, 'train.txt'), 'w') as f:
                for img_name in os.listdir(img_path):
                    f.write('./images/' + img_name + '\n')
            f.close()
    except Exception as e:
        print(e)
        raise RuntimeError('error file: ', label_file)

if __name__ == "__main__":
    opt = parse_opt()
    main(opt)
