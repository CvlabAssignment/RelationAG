from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import glob
import re
import sys
import urllib
import tarfile
import zipfile
import os.path as osp
from scipy.io import loadmat
import numpy as np
import h5py
#from scipy.misc import imsave
import torch.utils.data as torch_data
import pickle
from skimage import io
from skimage.transform import resize

#from ..utils.osutils import mkdir_if_missing
#from ..utils.serialization import write_json, read_json


class KIST(object):
    """

    Dataset statistics:
    # identities: 1360
    # images: 13164
    # cameras: 6
    # splits: 20 (classic)
    Args:
        split_id (int): split index (default: 0)
        cuhk03_labeled (bool): whether to load labeled images; if false, detected images are loaded (default: False)
    """




    def __init__(self, split_id=0, verbose=True,  **kwargs):
        super(KIST, self).__init__()
        self.dataset_dir = '/media/sungheui/Temp/KIST/test_data/images' #이미지
        self.data_info = '/media/sungheui/A059-FC93/split_o.pickle'

       # img_dir= '/home/sungheui/Desktop/kist/imagesx1_gallery/'
        img_dir2 = '/home/sungheui/Desktop/kist/images5ox1_gallery/'
        img_dir3 = '/home/sungheui/Desktop/kist/images5ox1_query/'


      #  split={'query': 23 , 'gallery': 23, 'num_query_imgs': 2408, 'num_gallery_imgs': 2408, 'num_query_pids': 3,  'num_gallery_pids': 3   }

        def _extract_data_info(img_dir):

            tmp=[]
            unique_pid=set()

            for name in os.listdir(img_dir):

                num, pid = name.replace('.jpg', '').split('_')
                img_path = os.path.join(img_dir, name)
                cam_id = num

                if pid not in unique_pid:
                    unique_pid.add(pid)

                tmp.append((img_path,pid, cam_id))


                query_info = [tmp,len(unique_pid) ,3398] #image path, num unique person id(H00081, H00069, H00001. H00068) ,image num
         #   gallery_info = [tmp,unique_pid , 7]

            return  query_info


        gallery_info = _extract_data_info(img_dir = img_dir2) #img_dir2: gallery
        query_info = _extract_data_info(img_dir=img_dir3)



        split=[{'query': query_info[0], 'gallery': gallery_info[0],
            'num_query_pids': query_info[1], 'num_query_imgs': query_info[2],
            'num_gallery_pids': gallery_info[1], 'num_gallery_imgs': gallery_info[2]}]


        self.query = split[0]['query']
        self.gallery = split[0]['gallery']
        self.num_query_pids = split[0]['num_query_pids']
        self.num_gallery_pids = split[0]['num_gallery_pids']





if __name__ == '__main__':
    a= KIST()