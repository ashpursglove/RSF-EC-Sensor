


import time

p = 0 # loop hold
h = 0 #star roll timer

from gubbins.rsf import nameplate
while p == 0:
    print('\n'*100)
    nameplate()
    time.sleep(1)
    p +=1
    
from gubbins.look import look    
while p == 1:
    look()
    p +=1
    
from gubbins.return_acando import return_data
from gubbins.decor import me,top,bottom
while p==2:
    
    print('\n'*100)
    print(me())
    print(top(h))
    print('Conductivity = {}Oxygen Sensor Removed'.format(return_data()))
    print('Death Ray Removed')
    print(top(h))
    time.sleep(1)
    if(h<29):
        h+=1
    else:
        h=0



