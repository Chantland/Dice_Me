# import imageio as iio #Tried these, they all either fail or not do what I intended
# import visvis as vv  # Might need to
# from PIL import Image
import cv2
import math

import numpy as np


demo_arr = np.random.randint(1,9, size = (4,6,3))
print(demo_arr[0,2,1])

#endregion




# img = iio.imread("J&E_Abby_Wedding.jpg")
# vv.imshow(img)

img = cv2.imread("J&E_Abby_Wedding.jpg")
img = cv2.imread("J&E_Saint_L.jpg")
img = cv2.imread("J&E_With_Vicky.jpg")


#set up dummy to show I can get the mean average of a designated blotch
img2 = img.copy()                               # copy the imgage so the original is unedited
LargePix = img2[120:240, 120:240, :]            # designate space we want to mean Red Green and Blue (3 averages)
mean_pix = LargePix.mean(axis = (0,1)).round()  # get means of row and column then round
# LargePix[:,:] = mean_pix                      # unused to normally set the mean color to LargePix

img2[120:240, 120:240] = mean_pix               # replace all pixels in the originally chosen space with the mean RGB

cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.imshow('image', pic.img)
# cv2.resizeWindow('image', width = 1000, height=1000)
cv2.waitKey(0)  # show window until key press
cv2.destroyAllWindows()  # then destroy

#alternative way of indexing
rows = np.arange(0,120)
columns = np.arange(0,120)
img2[np.ix_(rows,columns)]

# largePix = img_trans[
#            y_dice * blockLen: (y_dice + 1) * blockLen,
#            x_dice * blockLen: (x_dice + 1) * blockLen,
#            :]
#input image to show whatever here
show_im(LargePix)
show_im(img2)
possible_blocks(1080, 1920) # these should eventually changed to just input a picture and it auto extracts the size


x = input(f"Which of the following dice dimensions sets (0 to {len(pic.posDiceNum)-1}) do you want?")
x = int(x)

if x < 0 or x > len(pic.posDiceNum)-1:
    raise ValueError(f"Number chosen is out of bounds, please choose a number between 0 and {len(pic.posDiceNum)-1}")
else:
    print("yay")








### demo for testing out color matrixes (do not delete!!!!!!!)

dice_dict = {'dice_black': np.array([50, 50, 56]),     # RGB
             'dice_brown': np.array([155, 71, 57]),
             'dice_red': np.array([193, 48, 46]),
             'dice_orange': np.array([250, 107, 68]),
             'dice_yellow': np.array([247, 222, 86]),
             'dice_green': np.array([58, 176, 141]),
             'dice_blue': np.array([43, 114, 224]),
             'dice_Lpurple': np.array([205, 166, 219]),
             'dice_Dpurple': np.array([71, 30, 100]),
             'dice_white': np.array([237, 236, 228])
             }
dice_dict = {'dice_black': np.array([56, 50, 50]),      # BRG
             'dice_brown': np.array([57, 155, 71]),
             'dice_red': np.array([46, 193, 48]),
             'dice_orange': np.array([68, 250, 107]),
             'dice_yellow': np.array([86, 247, 222]),
             'dice_green': np.array([141, 58, 176]),
             'dice_blue': np.array([224, 43, 114]),
             'dice_Lpurple': np.array([219, 205, 166]),
             'dice_Dpurple': np.array([100, 71, 30]),
             'dice_white': np.array([228, 237, 236])
             }
dice_dict = {'dice_black': np.array([56, 50, 50]),     # BGR
             'dice_brown': np.array([57, 71, 155]),
             'dice_red': np.array([46, 48, 193]),
             'dice_orange': np.array([68, 107, 250]),
             'dice_yellow': np.array([86, 222, 247]),
             'dice_green': np.array([141, 176, 58]),
             'dice_blue': np.array([224, 114, 43]),
             'dice_Lpurple': np.array([219, 166, 205]),
             'dice_Dpurple': np.array([100, 30, 71]),
             'dice_white': np.array([228, 236, 237])
             }


sample_pic = []
for i in range(0, len(dice_dict)):
    pic_row = []
    for key, value in dice_dict.items():
        pic_row.append(value)
    if i >0:                     # won't work with 0 so skip
        sliced_end = pic_row[-i:] #take the last i list inputs
        del pic_row[-i:]          # now delete them from the original...
        sliced_end.extend(pic_row) # only to add the original start to the end
        sample_pic.append(sliced_end) #the add this list to the growing matrix
    else:
        sample_pic.append(pic_row)
sample_pic = np.array(sample_pic)
sample_pic = sample_pic.astype('uint8') #set dtype or else it will crash

# show image then run the following commands (or else it doesn't display)
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.imshow('image', sample_pic)
cv2.waitKey(0)  # show window until key press
cv2.destroyAllWindows()  # then destroy