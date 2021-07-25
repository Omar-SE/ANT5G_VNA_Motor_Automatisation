# Autor : BOUCHENAK KHELLADI OMAR

# Ingénieur système embarqué

# bouchenak.omar6@gmail.com

from RsInstrument.RsInstrument import RsInstrument
from RsInstrument import *  # The RsInstrument package is hosted on pypi.org, see Readme.txt for more details
from time import time
import numpy as np
from RsInstrument import *  # The RsInstrument package is hosted on pypi.org, see Readme.txt for more details
from time import time
import numpy as np

from random import uniform
from pipython import GCSDevice, pitools
from pprint import pprint
# récupération data -60 degré
print('====== LOAD data -60  =======')
d1 = np.loadtxt('-60.txt')
print(d1)
# récupération de l'élement 21 et 22 à 26 GHZ
print('====== Load 21 -22  =======')
d1_26ghz = d1[20:22]
print(d1_26ghz)

# récupération data -50 degré
print('====== LOAD data -50  =======')
d2 = np.loadtxt('-50.txt')
print(d2)
# récupération de l'élement 21 et 22 à 26 GHZ
print('====== Load 21 -22  =======')
d2_26ghz = d2[20:22]
print(d2_26ghz)

# récupération data -50 degré
print('====== LOAD data -40  =======')
d3 = np.loadtxt('-40.txt')
print(d3)
# récupération de l'élement 21 et 22 à 26 GHZ
print('====== Load 21 -22  =======')
d3_26ghz = d3[20:22]
print(d3_26ghz)

print('=====BLOCK test ========')
block = np.hstack((d1_26ghz,d2_26ghz,d3_26ghz))
print(block)
np.savetxt('block.txt', block)
print('')
# ========================================================================
# ========================================================================
# ========================================================================
print('==================================     CODE 2 REPLCAE ELEMENT IN LIST')
block = ['-0.02093757', '0.05796649', '0.04455424', '0.05051775', '0.07904024', '0.01086844']
#print(block) # A,Quick,brown,fox,jumped,over,the,lazy,dog
print("liste originale : " + str(block))
#remplacement
res = [elem.replace('.', ',') for elem in block]
# print result
print("apres replaceme : " + str(res))
print('===')

#pprint(dir(block.))