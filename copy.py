'copy'

import shutil 
import os

path  = 'C:/../../../../'  

li_data =  os.listdir( path ) 

def copy( li_data , file_path , new_file_name ) :
    for i in li_data :
        if os.path.exists( os.path.join( file_path , new_file_name )):
            
            old_file = os.path.join( file_path ,  i )          
            new_file = os.path.join( file_path ,  new_file_name ) 
            
            shutil.copy ( old_file , new_file )
            
        else:
            new_file = os.path.join( file_path ,  new_file_name )
            os.makedirs ( new_file )
            old_file = os.path.join( file_path ,  i )          
            
            shutil.copy ( old_file , new_file )
            
'''
Ex:
    
copy( li_data , path , '1' )  

  
#path1 = 'C:/../../'           
#os.makedirs ( os.path.join( path1 ,  ' file_ name ' ) )           #make a file
#shutil.move( os.path.join( path ,  '1' ) ,  path1 )   #move file into new path

'''