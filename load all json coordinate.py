'load all json coordinate  '

import os
import json 

path = 'c:/../.../../.../'                                 # json file path
dirs = os.listdir(path)                                 #all json file name
                     
def ld_json_coordinate ( path , dirs ): 
           
    coordinate  = [] 
    json_shape = []
                                     
    for i in dirs:                       
        if os.path.splitext(i)[1] == ".json": #cut the file name into file name and file extension
            a = path +str(i)  
            with open(a , 'r') as reader:                
                jf = json.loads(reader.read())   
                json_shape.append(jf['shapes'])  
                for j in range(len(jf['shapes'])):  
                    coordinate.append(jf['shapes'][j]['points'])                
    return ( coordinate , json_shape)



