import os
dir_name = 'C:\\Ddisk\\包裹数据汇总\\\\package_20210318_zhuohang_cao_tang\\boxes\\'

base_name_set = set()
for file_name in os.listdir(dir_name):
    base_name = os.path.splitext(file_name)[0]
    base_name_set.add(base_name)
    # extr_name = os.path.splitext(file_name)[1]
    # if os.path.exists(os.path.join(dir_name, base_name + '.jpg'):

    # # if (os.path.exists(os.path.join(dir_name, base_name + '.jpg')) or os.path.exists(os.path.join(dir_name, base_name + '.png'))) and os.path.exists(os.path.join(dir_name, base_name + '.json')):
    #     if extr_name is '.json':
    #         os.
    #     print('extr_name: ', extr_name)



counter = 3883
for base_name in base_name_set:
    if (os.path.exists(os.path.join(dir_name, base_name + '.jpg')) or os.path.exists(os.path.join(dir_name, base_name + '.png'))) and os.path.exists(os.path.join(dir_name, base_name + '.json')):
        if os.path.exists(os.path.join(dir_name, base_name + '.jpg')):
            os.rename(os.path.join(dir_name, base_name + '.jpg'), os.path.join(dir_name, 'addx_' + str(counter).zfill(7) + '.jpg'))
        if os.path.exists(os.path.join(dir_name, base_name + '.jpeg')):
            os.rename(os.path.join(dir_name, base_name + '.jpeg'), os.path.join(dir_name, 'addx_' + str(counter).zfill(7) + '.jpg'))
        if os.path.exists(os.path.join(dir_name, base_name + '.png')):
            os.rename(os.path.join(dir_name, base_name + '.png'), os.path.join(dir_name,  'addx_' + str(counter).zfill(7) + '.jpg'))
        if os.path.exists(os.path.join(dir_name, base_name + '.json')):
            os.rename(os.path.join(dir_name, base_name + '.json'), os.path.join(dir_name, 'addx_' + str(counter).zfill(7) + '.json'))
        print(base_name)
        counter += 1
    else:
        if os.path.exists(os.path.join(os.path.join(dir_name, base_name + '.jpeg'))):
            os.remove(os.path.join(os.path.join(dir_name, base_name + '.jpeg')))
        if os.path.exists(os.path.join(os.path.join(dir_name, base_name + '.png'))):
            os.remove(os.path.join(os.path.join(dir_name, base_name + '.png')))
        if os.path.exists(os.path.join(os.path.join(dir_name, base_name + '.jpg'))):
            os.remove(os.path.join(os.path.join(dir_name, base_name + '.jpg')))
        if os.path.exists(os.path.join(os.path.join(dir_name, base_name + '.json'))):
            os.remove(os.path.join(os.path.join(dir_name, base_name + '.json')))

# for base_name in base_name_set:
#     if os.path.exists(os.path.join(dir_name, base_name + '.jpeg')) and os.path.exists(os.path.join(dir_name, base_name + '.json')):
#         if os.path.exists(os.path.join(dir_name, base_name + '.jpeg')):
#             os.rename(os.path.join(dir_name, base_name + '.jpeg'), os.path.join(dir_name, str(counter).zfill(7) + '.jpg'))
#         if os.path.exists(os.path.join(dir_name, base_name + '.json')):
#             os.rename(os.path.join(dir_name, base_name + '.json'), os.path.join(dir_name, str(counter).zfill(7) + '.json'))
#         print(base_name)
#     counter += 1
        
        