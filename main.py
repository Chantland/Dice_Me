import Dice_Picture

# for reloading the main dice file, disregard this unless you change "Dice_Picture.py"
from importlib import reload
Dice_Picture = reload(Dice_Picture)

# feel free to use these as demos
image = "Images\\J&E_Abby_Wedding.jpg"
image = "Images/J&E_Abby_Wedding.jpg"
image = "Images\\J&E_Saint_L.jpg"
image = "Images\\J&E_With_Vicky.jpg"
image = "Images\\J&E_Sunshine.jpg"
image = "Images\\Rainbow-Spectrum.jpg"

# input an image in the parenthesis, if it is in another folder, you must specify it
# THIS IS THE ONLY LINE OF CODE YOU TECHNICALLY NEED
pic = Dice_Picture.dicePic(image)


################## The rest here is optional ##############


# removing input arguments and including optional arguments
# These following lines run the code the exact same as above except give no prompts or text displays (except showIm)
pic = Dice_Picture.dicePic("Images\\J&E_Abby_Wedding.jpg", ycrop=[0, 'end'], xcrop = [0, 'end'], inp_prompt=False)
pic.possible_blocks()                       #for showing possible blocks but this is already called from init
pic.dice_alt(pic.posDiceNum[7])             # or pic.dice_alt([72, 128]), For creating the mock-up image for later use
pic.inp_Dice(perc_pip=.06, dice_dict=None)  # making the actual dice picture including size of the pips relative to the
                                            # die, you may also specifiy non-default dice (see below for template)
pic.showIm(pic.img_Dice_Pic, print_img=False)   #show the image and optionally print it,
pic.printIm()                               #print the image (if you didn't print before)


# optional cropping starting from top left corner (0, 0) coordinate
# inputs for x and y cropping are start-value then end-value. You can specify 0 for the very start and
# 'end' for the very end, otherwise just input desired coordinate range (e.g.  ycrop=[30, 1080], xcrop = [105, 'end'])
pic = Dice_Picture.dicePic(image, ycrop=[0, 'end'], xcrop = [0, 'end'])
pic = Dice_Picture.dicePic(image, ycrop=[0, 'end'], xcrop = [450, 1620])
pic = Dice_Picture.dicePic(image, ycrop=[0, 2400], xcrop = [0, 1860])
pic = Dice_Picture.dicePic(image, ycrop=[20, 800], xcrop = [60, 1200])






# create your own dict, requires a numpy array.
# you may change the names of the dice and even the quantity (as long as there are more than 0)
# DO NOT CHNAGE 'base_clr' or 'pip_clr'
import numpy as np

# for ease of input
black_pip = np.array([30, 30, 30])
white_pip = np.array([230, 230, 230])

dice_dict =  {'dice_black': {'base_clr': np.array([56, 50, 50]), 'pip_clr': white_pip},
              'dice_brown': {'base_clr': np.array([57, 71, 155]), 'pip_clr': white_pip},
              'dice_red': {'base_clr': np.array([46, 48, 193]), 'pip_clr': white_pip},
              'dice_orange': {'base_clr': np.array([68, 107, 250]), 'pip_clr': white_pip},
              'dice_yellow': {'base_clr': np.array([86, 222, 247]), 'pip_clr': black_pip},
              'dice_green': {'base_clr': np.array([141, 176, 58]), 'pip_clr': white_pip},
              'dice_blue': {'base_clr': np.array([224, 114, 43]), 'pip_clr': white_pip},
              'dice_Lpurple': {'base_clr': np.array([219, 166, 205]), 'pip_clr': white_pip},
              'dice_Dpurple': {'base_clr': np.array([100, 30, 71]), 'pip_clr': white_pip},
              'dice_white': {'base_clr': np.array([228, 236, 237]), 'pip_clr': black_pip}
              }