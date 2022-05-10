#
# txt
#

import random as r

fh = open('3numeros.txt', 'wt')
for k in range(6):
    fh.write(str(r.random())+'\n')    

fh.close()

print('done...')
