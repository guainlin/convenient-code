'crop'

import os
from PIL import Image

path = 'C:/Users/user/Desktop/all pic/'                # pictures file path
file_name = os.listdir(path) 
                               
def crop( int_x , int_y , int_w , int_h ,file_name ):  # w = length ,h =Length                                    
    im = Image.open( path + file_name )
    box = ( int_x , int_y, int_x + int_w , int_y + int_h )
    region = im.crop(box)
    #region.show()
    region.save( os.path.splitext(file_name)[0] +'.jpg')       
   
for i in file_name:
    x = 0
    y = 0
    w = 100
    h = 100
    crop (x,y,w,h,i)
    
    
    
    