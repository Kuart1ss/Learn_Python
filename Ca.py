#!/usr/bin/env python
# -*- coding:utf-8 -*-
import  sys

while 1:
 UserIntention = input('If you want to continue,press y and enter.'
                       '\nFor help,press h and enter.'
                       '\nIf not,press any other key and enter.')
 if UserIntention == 'y':
      FirNum = float(input('The First Number:'))
      SecNum = float(input('The Second Number:'))
      WhatDoYouWantToDo = input('You want to...(Add/Min/Mult/Div/Inv):')

      if WhatDoYouWantToDo == 'Add':
         print(FirNum, '+', SecNum, '=', FirNum + SecNum)
      elif WhatDoYouWantToDo == 'Min':
         print(FirNum, '-', SecNum, '=', FirNum - SecNum)
      elif WhatDoYouWantToDo == 'Mult':
         print(FirNum, 'x', SecNum, '=', FirNum * SecNum)
      elif WhatDoYouWantToDo == 'Div':
         print(FirNum, '/', SecNum, '=', FirNum / SecNum)
      elif WhatDoYouWantToDo == 'Inv':
         print(FirNum, '^', SecNum, '=', FirNum ** SecNum)
      else:
         print('ERROR!\nCOMMAND NOT FIND!\nPlease Enter true command.')
 elif UserIntention == 'h':
     print('When the program shows "The First Number",enter the nums what is in front of the equation.'
           '\nWhen the program shows "The Second Number",enter the nums what is behind of the equation.\n'
           'And now enter the operation type(Add/Min/Mult/Div/Inv),enter,you can get it on your screen.')
 else:
   print('The program is shutdown.')
   break