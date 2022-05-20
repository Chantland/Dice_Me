
# requires the download of opencv (cv2), math, numpy, os, and Scipy
import numpy as np
import math
import cv2

class dicePic():
    def __init__(self, image, ycrop=None, xcrop = None): # TODO: Should this automatically give preset values if say this had "preset = True"?
        self.img = cv2.imread(image)
        self.image_name = image.split('.')[0].split('\\')[-1] # remove file extension and path location


        if ycrop is not None:
            if ycrop[1] == 'end' or ycrop[1] > self.img.shape[0]:
                ycrop[1] = self.img.shape[0]
            self.img = self.img[ycrop[0]:ycrop[1],:]
        if xcrop is not None:
            if xcrop[1] == 'end' or xcrop[1] > self.img.shape[1]:
                xcrop[1] = self.img.shape[1]
            self.img = self.img[:,xcrop[0]:xcrop[1]]
        self.possible_blocks()
    def possible_blocks(self):


        ver_y, hor_x = self.img.shape[0:2] # TODO: I think I want this able function with an optional tuple argument, this might be removed later


        divisor = 2
        mod_list = []
        greatest_mod = 1 # TODO: I think this is superfluous (wait, why?)
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
        # for displaying the possible dice that could fit in the picture.
        # Mark it self. just for ease in case it needs to be accessed later after the picture is done.
        self.posDiceNum = dicePixSizeList

        np.set_printoptions(suppress=True) # suppress scientific notation for easier display

        varNum = 0
        print("possible combinations of the number of dice per row per column")
        for idim in self.posDiceNum:
            print(f'{varNum} {idim}')
            varNum += 1

        dice_alt_inpt = input(f"Which of the following dice dimension sets (0 to {len(self.posDiceNum) - 1}) do you want?")
        dice_alt_inpt = int(dice_alt_inpt)

        if dice_alt_inpt < 0 or dice_alt_inpt > len(self.posDiceNum) - 1:
            raise ValueError(
                f"Number chosen is out of bounds, please choose a number between 0 and {len(self.posDiceNum) - 1}")
        else:
            self.dice_alt(self.posDiceNum[dice_alt_inpt]) #get the intended X and Y axis from available dice dimensions




    def dice_alt(self, yxdim): #TODO: make yxdim optional and figure out how to correctly label these
        """
        :param yxdim: int or None, optional,
            Input number of dice desired on the vertical and horizontal axis. Best input a list [y,x].
            y into the vertical axis, x divide cleanly into the horizontal axis
        :return:
        """
        yxdim = np.array(yxdim) # convert to ndarray if not already

        if any(self.img.shape[0:2] % yxdim != 0): # check if list given is possible to divide into the image neatly
            raise ValueError("X-Y dimensions given must evenly divide into the image dimensions")

        self.y_dice, self.x_dice = np.array(yxdim) # sepaarte into y and x dice for visual ease


        # Take one of the sides (arbitrarily Y) and divide it by the number of dice.
        # The pixel size should be equivalent for both sides
        blockLen = self.img.shape[0] / self.y_dice


        self.img_reduced = np.zeros((self.y_dice,self.x_dice,3))
        for y_dice in range(0, self.y_dice):
            for x_dice in range(0, self.x_dice):

                # set rows and columns (this makes it cleaner down below)
                rows = np.arange(y_dice*blockLen, (y_dice+1)*blockLen, dtype=np.intp)
                columns = np.arange(x_dice*blockLen, (x_dice+1)*blockLen, dtype=np.intp)

                # designate the square that we want to average the Blue Green and Red values (3 averages)
                largePix = self.img[np.ix_(rows,columns)]
                meanPix = largePix.mean(axis=(0, 1)).round()

                # apply
                self.img_reduced[y_dice,x_dice] = meanPix

        self.img_reduced = np.array(self.img_reduced,  dtype=np.uint8)
        dice_count = self.y_dice * self.x_dice
        dice_cost = np.ceil(dice_count/100)
        print(f'total number of dice required {dice_count}')
        print(f'pricing from ${dice_cost * 10} to ${dice_cost * 16}\n')

        print('Size if you are using 5mm dice')  # TODO: this might use an input
        print(f'{np.round(self.y_dice * 5 / 25.4, 1)} inches or {np.round(self.y_dice * 5 / 1000, 2)} meters tall\n'
              f'{np.round(self.x_dice * 5 / 25.4, 1)} inches or {np.round(self.x_dice * 5 / 1000, 2)} meters wide\n')

        print('Size if you are using 12mm dice')
        print(f'{np.round(self.y_dice * 12 / 25.4, 1)} inches or {np.round(self.y_dice * 12 / 1000, 2)} meters tall\n'
              f'{np.round(self.x_dice * 12 / 25.4, 1)} inches or {np.round(self.x_dice * 12 / 1000, 2)} meters wide\n')

        print('Size if you are using 16mm dice')
        print(f'{np.round(self.y_dice * 16 / 25.4, 1)} inches or {np.round(self.y_dice * 12 / 1000, 2)} meters tall\n'
              f'{np.round(self.x_dice * 16 / 25.4, 1)} inches or {np.round(self.x_dice * 12 / 1000, 2)} meters wide\n')


        self.inp_Dice()



    def inp_Dice(self):
        import numpy as np
        from scipy.spatial import distance


        #### region OLD software for showing image without dice pips ##### #todo: maybe make this its own optional def section
        # dice_dict = {} # initialize the colors used for the dice array #TODO: Allow for user input
        # # BLUE-GREEN-RED,  blue shifted down 10%
        # dice_dict = {'dice_black': np.array([56, 50, 50]),
        #              'dice_brown': np.array([57, 71, 155]),
        #              'dice_red': np.array([46, 48, 193]),
        #              'dice_orange': np.array([68, 107, 250]),
        #              'dice_yellow': np.array([86, 222, 247]),
        #              'dice_green': np.array([141, 176, 58]),
        #              'dice_blue': np.array([224, 114, 43]),
        #              'dice_Lpurple': np.array([219, 166, 205]),
        #              'dice_Dpurple': np.array([100, 30, 71]),
        #              'dice_white': np.array([228, 236, 237])
        #              }
        # centroids = []
        # for key, value in dice_dict.items():
        #     centroids.append(value)
        # points = self.img_reduced
        # points = points.reshape(self.y_dice * self.x_dice, 3) #reshape to 2D vector for distance calculation
        #
        # die_dist = distance.cdist(points, centroids) # find distance of each block pixel to nearest centroid
        # labels = np.argmin(die_dist, axis=1)  # get min column ndx per row
        # centroids = np.array(centroids)
        #
        # self.pipless_Dice_Pic = centroids[labels].astype('uint8') #reassign the centroids to the dice pic and set datatype to uint8 (because it will crash otherwise)
        # self.pipless_Dice_Pic = self.pipless_Dice_Pic.reshape(self.y_dice, self.x_dice, 3)
        # self.showIm(image=self.pipless_Dice_Pic)
        # endregion

        #### region closest centroid based off the mean ##### #TODO: implement this as an optional input
        # mean_centroids = np.mean(centroids, axis=1)
        # mean_points = np.mean(points, axis=1)
        # mean_points = mean_points.reshape(self.y_dice * self.x_dice)
        # pseudo_lables = []
        # for i in range(0, len(mean_points)):
        #     lowest_number = 251
        #     lowest_cent = -1
        #     for ii in range(0, len(mean_centroids)):
        #         compNum = abs(mean_points[i] - mean_centroids[ii])
        #         if compNum < lowest_number:
        #             lowest_number = compNum
        #             lowest_cent = ii
        #     pseudo_lables.append(lowest_cent)
        # pseudo_lables = np.array(pseudo_lables)
        # self.Mean_Dice_Pic = centroids[pseudo_lables].astype('uint8')
        # self.Mean_Dice_Pic = self.Mean_Dice_Pic.reshape(self.y_dice, self.x_dice, 3)
        # endregion


        # perc_pip = (math.pi * (2.2**2)) / (15.75**2) # bottom rung dice, generous pip measurement
        # perc_pip = (math.pi * (2.0**2)) / (15.75**2) # bottom run dice, more conservative pip measurement
        # perc_pip = (math.pi * (1.75**2)) / (15.75**2) # chessex dice, 16mm
        # perc_pip = (math.pi * (1.25**2)) / (12.2**2) #chessex die, 12mm
        perc_pip = (math.pi * (18 ** 2)) / (141 ** 2)  # Gimp dice pic in pixel length (currently used)

        # for quickly swapping out pip shading/colors
        black_pip = np.array([30, 30, 30])
        white_pip = np.array([230, 230, 230])

        # BGR light, 10% blue reduced, Dice clror then pip color
        self.dice_dict = {'dice_black': {'base_clr': np.array([56, 50, 50]), 'pip_clr': white_pip},
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

        die_block_img = []  # dice image for later referencing
        ref_clr_array = []  # for matching the pip shaded color,  base die color
        for key, value in self.dice_dict.items():
            # Averaged color of the dice when including a specified number of pips
            self.dice_dict[key]['die_pipNum_clr'] = {}
            # die image (15x15 or otherwise specified) used for later image creation
            self.dice_dict[key]['dice_matrix'] = {}
            for i in range(1, 7):  # run through number of pips
                pip_Area = perc_pip * i  # get pip area
                base_Area = 1 - pip_Area  # get base die area left after taking away pips

                # append to dictionary starting at 1 pips
                self.dice_dict[key]['die_pipNum_clr'][i] = np.round(
                    (value['base_clr'] * base_Area) + (value['pip_clr'] * pip_Area))

                die_matrix = np.full((15, 15, 3), value['base_clr'],
                                     dtype='uint8')  # create a 15x15x3 array containing the original dice color
                # create the pips that will be used.
                mini_pip = np.full((3, 3, 3), value['base_clr'], dtype='uint8')
                mini_pip[1, :] = self.dice_dict[key]['pip_clr']
                mini_pip[:, 1] = self.dice_dict[key]['pip_clr']
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
                    raise ValueError(
                        "pips specified outside of 1-6 range. This may be an error on the software creator's part")
                self.dice_dict[key]['dice_matrix'] = die_matrix

                # die matrix
                die_block_img.append(die_matrix)
                # for adding to a list for ease of access to colors and pips:
                # 0 = for each die get the 6 pip variation dice colors,
                # 1 = base die color
                ref_clr_array.append([self.dice_dict[key]['die_pipNum_clr'][i], value['base_clr']]) #TODO: make this into two separate variables?
        ref_clr_array = np.array(ref_clr_array)
        centroids = ref_clr_array[:, 0]  # dice represent centroids for distance between picture pixels

        points = self.img_reduced
        points = points.reshape(self.y_dice * self.x_dice, 3)  # reshape to 2D vector for distance calculation

        # find distance of each block pixel to nearest centroid
        die_dist = distance.cdist(points, centroids)
        labels = np.argmin(die_dist, axis=1)  # get min column ndx per row

        # create map for dice pic (decided on 15 by 15 pixel dice)
        self.img_Dice_Pic = np.zeros((self.y_dice * 15, self.x_dice * 15, 3))

        # create final picture
        # Use die and pip (centroid label using dice_matrix) with the smallest distance
        ndx_lables = 0
        for y_dice in range(0, self.y_dice):
            for x_dice in range(0, self.x_dice):
                blockLen = 15
                # set rows and columns (this makes it cleaner down below)
                rows = np.arange(y_dice * blockLen, (y_dice + 1) * blockLen, dtype=np.intp)
                columns = np.arange(x_dice * blockLen, (x_dice + 1) * blockLen, dtype=np.intp)
                
                # replace with die
                self.img_Dice_Pic[np.ix_(rows, columns)] = die_block_img[labels[ndx_lables]]
                ndx_lables += 1 
        self.img_Dice_Pic = self.img_Dice_Pic.astype('uint8')

        self.showIm(image=self.img_Dice_Pic)


    def showIm(self, image=None):
        """
        :param image: n*m*3 np.array Uint8 dtype, optional
            displays the image desired or shows the currently transformed img
        :return:
        """
        import cv2

        if image is None:
            image = self.img


        # show image then run the following commands (or else it doesn't display)
        cv2.namedWindow("image", cv2.WINDOW_NORMAL)
        cv2.imshow('image', image)
        print("CLICK ON THE IMAGE AND PRESS ANY KEY TO CONTINUE")
        cv2.waitKey(0)  # show window until key press
        if self.y_dice * self.x_dice > 20000:
            save_pic_ques = input(f"WARNING this picture will be {self.x_dice *15} by {self.y_dice *15} and may be more "
                  f"than {(self.y_dice * self.x_dice)/15000 } megabytes to save. Would you still like to save this photo?"
                  f"\n Type 'y' or 'n'\n")
            if save_pic_ques == 'y' or save_pic_ques == 'Y':
                self.printIm()
                print("Image saved")
            else:
                print("Image not saved")
        else:
            self.printIm()
            print("Image saved")
        cv2.destroyAllWindows()  # then destroy window



    def printIm(self):
        import cv2
        import os

        directory = os.getcwd()  # get current directory
        output_dir = "Image-Output"  # output directory
        output_dir_path = directory + '\\' + output_dir  # output directory path
        os.makedirs(output_dir_path, exist_ok=True)  # make Image-Output folder if it does not exist

        # create the dimension add-ons  for sake of clarity and later use
        img_dim_name = self.y_dice.astype('str') + "y" + self.x_dice.astype('str') + "x"
        # find all duplicates images which share the dimensions as the one we are about to save.
        file_copy = 0
        for i_string in os.listdir(output_dir_path):
            if img_dim_name in i_string and self.image_name in i_string:
                last_digit = i_string.split('-')[-1].split(".")[
                    0]  # split by the dashes then leave off the file extension
                last_digit = int(last_digit)
                file_copy = max(file_copy, last_digit)
        file_copy = str(file_copy + 1)  # do one more than the present number of image duplicates

        # prepare filename, add self. for ease of confirming file name
        self.filename = self.image_name + "-" + img_dim_name + "-" + file_copy + ".png"  # png here is cleaner and smaller file size

        cv2.imwrite(output_dir + "\\" + self.filename, self.img_Dice_Pic)  # write the file to folder

