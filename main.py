import Dice_Picture

from importlib import reload
reload(Dice_Picture);

image = "J&E_Abby_Wedding.jpg"

pic = Dice_Picture.dicepic(image)
pic.possible_blocks()
pic.show_im()