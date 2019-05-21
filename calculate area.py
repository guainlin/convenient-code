'calculate area with coordination'

def polygon_area(points):                  
    area = 0                                #use shoelace formul 
    q = points[-1]                          #ex: x1~4 , y1~4。q=[x4,y4]
    for p in points:                        #p=[x1,y1]
        area += p[0] * q[1] - p[1] * q[0]   #x1*y4-x4*y1
        q = p                               #q=[x1,y1]  and then next p=[x2,y2]    
    return abs(area/2)                    #return |area/2|
   
'''
Ex:
polygon_area([[1,2],[3,4],[4,6],[5,7]])

'''