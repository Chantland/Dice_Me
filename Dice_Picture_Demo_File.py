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
dice_dict = {'dice_black': np.array([56, 50, 50]),     # BGR Light, 10% blue reduced
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





#################################################
#
# ########### multi-dictionary pip color input testing.
#
# import math
# import numpy as np
# from scipy.spatial import distance
#
#
# # NOTE: you'll have to run the dice script initially to make this demo work
# import Dice_Picture
# image = "J&E_Abby_Wedding.jpg"
# pic = Dice_Picture.dicePic(image)
# pic.inp_Dice()
#
#
#
# perc_pip = (math.pi * (2.2**2)) / (15.75**2) # bottom rung dice, generous pip measurement
# perc_pip = (math.pi * (2.0**2)) / (15.75**2) # bottom run dice, more conservative pip measurement
# perc_pip = (math.pi * (1.75**2)) / (15.75**2) # chessex dice, 16mm
# perc_pip = (math.pi * (1.25**2)) / (12.2**2) #chessex die, 12mm
# perc_pip = (math.pi * (18**2)) / (141**2)   #Gimp dice pic in pixel length (currently used)
#
# black_pip = np.array([30, 30, 30])
# white_pip = np.array([230, 230, 230])
#
# dice_dict = {'dice_black': {'base_clr':np.array([56, 50, 50]), 'pip_clr':np.array([230, 230, 230])},     # BGR light, 10% blue reduced, Dice clror then pip color
#              'dice_brown': {'base_clr':np.array([57, 71, 155]), 'pip_clr':np.array([230, 230, 230])},
#              'dice_red': {'base_clr':np.array([46, 48, 193]), 'pip_clr':np.array([230, 230, 230])},
#              'dice_orange': {'base_clr':np.array([68, 107, 250]), 'pip_clr':np.array([230, 230, 230])},
#              'dice_yellow': {'base_clr':np.array([86, 222, 247]), 'pip_clr':np.array([30, 30, 30])},
#              'dice_green': {'base_clr':np.array([141, 176, 58]), 'pip_clr':np.array([230, 230, 230])},
#              'dice_blue': {'base_clr':np.array([224, 114, 43]), 'pip_clr':np.array([230, 230, 230])},
#              'dice_Lpurple': {'base_clr':np.array([219, 166, 205]), 'pip_clr':np.array([230, 230, 230])},
#              'dice_Dpurple': {'base_clr':np.array([100, 30, 71]), 'pip_clr':np.array([230, 230, 230])},
#              'dice_white': {'base_clr':np.array([228, 236, 237]), 'pip_clr':np.array([30, 30, 30])}
#              }
# pip_dice_dict = {}
# dif_Die_Count = 0
# centroids = []
# for key, value in dice_dict.items():
#     pip_dice_dict[key] = {} #extract key
#     for i in range(1, 7):   #run through number of pips
#         dif_Die_Count += 1  # move onto the next pip
#         pip_Area = perc_pip * i    #get pip area
#         base_Area = 1 - pip_Area  #get base die area left after taking away pips
#         # append to dictionary starting at 1 pips (note that the labels start at 0 so to match these up, you will need to add 1 to the label)
#         # value[0] is dice color, value[1] is pip color
#         pip_dice_dict[key][dif_Die_Count] = np.round((value[0] * base_Area) + (value[1] * pip_Area))
#         centroids.append([pip_dice_dict[key][dif_Die_Count], value[0]])  #for adding to a centroid list: averaged die color, base die color
# centroids = np.array(centroids)
#
# points = pic.img_reduced
# ver_y, hor_x = pic.img_reduced.shape[0:2]
# points = points.reshape(ver_y * hor_x, 3) #reshape to 2D vector for distance calculation
#
# die_dist = distance.cdist(points, centroids[:,0]) # find distance of each block pixel to nearest centroid (right now the centroid is complex so we are now indexing)
# labels = np.argmin(die_dist, axis=1)  # get min column ndx per row
#
# pic.Dice_Pic = centroids[labels,0].astype('uint8')  # reassign the centroids to the dice pic and set datatype to uint8 (because it will crash otherwise)
# pic.Dice_Pic = pic.Dice_Pic.reshape(ver_y, hor_x, 3)
# pic.showIm(image=pic.Dice_Pic)

############ implementing pips #########

import math
import numpy as np
from scipy.spatial import distance


# NOTE: you'll have to run the dice script initially to make this demo work
import Dice_Picture
image = "Rainbow-Spectrum.jpg"
pic = Dice_Picture.dicePic(image)
pic.inp_Dice()



# perc_pip = (math.pi * (2.2**2)) / (15.75**2) # bottom rung dice, generous pip measurement
# perc_pip = (math.pi * (2.0**2)) / (15.75**2) # bottom run dice, more conservative pip measurement
# perc_pip = (math.pi * (1.75**2)) / (15.75**2) # chessex dice, 16mm
# perc_pip = (math.pi * (1.25**2)) / (12.2**2) #chessex die, 12mm
perc_pip = (math.pi * (18**2)) / (141**2)   #Gimp dice pic in pixel length (currently used)

black_pip = np.array([30, 30, 30])  #for quickly swapping out pip shading/colors
white_pip = np.array([230, 230, 230])

dice_dict = {'dice_black': {'base_clr':np.array([56, 50, 50]), 'pip_clr':white_pip},     # BGR light, 10% blue reduced, Dice clror then pip color
             'dice_brown': {'base_clr':np.array([57, 71, 155]), 'pip_clr':white_pip},
             'dice_red': {'base_clr':np.array([46, 48, 193]), 'pip_clr':white_pip},
             'dice_orange': {'base_clr':np.array([68, 107, 250]), 'pip_clr':white_pip},
             'dice_yellow': {'base_clr':np.array([86, 222, 247]), 'pip_clr':black_pip},
             'dice_green': {'base_clr':np.array([141, 176, 58]), 'pip_clr':white_pip},
             'dice_blue': {'base_clr':np.array([224, 114, 43]), 'pip_clr':white_pip},
             'dice_Lpurple': {'base_clr':np.array([219, 166, 205]), 'pip_clr':white_pip},
             'dice_Dpurple': {'base_clr':np.array([100, 30, 71]), 'pip_clr':white_pip},
             'dice_white': {'base_clr':np.array([228, 236, 237]), 'pip_clr':black_pip}
             }

die_block_img = [] # dice image for later referencing
ref_clr_array = [] #for matching the pip shaded color,  base die color
for key, value in dice_dict.items():
    dice_dict[key]['die_pipNum_clr'] = {} #Averaged color of the dice when including a specified number of pips
    dice_dict[key]['dice_matrix'] = {} # die image (7x7 or otherwise specified) used for later image creation
    for i in range(1, 7):   #run through number of pips
        pip_Area = perc_pip * i    #get pip area
        base_Area = 1 - pip_Area  #get base die area left after taking away pips

        # append to dictionary starting at 1 pips
        dice_dict[key]['die_pipNum_clr'][i] = np.round((value['base_clr'] * base_Area) + (value['pip_clr'] * pip_Area))

        die_matrix = np.full((15, 15, 3), value['base_clr'],
                              dtype='uint8')  # create a 15x15x3 array containing the original dice color
        # create the pips that will be used.
        mini_pip = np.full((3, 3, 3), value['base_clr'], dtype='uint8')
        mini_pip[1, :] = dice_dict[key]['pip_clr']
        mini_pip[:, 1] = dice_dict[key]['pip_clr']
        # implement the pips (tedious but some python systems may not have the switch statement.
        # This could be shortened but may be more confusing)
        if i == 1:
            die_matrix[6:9, 6:9] = mini_pip
        elif i == 2:
            die_matrix[2:5, 2:5] = mini_pip
            die_matrix[10:13, 10:13] = mini_pip
        elif i == 3:
            die_matrix[2:5, 10:13] = mini_pip
            die_matrix[6:9, 6:9] = mini_pip
            die_matrix[10:13, 2:5] = mini_pip
        elif i == 4:
            die_matrix[2:5, 2:5] = mini_pip
            die_matrix[10:13, 2:5] = mini_pip
            die_matrix[2:5, 10:13] = mini_pip
            die_matrix[10:13, 10:13] = mini_pip
        elif i == 5:
            die_matrix[2:5, 2:5] = mini_pip
            die_matrix[10:13, 2:5] = mini_pip
            die_matrix[6:9, 6:9] = mini_pip
            die_matrix[2:5, 10:13] = mini_pip
            die_matrix[10:13, 10:13] = mini_pip
        elif i == 6:
            die_matrix[2:5, 2:5] = mini_pip
            die_matrix[6:9, 2:5] = mini_pip
            die_matrix[10:13, 2:5] = mini_pip
            die_matrix[2:5, 10:13] = mini_pip
            die_matrix[6:9, 10:13] = mini_pip
            die_matrix[10:13, 10:13] = mini_pip
        else:
            raise ValueError("pips specified outside of 1-6 range. This may be an error on the software creator's part")
        dice_dict[key]['dice_matrix'] = die_matrix


        # die matrix
        die_block_img.append(die_matrix)
        # for adding to a list for ease of access to colors and pips:
        # 0 = for each die get the 6 pip variation dice colors,
        # 1 = base die color
        ref_clr_array.append([dice_dict[key]['die_pipNum_clr'][i], value['base_clr']])
ref_clr_array = np.array(ref_clr_array)
centroids = ref_clr_array[:,0]
# centroids = np.array(centroids)

points = pic.img_reduced
ver_y, hor_x = pic.img_reduced.shape[0:2]
points = points.reshape(ver_y * hor_x, 3) #reshape to 2D vector for distance calculation

die_dist = distance.cdist(points, centroids) # find distance of each block pixel to nearest centroid (right now the centroid is complex so we are now indexing)
labels = np.argmin(die_dist, axis=1)  # get min column ndx per row

# pic.Dice_Pic = ref_clr_array[labels,1].astype('uint8')  # reassign the base die color to the dice pic and set datatype to uint8 (because it will crash otherwise)
# pic.Dice_Pic = pic.Dice_Pic.reshape(ver_y, hor_x, 3)
# pic.showIm(image=pic.Dice_Pic)


## adding the pips (use above)###

img_Dice_Pip = np.zeros((ver_y*15, hor_x*15, 3)) # create map for dice pic (decided on 7 by 7 pixel dice)

ndx_lables = 0
for y_dice in range(0, ver_y):
    for x_dice in range(0, hor_x):

        blockLen = 15
        # set rows and columns (this makes it cleaner down below)
        rows = np.arange(y_dice * blockLen, (y_dice + 1) * blockLen, dtype=np.intp)
        columns = np.arange(x_dice * blockLen, (x_dice + 1) * blockLen, dtype=np.intp)

        # replace with die
        img_Dice_Pip[np.ix_(rows, columns)] = die_block_img[labels[ndx_lables]]

        ndx_lables += 1 #move to next index of the label
img_Dice_Pip = img_Dice_Pip.astype('uint8')

# pic.showIm(image=pic.Dice_Pic)
pic.showIm(image=img_Dice_Pip)
