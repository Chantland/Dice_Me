import Dice_Picture

from importlib import reload
Dice_Picture = reload(Dice_Picture)

image = "J&E_Abby_Wedding.jpg"
# image = "J&E_Saint_L.jpg"
# image2 = "J&E_With_Vicky.jpg"



pic = Dice_Picture.dicePic(image)
# pic = Dice_Picture.dicePic(image, crop=[1620,2040])

pic.possible_blocks()

# pic.dice_alt([36,64])
pic.dice_alt(pic.posDiceNum[11])


pic.showIm()
pic.showIm(image=pic.img_trans)
pic.showIm(image=pic.img_reduced)
# pic.showIm()