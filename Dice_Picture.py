# # import imageio as iio
# # import visvis as vv
# import cv2
# import math
# # from PIL import Image
#
#
# # used to test
# import numpy as np





class dicepic():
    def __init__(self, image): #Should this automatically give preset values if say this had "preset = True"
        import cv2
        self.img = cv2.imread(image)

    def possible_blocks(Hor_x,Ver_y):
        import numpy as np
        import math


        num1 = Hor_x
        num2 = Ver_y

        x=0
        divisor = 2
        mod_list = []
        greatest_mod = 1
        #for finding the greatest number than can go into both pixel lengths of the photo
        while divisor < min(num1, num2):
            if (num1 % divisor == 0) & (num2 % divisor == 0):
                mod_list.append(divisor)
                num1 = num1/divisor
                num2 = num2/divisor
                greatest_mod *= divisor
                divisor = 2
            else:
                divisor += 1

            #to make sure it has an end point
            x += 1
            if x >200:
                print('too many loops')
                break


        mod_product_list = [] #for storing every number that can go into the two numbers given
        Common_multiple = 1
        while Common_multiple < math.sqrt(greatest_mod):
            if greatest_mod % Common_multiple == 0:
                mod_product_list.extend([Common_multiple, greatest_mod/Common_multiple])
            Common_multiple += 1

        mod_product_list.sort()
        pixel_mod_list = []
        for iDiv in mod_product_list:
            pixel_mod_list.append([Hor_x/iDiv, Ver_y/iDiv])
        pixel_mod_list = np.array(pixel_mod_list)

        return pixel_mod_list


    def show_im(image):
        import cv2
        #show image then run the following commands (or else it crashes)
        cv2.imshow('image', image)
        cv2.waitKey(0)  # show window until key press
        cv2.destroyAllWindows()  # then destroy