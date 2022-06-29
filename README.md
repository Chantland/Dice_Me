# Dice_Me
Turns inputted pictures into a dice mosaic output using optional predefined inputs such as: cropping, number of dice (i.e. the dimensions used), color of dice, pip size, and pip color.



<p>
  <img src="https://github.com/Chantland/Dice_Me/blob/main/Images/J&E_Saint_L.jpg" width="350" style="display:inline" alt="Before Dice">
  <img src="https://github.com/Chantland/Dice_Me/blob/main/Images/J&E_Saint_L-56y54x.png?raw=true" style="display:inline" width="338" alt="After Dice">
</p>


## Setup
1. Make sure that you have the required packages listed in `requirements.txt`. Use `pip install -r requirements.txt` if unsure. 
2. The only command required is `Dice_Me.dicePic("image.png")` with `image.png` replaced with your file name and path.
3. However, this will only use the default values for everything. For use of optional inputs use the following as well as checking main.py for general examples for running for running: 


## Functions


| _Function_                       | _Brief Description_ | _required inputs_ | _Optional inputs_ 
| --------------- | -------------- |  --------------- |--------------- |
| dicePic       | Main class, initialize the object the run pic_div. Will run through the rest of the functions unless optionally specified. The only thing absolutely required to call. To intialize the object `pic = Dice_Me.dicePic("image.png")` is reccommended    | `image`="image.png" | `ycrop`=[min,max], `xcrop`=[min,max], `inp_prompt`=boolean|
| pic_div       | Calculates every permutation that the inputted picture may be subdivided by. Only useful to be called if the image inputted is changed and you need to rerun the permutation. Otherwise, this is called when `dicePic` is initialized |||
| dice_alt       | Specify what dice dimensions (number of dice comprising the width and height)  based on the permutations found in `posDiceNum` which is obtained through running the object initialization of `dicePic` or `pic_div`. Input one of the permutations via a 2 integer list/array or just `pic.posDiceNum[int]` | `yxdim`=[ydim,xdim] | |
| inp_Dice       | creates the dice image via scikit-learn using the optional arguments of percentage in decimal of pip size relative to the dice size as well as a dictionary of the dice colors and pip colors. See main.py for a template of the dictionary | | `perc_pip`=float, `dice_dict`=dict |
| showIm       | Used to show the image (UTF-8 encoded image array required and is typically aquired by calling `pic.img_Dice_Pic`). Unless otherwise specified, it will automatically save the the shown image via `printIm`  | `image`=[UTF-8 numpy array]| `print_img`=boolean |
| printIm       | Saves the image to folder "Image-output". Each saved image will also say the x and y dice dimensions used to create it. If desired, you may have duplicate images be each unique and saved. Otherwise if the image output already exists, save over it  || `file_dup`=boolean |
