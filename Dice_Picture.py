
# requires the download of opencv (cv2) and math
import numpy as np
import numpy as np
import math
import cv2

class dicePic():
    def __init__(self, image): # TODO: Should this automatically give preset values if say this had "preset = True"?
        self.img = cv2.imread(image)

    def possible_blocks(self):


        ver_y, hor_x = self.img.shape[0:2] # TODO: I think I want this able function with an optional tuple argument, this might be removed later


        divisor = 2
        mod_list = []
        greatest_mod = 1 # TODO: I think this is superfluous
        num1,num2 = ver_y, hor_x #make copies so we can gradually reduce the number
        num_roll_through = 0
        #for finding the greatest number that can go into both pixel lengths of the photo
        while divisor < min(num1, num2):
            if (num1 % divisor == 0) & (num2 % divisor == 0):
                mod_list.append(divisor)
                num1 = num1/divisor
                num2 = num2/divisor
                greatest_mod *= divisor
                divisor = 2
            else:
                divisor += 1

            num_roll_through += 1
            if divisor == min(ver_y, hor_x):
                raise ValueError("One or more image dimensions cannot be subdivided (a side has a prime length)")


        mod_product_list = [] #for storing every number that can go into the two numbers given
        Common_multiple = 1
        while Common_multiple < math.sqrt(greatest_mod): #find largest common multiple of integer that can go in image dim
            if greatest_mod % Common_multiple == 0:  #if a multiple, store
                mod_product_list.extend([Common_multiple, greatest_mod/Common_multiple])
            Common_multiple += 1 #once it reaches the square root of the greatest mod, there can be no higher number

        mod_product_list.sort()
        dicePixSizeList = []
        for iDiv in mod_product_list:  #take the possible pixel sizes and divide them from the image to get number of dice
            dicePixSizeList.append([ver_y/iDiv, hor_x / iDiv])
        dicePixSizeList = np.array(dicePixSizeList)
        self.posDiceNum = dicePixSizeList

        np.set_printoptions(suppress=True) # suppress scientific notation for easier display

        return print("possible combinations of the number of dice per column per row \n",
                     self.posDiceNum)
        


    def dice_alt(self, xydim): #TODO: make xydim optional and figure out how to correctly label these
        """
        :param xydim: int or None, optional,
            Input number of dice desired on the vertical and horizontal axis. Bust input a list [y,x].
            y into the vertical axis, x divide cleanly into the horizontal axis and.
        :return:
        """
        xydim = np.array(xydim) # convert to ndarray if not already

        if any(self.img.shape[0:2] % xydim != 0): # check if list given is possible to divide into the image neatly
            raise ValueError("X-Y dimensions given must evenly divide into the image dimensions")

        # Take one of the sides (arbitrarily Y) and divide it by the number of dice.
        # The pixel size should be equivalent for both sides
        blockLen = self.img.shape[0] / xydim[0]

        self.img_trans = self.img.copy()
        for y_dice in range(0, xydim[0]):
            for x_dice in range(0, xydim[1]):

                # set rows and columns (this makes it cleaner down below)
                rows = np.arange(y_dice*blockLen, (y_dice+1)*blockLen, dtype=np.intp)
                columns = np.arange(x_dice*blockLen, (x_dice+1)*blockLen, dtype=np.intp)

                # designate the square that we want to average the Red Green and Blue values (3 averages)
                largePix = self.img_trans[np.ix_(rows,columns)]

                # get means of row and column then round
                meanPix = largePix.mean(axis=(0, 1)).round()
                # apply
                self.img_trans[np.ix_(rows,columns)] = meanPix

        self.showIm(image=self.img_trans)

        return print('done')



    def showIm(self, image=None):
        """
        :param image: 3x3 np.array, optional
            displays the image desired or shows the currently transformed img
        :return:
        """
        import cv2

        if image is None:
            image = self.img #TODO: make this actually use a different image input (img2) since the new image is what we want.

        # show image then run the following commands (or else it crashes)
        cv2.imshow('image', image)
        cv2.waitKey(0)  # show window until key press
        cv2.destroyAllWindows()  # then destroy

#
# img2 = img.copy()                               # copy the imgage so the original is unedited
# LargePix = img2[120:240, 120:240, :]            # designate space we want to mean Red Green and Blue (3 averages)
# mean_pix = LargePix.mean(axis = (0,1)).round()  # get means of row and column then round
# # LargePix[:,:] = mean_pix                      # unused to normally set the mean color to LargePix
#
# img2[120:240, 120:240] = mean_pix               # replace all pixels in the originally chosen space with the mean RGB