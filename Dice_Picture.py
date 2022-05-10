
# requires the download of opencv (cv2) and math
import numpy as np
import numpy as np
import math
import cv2

class dicePic():
    def __init__(self, image, crop=None): # TODO: Should this automatically give preset values if say this had "preset = True"?
        self.img = cv2.imread(image)

        # supply x and y values to Crop
        if crop is not None:
            self.img = self.img[0:crop[0],0:crop[1]]
        self.possible_blocks()
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
        dicePixSizeList = np.array(dicePixSizeList, dtype=np.intp)
        self.posDiceNum = dicePixSizeList

        np.set_printoptions(suppress=True) # suppress scientific notation for easier display

        varNum = 0
        print("possible combinations of the number of dice per row per column")
        for idim in self.posDiceNum:
            print(f'{varNum} {idim}')
            varNum += 1
        # return print("possible combinations of the number of dice per row per column \n",
        #              self.posDiceNum)



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
        self.img_reduced = np.zeros((xydim[0],xydim[1],3))  #TODO: make this the only thing that originally displays

        self.meanPix_list = []
        for y_dice in range(0, xydim[0]):
            for x_dice in range(0, xydim[1]):

                # set rows and columns (this makes it cleaner down below)
                rows = np.arange(y_dice*blockLen, (y_dice+1)*blockLen, dtype=np.intp)
                columns = np.arange(x_dice*blockLen, (x_dice+1)*blockLen, dtype=np.intp)

                # designate the square that we want to average the Red Green and Blue values (3 averages)
                largePix = self.img_trans[np.ix_(rows,columns)]

                # get means of row and column then round
                meanPix = largePix.mean(axis=(0, 1)).round()
                self.meanPix_list.append(meanPix)
                # apply
                self.img_trans[np.ix_(rows,columns)] = meanPix
                self.img_reduced[y_dice,x_dice] = meanPix

        self.img_reduced = np.array(self.img_reduced,  dtype=np.uint8)
        dice_count = xydim[0] * xydim[1]
        dice_cost = np.ceil(dice_count/100)
        print(f'total number of dice required {dice_count}')
        print(f'pricing from ${dice_cost * 10} to ${dice_cost * 16}\n')

        print('size in inches if you are using 5mm dice')  # TODO: this might use an input
        print(f'{xydim[0] * 5 / 25.4} tall and {xydim[1] * 12 / 25.4} wide\n')

        print('size in inches if you are using 12mm dice') #TODO: this might use an input
        print(f'{xydim[0]*12/25.4} tall and {xydim[1]*12/25.4} wide\n')

        print('size in inches if you are using 16mm dice')
        print(f'{xydim[0]*16/25.4} tall and {xydim[1]*16/25.4} wide\n')

        self.showIm(image=self.img_trans) #TODO: chnage this to call inp_Dice


    def inp_Dice(self):
        import numpy as np
        from scipy.spatial import distance

        ver_y, hor_x = self.img_reduced.shape[0:2] #get x and y axis of reduced image.


        dice_dict = {} # initialize the colors used for the dice array #TODO: Allow for user input
        dice_dict = {'dice_black': np.array([40, 40, 40]),
                     'dice_brown': np.array([155, 60, 40]),
                     'dice_red': np.array([200, 30, 30]),
                     'dice_orange': np.array([250, 102, 70]),
                     'dice_green': np.array([58, 170, 151]),
                     'dice_blue': np.array([40, 110, 245]),
                     'dice_Lpurple': np.array([200, 160, 200]),
                     'dice_Dpurple': np.array([67, 27, 107]),
                     'dice_white': np.array([230, 230, 230])
                     }

        centroids = []
        for key, value in dice_dict.items():
            centroids.append(value)
        points = self.img_reduced
        points = points.reshape(ver_y * hor_x, 3) #reshape to 2D vector for distance calculation

        die_dist = distance.cdist(points, centroids) # find distance of each block pixel to nearest centroid
        labels = np.argmin(die_dist, axis=1)  # get min column ndx per row

        centroids = np.array(centroids)
        self.Dice_Pic = centroids[labels].astype('uint8') #reassign the centroids to the dice pic
        self.Dice_Pic = self.Dice_Pic.reshape(ver_y, hor_x, 3)
        self.showIm(image=self.Dice_Pic)


    def showIm(self, image=None):
        """
        :param image: n*m*3 np.array, optional
            displays the image desired or shows the currently transformed img
        :return:
        """
        import cv2

        if image is None:
            image = self.img

        # show image then run the following commands (or else it doesn't display)
        cv2.namedWindow("image", cv2.WINDOW_NORMAL)
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