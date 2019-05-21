'one-to-many Extend'

def one_to_many ( li_repeat_num , li_norepeat) :
    
    li_repeat = []
    li_repeat_num_new = []
    
    for i in range(len( li_repeat_num )) :
        for j in range( 0 , sum( li_repeat_num )) :
            if j+1 <= li_repeat_num[i] :
               li_repeat_num_new.append(j+1)
               li_repeat.append( li_norepeat[i] )
            else :
                break
    return( li_repeat , li_repeat_num_new )

'''
Ex:
norepeat_list = [1,2,3,4,5,6]      
repeat_list   = [1,2,2,3,4,5,5,5,6,6]
    
repeat_num    = [1,2,1,1,3,2]         


one_to_many ( repeat_num , norepeat_list)

=>
[1,2,3,4,5,6] -> [1, 2, 2, 3, 4, 5, 5, 5, 6, 6]

[1,2,1,1,3,2] -> [1, 1, 2, 1, 1, 1, 2, 3, 1, 2]

'''