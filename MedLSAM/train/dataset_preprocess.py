# import os
# import sys

# sys.path.append(os.path.abspath(__file__))
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))  
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# current_directory = os.path.dirname(os.path.abspath(__file__))
# join = os.path.join
# from tqdm import trange
# from data_process.data_process_func import *


# ### rescale CT image to 3*3*3 mm & normalize the HU from [-1000, -200, 200, 1500] to [0,0.2,0.8,1]
# ### this Segmental Linear Normalization Function was proposed in "Automatic Segmentation of Organs-at-Risk from Head-and-Neck CT using Separable Convolutional Neural Network with Hard-Region-Weighted Loss"


# ori_file_ls_path = 'train/config/ori_nii.txt' # change it to the txt file which contains all your CT nii data path
# output_filename = 'train/config/pre_nii.txt' # change it to the txt file which contains all your preprocessed CT nii data path
# ori_file_ls = read_file_list(ori_file_ls_path)
# preprocess_file_ls = []

# for ori_file_path in trange(ori_file_ls):
#     preprocessed_sample = load_and_pre_ct(ori_file_path, mode='image')
#     preprocessed_image = preprocessed_sample['image']
#     file_save_path = ori_file_path.replace('.nii', '_pre.nii') # change it to file save path
#     save_array_as_nifty_volume(preprocessed_image, output_filename, pixel_spacing=[3,3,3])
#     preprocess_file_ls.append(file_save_path)


# with open('train/config/pre_nii.txt', 'w') as file:
#     for item in preprocess_file_ls:
#         file.write(item + '\n')

import os
import sys

sys.path.append(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))  
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
current_directory = os.path.dirname(os.path.abspath(__file__))
join = os.path.join
from tqdm import trange
from data_process.data_process_func import *

### rescale CT image to 3*3*3 mm & normalize the HU from [-1000, -200, 200, 1500] to [0,0.2,0.8,1]
### this Segmental Linear Normalization Function was proposed in "Automatic Segmentation of Organs-at-Risk from Head-and-Neck CT using Separable Convolutional Neural Network with Hard-Region-Weighted Loss"

ori_file_ls_path = 'train/config/ori_nii.txt' # change it to the txt file which contains all your CT nii data path
output_filename = 'train/config/pre_nii.txt' # change it to the txt file which contains all your preprocessed CT nii data path
ori_file_ls = read_file_list(ori_file_ls_path)
preprocess_file_ls = []

# Sử dụng range(len()) để lặp qua chỉ số
for i in trange(len(ori_file_ls)):
    ori_file_path = ori_file_ls[i]  # Lấy đường dẫn từ danh sách
    preprocessed_sample = load_and_pre_ct(ori_file_path, mode='image')
    preprocessed_image = preprocessed_sample['image']
    file_save_path = ori_file_path.replace('.nii', '_pre.nii') # change it to file save path
    save_array_as_nifty_volume(preprocessed_image, file_save_path, pixel_spacing=[3,3,3])  # Sửa filename
    preprocess_file_ls.append(file_save_path)

with open(output_filename, 'w') as file:  # Sử dụng output_filename
    for item in preprocess_file_ls:
        file.write(item + '\n')
