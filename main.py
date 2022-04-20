import Dice_Picture

from importlib import reload
Dice_Picture = reload(Dice_Picture)

image = "J&E_Abby_Wedding.jpg"
image = "J&E_Saint_L.jpg"
image = "J&E_With_Vicky.jpg"
image = "J&E_Sunshine.jpg"


pic = Dice_Picture.dicePic(image)
# pic = Dice_Picture.dicePic(image, crop=[1620,2040])
pic = Dice_Picture.dicePic(image, crop=[2800,2300])

pic.possible_blocks()

# pic.dice_alt([36,64])
pic.dice_alt(pic.posDiceNum[6])


pic.showIm()
pic.showIm(image=pic.img_trans)
pic.showIm(image=pic.img_reduced)
# pic.showIm()


#for getting those dice strips
image2 = "Dice_strips/p_strip.jpg"
image2 = "Austor 100 piece (square).jpg"

pic2 = Dice_Picture.dicePic(image2)

# Black
# pic2.showIm(pic2.img[380:430, 86:105])
# dice_b = np.median(pic2.img[380:430, 86:105], axis=(0, 1))
dice_b = np.array([30, 30, 30])

# White
# pic2.showIm(pic2.img[380:460, 208:238])
# dice_w = np.median(pic2.img[380:430, 208:238], axis=(0, 1))
dice_w = np.array([240, 240, 240])

# pink
# pic2.showIm(pic2.img[380:460, 344:370])
# dice_p = np.median(pic2.img[380:460, 344:370], axis=(0, 1))
# dice_p = np.array([245, 205, 230])



# Black
# dice_black = np.array([40, 40, 40])

# brown
# dice_brown = np.array([155, 60, 40])

# red
# dice_red = np.array([200, 30, 30])