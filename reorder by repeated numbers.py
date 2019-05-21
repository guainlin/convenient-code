'reorder by repeated numbers' 

def reorder( li_repeat_num , li_repeat ):
    
    li_reorder = []
    first=0
    last =0
    
    for i in li_repeat_num :
        last = first + i
        li_reorder.append( li_repeat[first:last:1] )
        first = last   
    return( li_reorder )  
    
    
    
'''
Ex:
norepeat_list = [1,2,3,4,5,6]      
repeat_list   = [1,2,2,3,4,5,5,5,6,6]
    
repeat_num    = [1,2,1,1,3,2]         


reorder( repeat_num , repeat_list)

=>
[[1], [2, 2], [3], [4], [5, 5, 5], [6, 6]]

'''