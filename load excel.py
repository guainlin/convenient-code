'load excel'

import xlrd

path = 'C:/Users/user/Desktop/Lin/'

myWorkbook = xlrd.open_workbook(path + 'xxx.xls')
mySheets = myWorkbook.sheets()[0]                

myRowValues = mySheets.row_values(0)     #get a row value

myRowValues = mySheets.col_values(0)     #get a column value
      
cell = mySheets.cell_value (0,0)         #get (0,0) cell value


'''
Ex:
    name   thing
    julia   A
    
    jazz    B
    
    jacky   C

    jerry   D
    
myRowValues = mySheets.row_values(0)    
=>
['name', 'thing']

myRowValues = mySheets.col_values(0
=>
['name', 'julia', 'jazz', 'jacky', 'jerry']

cell = mySheets.cell_value (0,0)      
=>
'name'

'''