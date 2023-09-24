from DataSet_Prep.Prepare_COCO import Get_Prep_Annotation,Aug_IMGs
import albumentations as a
import sys
import cv2
from DataSet_Prep.util import *
import json

##################################################################
##################### Transformations ############################
transform1 = a.Compose([
    a.HorizontalFlip(p=0.5),
    a.Rotate(limit=30, p=0.2),
    a.OneOf([
            a.RandomBrightnessContrast(p=0.5),
            a.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.2, p=0.5), # изменение цвета
            a.augmentations.transforms.GaussNoise(var_limit=(10,50),mean=0,p=0.5), # шум гаусса
            a.augmentations.transforms.CLAHE (clip_limit=4.0, tile_grid_size=(8, 8), always_apply=False, p=0.5)
        ], p=0.3),
        a.Blur(blur_limit=3, p=0.1), # Размытие
        # A.augmentations.transforms.Equalize(),
        a.augmentations.geometric.transforms.Affine(p=0.1, shear={'x': (-30, 30), 'y': (-30, 30)}),
        a.OneOf([
            a.augmentations.transforms.ToGray(p=0.2), # оттенки серого
            a.RandomRain(brightness_coefficient=0.9, drop_width=1, blur_value=3, p=0.2), # добавляет дождь
            a.RandomSnow(brightness_coeff=2.5, snow_point_lower=0.3, snow_point_upper=0.5, p=0.2), #Добавляет снег
            a.RandomFog(fog_coef_lower=0.1, fog_coef_upper=0.2, alpha_coef=0.8, p=1), # туман
            a.RandomSunFlare(flare_roi=(0, 0, 1, 0.5), angle_lower=0, angle_upper=1, num_flare_circles_lower=20, num_flare_circles_upper=30, src_radius=100, p=0.02)
            ],p=0.3), # солнечные блики],p=0.3)
], bbox_params=a.BboxParams(format='coco', label_fields=['category_ids']))

# transform2 = a.Compose([
#     a.RandomSunFlare(flare_roi=(0, 0, 1, 0.5), angle_lower=0.5, angle_upper=1, num_flare_circles_lower=0, num_flare_circles_upper=1, src_radius=300, p=1)], # солнечные блики],p=0.3), 
# bbox_params=a.BboxParams(format='coco', label_fields=['category_ids']))

transform2 = a.Compose([
    a.HorizontalFlip(p=0.5),
    a.OneOf([
            a.RandomBrightnessContrast(p=0.5),
            a.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.2, p=0.5), # изменение цвета
            a.augmentations.transforms.GaussNoise(var_limit=(10,50),mean=0,p=0.5), # шум гаусса
            a.augmentations.transforms.CLAHE (clip_limit=4.0, tile_grid_size=(8, 8), always_apply=False, p=0.5)
        ], p=0.3),
    a.Blur(blur_limit=3, p=0.1), # Размытие
    a.augmentations.transforms.Equalize(p=0.5),

], bbox_params=a.BboxParams(format='coco', label_fields=['category_ids']))

transformtest = A. Compose([A.CenterCrop (width=280, height=280, p=1),
], bbox_params=A. BboxParams (format= 'coco' , label_fields=['category_ids'], min_visibility=0.3))


# transforms = [transform1]
# transforms = [transformtest]
transforms = [transform1, transform1, transform1, transform2, transform2, transform2, transform2, transform2, transform2, transform2 ]
##################################################################



in_Path ="/Users/albivaltzew/Desktop/urbanhack-train/augment_repo/Augmentation-using-Albumentations/cvat_images_2part/"
in_Ann_Path = "/Users/albivaltzew/Desktop/urbanhack-train/augment_repo/Augmentation-using-Albumentations/cvat_coco_clean/instances_Train.json"
Out_Path = "/Users/albivaltzew/Desktop/urbanhack-train/augment_repo/Augmentation-using-Albumentations/cvat_coco_out_clean/" 
out_Annotation_p = "/Users/albivaltzew/Desktop/urbanhack-train/augment_repo/Augmentation-using-Albumentations/cvat_coco_out_clean_ann/out.json"


Classes_Name = ["filled", "window", "empty"]

#Rename_COCO(in_Path,in_Ann_Path)

Aug_IMGs(in_Path,in_Ann_Path,Classes_Name,transforms,Out_Path,out_Annotation_p)
    
        
        
        
