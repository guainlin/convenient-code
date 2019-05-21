' Make excel '

import xlwt

book = xlwt.Workbook()
sheet1 = book.add_sheet(' xxx ')
            
sheet1.write( 0 , 0, ' sheet_name ') #in 0,0 insert name

book.save(' excel_name.xls ')                         #save excel


'Book -> sheet -> cell '
