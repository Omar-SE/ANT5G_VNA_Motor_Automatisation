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
## ==========================================
##                    -60
## ==========================================
# récupération data -60 degré
print('====== LOAD data -60  =======')
d1 = np.loadtxt('-60.txt')
print(d1)
# récupération de l'élement 21 et 22 à 26 GHZ
print('====== Load 21 -22  =======')
d1_26ghz = d1[20:22]
print(d1_26ghz)
## ==========================================
##                    -50
## ==========================================
# récupération data -50 degré
print('====== LOAD data -50  =======')
d2 = np.loadtxt('-50.txt')
print(d2)
# récupération de l'élement 21 et 22 à 26 GHZ
print('====== Load 21 -22  =======')
d2_26ghz = d2[20:22]
print(d2_26ghz)
## ==========================================
##                    -40
## ==========================================
# récupération data -40 degré
print('====== LOAD data -40  =======')
d3 = np.loadtxt('-40.txt')
print(d3)
# récupération de l'élement 21 et 22 à 26 GHZ
print('====== Load 21 -22  =======')
d3_26ghz = d3[20:22]
print(d3_26ghz)
## ==========================================
##                    -30
## ==========================================
# récupération data -40 degré
print('====== LOAD data -40  =======')
d4 = np.loadtxt('-30.txt')
print(d4)
# récupération de l'élement 21 et 22 à 26 GHZ
print('====== Load 21 -22  =======')
d4_26ghz = d4[20:22]
print(d4_26ghz)
## ==========================================
##                    -20
## ==========================================
# récupération data -40 degré
print('====== LOAD data -40  =======')
d5 = np.loadtxt('-20.txt')
print(d5)
# récupération de l'élement 21 et 22 à 26 GHZ
print('====== Load 21 -22  =======')
d5_26ghz = d5[20:22]
print(d5_26ghz)
## ==========================================
##                    -10
## ==========================================
# récupération data -40 degré
print('====== LOAD data -40  =======')
d6 = np.loadtxt('-10.txt')
print(d6)
# récupération de l'élement 21 et 22 à 26 GHZ
print('====== Load 21 -22  =======')
d6_26ghz = d6[20:22]
print(d6_26ghz)
## ==========================================
##                    0
## ==========================================
# récupération data -40 degré
print('====== LOAD data -40  =======')
d7 = np.loadtxt('0.txt')
print(d7)
# récupération de l'élement 21 et 22 à 26 GHZ
print('====== Load 21 -22  =======')
d7_26ghz = d7[20:22]
print(d7_26ghz)
## ==========================================
##                    10
## ==========================================
# récupération data -40 degré
print('====== LOAD data -40  =======')
d8 = np.loadtxt('+10.txt')
print(d8)
# récupération de l'élement 21 et 22 à 26 GHZ
print('====== Load 21 -22  =======')
d8_26ghz = d8[20:22]
print(d8_26ghz)
## ==========================================
##                    20
## ==========================================
# récupération data -40 degré
print('====== LOAD data -40  =======')
d9 = np.loadtxt('+20.txt')
print(d9)
# récupération de l'élement 21 et 22 à 26 GHZ
print('====== Load 21 -22  =======')
d9_26ghz = d9[20:22]
print(d9_26ghz)
## ==========================================
##                    30
## ==========================================
# récupération data -40 degré
print('====== LOAD data -40  =======')
d10 = np.loadtxt('+30.txt')
print(d10)
# récupération de l'élement 21 et 22 à 26 GHZ
print('====== Load 21 -22  =======')
d10_26ghz = d10[20:22]
print(d10_26ghz)
## ==========================================
##                    40
## ==========================================
# récupération data -40 degré
print('====== LOAD data -40  =======')
d11 = np.loadtxt('+40.txt')
print(d11)
# récupération de l'élement 21 et 22 à 26 GHZ
print('====== Load 21 -22  =======')
d11_26ghz = d11[20:22]
print(d11_26ghz)
## ==========================================
##                    50
## ==========================================
# récupération data -40 degré
print('====== LOAD data -40  =======')
d12 = np.loadtxt('+50.txt')
print(d12)
# récupération de l'élement 21 et 22 à 26 GHZ
print('====== Load 21 -22  =======')
d12_26ghz = d12[20:22]
print(d12_26ghz)
## ==========================================
##                    60
## ==========================================
# récupération data -40 degré
print('====== LOAD data -40  =======')
d13 = np.loadtxt('+60.txt')
print(d13)
# récupération de l'élement 21 et 22 à 26 GHZ
print('====== Load 21 -22  =======')
d13_26ghz = d13[20:22]
print(d13_26ghz)


print('=====BLOCK test ========')
block2 = np.hstack((d1_26ghz,d2_26ghz,d3_26ghz,d4_26ghz,d5_26ghz,d6_26ghz,d7_26ghz,d8_26ghz,d9_26ghz,d10_26ghz,d11_26ghz,d12_26ghz,d13_26ghz))
print(block2)
np.savetxt('block.txt', block2)
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
print('')
# ========================================================================
# ========================================================================
# ========================================================================
# Liste d'entiers
strList = [1, 2, 3, 4, 5]
# Combiner toutes les String de la liste
str = ' '.join(str(elem) for elem in strList)
# Afficher la liste
print(str)