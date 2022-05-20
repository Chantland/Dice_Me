import Dice_Picture

# for reloading the main dice file, disregard this unless you change "Dice_Picture.py"
from importlib import reload
Dice_Picture = reload(Dice_Picture)

# feel free to use these as demos
image = "Images\\J&E_Abby_Wedding.jpg"
image = "Images\\J&E_Saint_L.jpg"
image = "Images\\J&E_With_Vicky.jpg"
image = "Images\\J&E_Sunshine.jpg"
image = "Images\\Rainbow-Spectrum.jpg"

# input an image in the parenthesis, if it is in another folder, you must specify it
# THIS IS THE ONLY LINE OF CODE YOU NEED
pic = Dice_Picture.dicePic(image)


################## The rest here is optional ##############

# optional cropping starting from top left corner (0, 0) coordinate
# inputs for x and y cropping are start-value then end-value. You can specify 0 for the very start and
# 'end' for the very end, otherwise just input desired coordinate range (e.g.  ycrop=[30, 1080], xcrop = [105, 'end'])
pic = Dice_Picture.dicePic(image, ycrop=[0, 'end'], xcrop = [0, 'end'])
pic = Dice_Picture.dicePic(image, ycrop=[0, 'end'], xcrop = [450, 1620])
pic = Dice_Picture.dicePic(image, ycrop=[0, 2400], xcrop = [0, 1860])
pic = Dice_Picture.dicePic(image, ycrop=[20, 800], xcrop = [60, 1200])

## outdated but completely usable (right now) codings since these functions are now automatically called into other def
pic.possible_blocks()  #for showing possible blocks but this is already called from init
pic.dice_alt([36,64])
pic.dice_alt(pic.posDiceNum[4]) #

pic.inp_Dice() # for showing the picture but using dice

pic.showIm()                      # show original picture
pic.showIm(pic.img_reduced)       #show trans picture but in single pixel blocks for easier display
pic.showIm(image=pic.Dice_Pic)    #show completed dice pic

