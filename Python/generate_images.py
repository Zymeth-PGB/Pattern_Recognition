from PIL import Image
from change_dilation_v2 import change_dilation
from configparser import ConfigParser

def generates(image_path, segm_path, save_path):
    # Open input image
    img1 = Image.open(image_path)
    
    # Read segmentation data
    config = ConfigParser()
    config.read(segm_path)
    
    # Select segmentation data
    pupil_xyr = [float(config['pupil']['center_x']), float(config['pupil']['center_y']), float(config['pupil']['radius'])]
    iris_xyr = [float(config['iris']['center_x']), float(config['iris']['center_y']), float(config['iris']['radius'])]
    
    # Create dilation
    center = round(round(pupil_xyr[2] / iris_xyr[2], 2) - 0.03, 2)
    dil_list = [0] * 7
    dil_list[0] = center
    for i in range(6):
        dil_list[i + 1] = round(dil_list[i] + 0.01, 2)
    
    # Generate images
    idx = 1
    for dil in dil_list:
        img2 = change_dilation(img1, dil, pupil_xyr, iris_xyr)
        img2.save(save_path + str(idx) + ".png")
        idx += 1
        
    return "Successfully"

def read_path(fileName):
    with open(fileName) as f:
        path = [p.strip() for p in f.readlines()]
    
    return path

def main():
    SEGM_PATH = "./Dataset/Position/"
    IMG_PATH = "./Dataset/Train/"
    SAVE_PATH = "./Dataset/Train_v2/"
    
    segm_path = read_path("PositionFile.txt")
    img_path = read_path("imgPath.txt")
    iris = {}
    n = len(img_path)
    
    for i in range(n):
        iris[img_path[i]] = segm_path[i]
    
    for key, value in iris.items():
        tmp_img = IMG_PATH + key
        tmp_segm = SEGM_PATH + value
        tmp_save = SAVE_PATH + key.split('/')[0] + '/'
        
        success = generates(tmp_img, tmp_segm, tmp_save)

    print(success)
    
if __name__ == "__main__":
    main()