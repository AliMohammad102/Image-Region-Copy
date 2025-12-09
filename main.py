import numpy as np
import imageio.v3 as iio
import matplotlib.pyplot as plt


def is_valid_region(Image,row_start,row_end,column_start,column_end):
    h,w,c=Image.shape
    if (row_start>=0) and (row_end> row_start) and (row_end<h) and (column_start>=0) and (column_end > column_start) and (column_end<w):
        return True
    else:
        return False

def get_item_from_image(Image,row_start,row_end,column_start,column_end):
    if is_valid_region(Image,row_start,row_end,column_start,column_end):
        result=np.copy(Image[row_start:row_end,column_start:column_end])
        return result
    else:
        raise ValueError("The input index is out of range.")

def move_item_in_image(Image,item,row_start,row_end,column_start,column_end):
    if is_valid_region(Image,row_start,row_end,column_start,column_end):
        Image[row_start:row_end,column_start:column_end]=item
        return Image
    else:
        raise ValueError("The input index is out of range.")

def main():



    FirstImage=iio.imread("Multimedia/CopyItemInImage/FirstImage.jpg")
    FirstItem=get_item_from_image(FirstImage,490,640,440,600)
    NewFirstImage=move_item_in_image(FirstImage,FirstItem,725,875,920,1080)
    iio.imwrite("NewFirstImage.jpg",NewFirstImage)

    SecondImage=iio.imread("Multimedia/CopyItemInImage/SecondImage.jpg")
    SecondItem=get_item_from_image(SecondImage,3300,4885,1200,2725)
    NewSecondImage=move_item_in_image(SecondImage,SecondItem,1100,2685,1200,2725)
    iio.imwrite("NewSecondImage.jpg",NewSecondImage)

    thirdImage=iio.imread("Multimedia/CopyItemInImage/ThirdImage.jpg")
    thirdItem=get_item_from_image(thirdImage,1400,3495,1750,2820)
    NewthirdImage=move_item_in_image(thirdImage,thirdItem,1400,3495,4400,5470)
    iio.imwrite("NewthirdImage.jpg",NewthirdImage)

main()
