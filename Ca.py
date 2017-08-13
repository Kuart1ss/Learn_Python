#!/usr/bin/env python
# -*- coding:utf-8 -*-
import  sys

while 1:
 UserIntention = input('If you want to continue,press y and enter.'
                       '\nFor help,press h and enter.'
                       '\nIf not,press any other key and enter.')
 if UserIntention == 'y':
      FirNum = int(input('The First Number:'))
      SecNum = int(input('The Second Number:'))
      WhatDoYouWantToDo = input('You want to...(Add/Min/Mult/Div/Inv):')

      if WhatDoYouWantToDo == 'Add':
         NowAnswer = FirNum + SecNum
         print(FirNum, '+', SecNum, '=', NowAnswer)
      elif WhatDoYouWantToDo == 'Min':
         NowAnswer = FirNum - SecNum
         print(FirNum, '-', SecNum, '=', NowAnswer)
      elif WhatDoYouWantToDo == 'Mult':
         NowAnswer = FirNum * SecNum
         print(FirNum, 'x', SecNum, '=', NowAnswer)
      elif WhatDoYouWantToDo == 'Div':
         NowAnswer = FirNum / SecNum
         print(FirNum, '/', SecNum, '=', NowAnswer)
      elif WhatDoYouWantToDo == 'Inv':
         NowAnswer = FirNum ** SecNum
         print(FirNum, '^', SecNum, '=', NowAnswer)
      else:
         print('ERROR!\nCOMMAND NOT FIND!\nPlease Enter true command.')
 elif UserIntention == 'h':
     print('When the program shows "The First Number",enter the nums what is in front of the equation.'
           '\nWhen the program shows "The Second Number",enter the nums what is behind of the equation.\n'
           'And now enter the operation type(Add/Min/Mult/Div/Inv),enter,you can get it on your screen.')
 else:
   print('The program is shutdown.')
   break