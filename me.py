import pickle
import os


class ME():

    dataset_dir = '/media/sungheui/Temp/KIST/test_data/images'  # 이미지
    data_info = '/media/sungheui/A059-FC93/split_o.pickle'
    #
    # with open(data_info, "rb") as fr:
    #     split = pickle.load(fr)
    #     print(split)
    #
    #     a = []
    #     for i in range(1809):
    #         if 'num_gallery_pids' not in split:
    #             a.append(i)
    #         else:
    #             a.append(i)
    #     split['num_gallery_pids'] = a
    #
    # split['num_gallery_imgs'] = split.pop('num_train_imgs')
    # split['num_gallery_pids'] = split.pop('num_train_pids')
    #
    # dir='/home/sungheui/Desktop/kist'
    # dir2= os.path.join(dir,'data_info.pickle')
    # with open(dir2, 'wb' ) as fw:
    #      pickle.dump(split,fw)
    #
    # with open('/home/sungheui/Desktop/kist/data_info.pickle', 'rb') as fr:
    #     a= pickle.load(fr)
    #     print(a)

   # file = open(dir2, "rb")
   # content = pickle.load(file)

    # img_path = '/home/sungheui/Desktop/kist/images_gallery'
    # person_id = []
    #
    # for name in os.listdir(img_path):
    #    num, pid = name.replace('.jpg','').split('_')
    #
    #    if pid not in person_id:
    #        person_id.append(pid)
    #

    import h5py
    import numpy as np
    filep= './cuhk03/cuhk03_release/cuhk-03.mat'

    array={}
    f=h5py.File(filep)
    for k, v  in f.items():

        array[k] = np.array(v)

    print(array.keys())
    print(array['labeled'])





if __name__ == '__main__':
    a= ME()