import os
import time

# os.makedirs('folder')
#
# time.sleep(3)
#
# os.makedirs('folder/videos')
# os.makedirs('folder/audios')
# os.makedirs('folder/pictures')
# os.makedirs('folder/documents')
#
# print(len(os.listdir('need_sorting')))

my_list = list(os.listdir('need_sorting'))

for i in my_list:
    my_lst2 = os.path.splitext(i)

if my_lst2[1] in ('.jpg','.png'):
    if os.path.isdir(r'folder\pictures') == False:
        os.makedirs(r'folder\pictures')
    file_path1 = str(os.path.join('need_sorting\\', my_lst2[0] + my_lst2[1]))
    file_path2 = str(os.path.join('folder\pictures\\', my_lst2[0] + my_lst2[1]))
    os.replace(file_path1, file_path2)

if my_lst2[1] in ('.mp4'):
    if os.path.isdir(r'folder\videos') == False:
        os.makedirs(r'folder\videos')
    file_path1 = str(os.path.join('need_sorting\\', my_lst2[0] + my_lst2[1]))
    file_path2 = str(os.path.join('folder\\videos\\', my_lst2[0] + my_lst2[1]))
    os.replace(file_path1, file_path2)

if my_lst2[1] in ('.mp3'):
    if os.path.isdir(r'folder\audios') == False:
        os.makedirs(r'folder\audios')
    file_path1 = str(os.path.join('need_sorting\\', my_lst2[0] + my_lst2[1]))
    file_path2 = str(os.path.join('folder\\audios\\', my_lst2[0] + my_lst2[1]))
    os.replace(file_path1, file_path2)

if my_lst2[1] in ('.txt'):
    if os.path.isdir(r'folder\documents') == False:
        os.makedirs(r'folder\documents')
    file_path1 = str(os.path.join('need_sorting\\', my_lst2[0] + my_lst2[1]))
    file_path2 = str(os.path.join('folder\documents\\', my_lst2[0] + my_lst2[1]))
    os.replace(file_path1, file_path2)