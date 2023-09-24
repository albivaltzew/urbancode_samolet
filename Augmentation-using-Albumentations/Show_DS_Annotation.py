from DataSet_Prep.Prepare_COCO import Get_Prep_Annotation
from DataSet_Prep.util import *
import cv2


## Put ur Paths
imgDir_Path = "/Users/albivaltzew/Desktop/urbanhack-train/augment_repo/Augmentation-using-Albumentations/out_aug"
Annotation_File = "/Users/albivaltzew/Desktop/urbanhack-train/augment_repo/Augmentation-using-Albumentations/output.json"
#########################
# Get Dict with {
#       img_RGB , bbox , class_labels  
#}

Imgs_Prepared_to_Trans = Get_Prep_Annotation(imgDir_Path,Annotation_File)
#########################
# Put ur classes names 
Label_2_ClassName =["window", "empty", "filled"]

for img in Imgs_Prepared_to_Trans:
    print(img['img_Name'])
    visualize(img['img_RGB'],img['bbox'],img['class_labels'],Label_2_ClassName)
