'many-to-one   Subtractoin'


def many_to_one ( li_repeat , int_correct_position ): 
    error = 0
    for i in li_repeat:
        int_correct_position = int_correct_position -i
        error += 1
        if int_correct_position <= 0 :
            break 
    return ( error )

'''
Ex:
    
norepeat_list = [1,2,3,4,5,6]      
repeat_list   = [1,2,2,3,4,5,5,5,6,6]
    
repeat_num    = [1,2,1,1,3,2]         


want to get repeat_list[5] number in norepeat_list  

=>

a[ many_to_one( repeat_num , repeat_list[5]) ]
=>
5

'''