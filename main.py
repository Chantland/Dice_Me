import Dice_Me

# # It may be good to make a virtual enviornment: python3 -m venv venv
# # if you need required packages, enter in the terminal: pip install -r requirements.txt   


# for reloading the main dice file, disregard this unless you change "Dice_Me.py"
from importlib import reload
Dice_Me = reload(Dice_Me)






from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

# A quick gui for selecting images. Most image types should work.
# Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
# image = askopenfilename() # show an "Open" dialog box and return the path to the selected file7


# # feel free to use these as demos
# image = "Images/J&E_Abby_Wedding.jpg"
image = "Images/J&E_Saint_L.jpg"
# image = "Images/J&E_With_Vicky.jpg" #this will not work unless you crop it (see below)
# image = "Images/J&E_Sunshine.jpg"
# image = "Images/Rainbow-Spectrum.jpg"

# input an image in the parenthesis, if it is in another folder, you must specify it
# THIS IS THE ONLY LINE OF CODE YOU TECHNICALLY NEED, otherwise, comment out and use below examples
pic = Dice_Me.dicePic(image)


################## The rest here is optional uncomment to use ##############


# # removing input arguments and including optional arguments
# These following lines run the code the exact same as above except give no prompts or text displays (except showIm)
# pic = Dice_Me.dicePic initializes an object and accepts optional cropping (see below).
# inp_prompt defines if the function will automatically continue and defaults to true
# pic = Dice_Me.dicePic("Images/J&E_Saint_L.jpg", ycrop=[24, 2040], xcrop = [96, 2040], inp_prompt=False)
# pic.dice_alt(pic.posDiceNum[9])             # For creating the mock-up image for later use
#                                             # also accepts pic.dice_alt([72, 128])
# pic.inp_Dice(perc_pip=.06, dice_dict=None, centroidChange=True)  # making the actual dice picture including size of the pips relative to the
#                                             # die, you may also specifiy non-default dice (see below for template!)
# pic.showIm(pic.img_Dice_Pic, print_img=False)   #show the image and optionally print it,
# pic.printIm(file_dup = False)               # print the image (if you didn't print before)
#                                             # pic.printIm(file_dup=True) is optional argument to allow for multiple of
#                                             # the same file printed.





# # optional cropping starting from top left corner (0, 0) coordinate
# # inputs for x and y cropping are start-value then end-value. You can specify 0 for the very start and
# # 'end' for the very end, otherwise just input desired coordinate range (e.g.  ycrop=[30, 1080], xcrop = [105, 'end'])
# pic = Dice_Me.dicePic(image, ycrop=[0, 'end'], xcrop = [0, 'end'])
# pic = Dice_Me.dicePic(image, ycrop=[0, 'end'], xcrop = [450, 1620])
# pic = Dice_Me.dicePic(image, ycrop=[0, 2400], xcrop = [0, 1860])
# pic = Dice_Me.dicePic(image, ycrop=[24, 2040], xcrop = [96, 2040])







# # create your own dict, requires a numpy array.
# # you may change the names of the dice and even the quantity (as long as there are more than 0)
# # DO NOT CHANGE the names 'base_clr' or 'pip_clr' but you can change all other values and names
# import numpy as np

# # for ease of input
# black_pip = np.array([30, 30, 30])
# white_pip = np.array([230, 230, 230])

# dice_dict =  {'dice_black': {'base_clr': np.array([56, 50, 50]), 'pip_clr': white_pip},
#               'dice_brown': {'base_clr': np.array([57, 71, 155]), 'pip_clr': white_pip},
#               'dice_red': {'base_clr': np.array([46, 48, 193]), 'pip_clr': white_pip},
#               'dice_orange': {'base_clr': np.array([68, 107, 250]), 'pip_clr': white_pip},
#               'dice_yellow': {'base_clr': np.array([86, 222, 247]), 'pip_clr': black_pip},
#               'dice_green': {'base_clr': np.array([141, 176, 58]), 'pip_clr': white_pip},
#               'dice_blue': {'base_clr': np.array([224, 114, 43]), 'pip_clr': white_pip},
#               'dice_Lpurple': {'base_clr': np.array([219, 166, 205]), 'pip_clr': white_pip},
#               'dice_Dpurple': {'base_clr': np.array([100, 30, 71]), 'pip_clr': white_pip},
#               'dice_white': {'base_clr': np.array([228, 236, 237]), 'pip_clr': black_pip}
#               }

# dice_dict =  {'dice_black': {'base_clr': np.array([56, 50, 50]), 'pip_clr': white_pip},
#               'dice_brown_lp': {'base_clr': np.array([57, 71, 155]), 'pip_clr': white_pip},
#               'dice_red_lp': {'base_clr': np.array([46, 48, 193]), 'pip_clr': white_pip},
#               'dice_orange_lp': {'base_clr': np.array([68, 107, 250]), 'pip_clr': white_pip},
#               'dice_yellow_lp': {'base_clr': np.array([86, 222, 247]), 'pip_clr': black_pip},
#               'dice_green_lp': {'base_clr': np.array([141, 176, 58]), 'pip_clr': white_pip},
#               'dice_blue_lp': {'base_clr': np.array([224, 114, 43]), 'pip_clr': white_pip},
#               'dice_Lpurple_lp': {'base_clr': np.array([219, 166, 205]), 'pip_clr': white_pip},
#               'dice_Dpurple_lp': {'base_clr': np.array([100, 30, 71]), 'pip_clr': white_pip},
#               'dice_white': {'base_clr': np.array([228, 236, 237]), 'pip_clr': black_pip},
#               'dice_brown_dp': {'base_clr': np.array([57, 71, 155]), 'pip_clr': black_pip},
#               'dice_red_dp': {'base_clr': np.array([46, 48, 193]), 'pip_clr': black_pip},
#               'dice_orange_dp': {'base_clr': np.array([68, 107, 250]), 'pip_clr': black_pip},
#               'dice_green_dp': {'base_clr': np.array([141, 176, 58]), 'pip_clr': black_pip},
#               'dice_blue_dp': {'base_clr': np.array([224, 114, 43]), 'pip_clr': black_pip},
#               'dice_Lpurple_dp': {'base_clr': np.array([219, 166, 205]), 'pip_clr': black_pip},
#               'dice_Dpurple_dp': {'base_clr': np.array([100, 30, 71]), 'pip_clr': black_pip},
#               }

# black_pip = np.array([30, 30, 30])
# white_pip = np.array([230, 230, 230])

# dice_dict =  {'dice_black': {'base_clr': np.array([56, 50, 50]), 'pip_clr': white_pip},
#               'dice_black_d': {'base_clr': np.array([76, 70, 70]), 'pip_clr': white_pip},
#               'dice_brown': {'base_clr': np.array([57, 71, 155]), 'pip_clr': white_pip},
#               'dice_brown_d': {'base_clr': np.array([150, 120, 20]), 'pip_clr': white_pip},
#               'dice_red': {'base_clr': np.array([46, 48, 193]), 'pip_clr': white_pip},
#               'dice_red_d': {'base_clr': np.array([78, 25, 230]), 'pip_clr': white_pip},
#               'dice_orange': {'base_clr': np.array([68, 107, 250]), 'pip_clr': white_pip},
#               'dice_orange_d': {'base_clr': np.array([75, 160, 250]), 'pip_clr': white_pip},
#               'dice_yellow': {'base_clr': np.array([86, 222, 247]), 'pip_clr': black_pip},
#               'dice_yellow_d': {'base_clr': np.array([60, 200, 220]), 'pip_clr': white_pip},
#               'dice_green': {'base_clr': np.array([141, 176, 58]), 'pip_clr': white_pip},
#               'dice_green_d': {'base_clr': np.array([170, 100, 180]), 'pip_clr': white_pip},
#               'dice_blue': {'base_clr': np.array([224, 114, 43]), 'pip_clr': white_pip},
#               'dice_blue_d': {'base_clr': np.array([230, 185, 50]), 'pip_clr': white_pip},
#               'dice_Lpurple': {'base_clr': np.array([219, 166, 205]), 'pip_clr': white_pip},
#               'dice_Lpurple_d': {'base_clr': np.array([200, 125, 240]), 'pip_clr': white_pip},
#               'dice_Dpurple': {'base_clr': np.array([100, 30, 71]), 'pip_clr': white_pip},
#               'dice_Dpurple_d': {'base_clr': np.array([80, 25, 90]), 'pip_clr': white_pip},
#               'dice_white': {'base_clr': np.array([228, 236, 237]), 'pip_clr': black_pip},
#               'dice_white_d': {'base_clr': np.array([150, 150, 150]), 'pip_clr': black_pip}
#               }
# dice_dict =  {
#               'dice_black_d': {'base_clr': np.array([76, 70, 70]), 'pip_clr': white_pip},
#               'dice_brown_d': {'base_clr': np.array([150, 120, 20]), 'pip_clr': white_pip},
#               'dice_red_d': {'base_clr': np.array([78, 25, 230]), 'pip_clr': white_pip},
#               'dice_orange_d': {'base_clr': np.array([75, 160, 250]), 'pip_clr': white_pip},
#               'dice_yellow_d': {'base_clr': np.array([60, 200, 220]), 'pip_clr': white_pip},
#               'dice_green_d': {'base_clr': np.array([170, 100, 180]), 'pip_clr': white_pip},
#               'dice_blue_d': {'base_clr': np.array([230, 185, 50]), 'pip_clr': white_pip},
#               'dice_Lpurple_d': {'base_clr': np.array([200, 125, 240]), 'pip_clr': white_pip},
#               'dice_Dpurple_d': {'base_clr': np.array([80, 25, 90]), 'pip_clr': white_pip},
#               'dice_white_d': {'base_clr': np.array([150, 150, 150]), 'pip_clr': black_pip}
#               }



# pic = Dice_Me.dicePic(image, ycrop=[24, 2040], xcrop = [96, 2040], inp_prompt=False)
# pic.dice_alt(pic.posDiceNum[7])             # For creating the mock-up image for later use
# #                                             # also accepts pic.dice_alt([72, 128])
# pic.inp_Dice(dice_dict=dice_dict)  # making the actual dice picture including size of the pips relative to the
#                                             # die, you may also specifiy non-default dice (see below for template!)
# pic.showIm(pic.img_Dice_Pic, print_img=False)   #show the image and optionally print it,
# # pic.printIm(file_dup = False)               # print the image (if you didn't print before)
# #                                             # pic.printIm(file_dup=True) is optional argument to allow for multiple of
# #                                             # the same file printed.

