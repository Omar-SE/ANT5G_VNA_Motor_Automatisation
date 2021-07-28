# Autor : BOUCHENAK KHELLADI OMAR

from RsInstrument.RsInstrument import RsInstrument
from RsInstrument import *  # The RsInstrument package is hosted on pypi.org, see Readme.txt for more details
from time import time
import numpy as np
from RsInstrument import *  # The RsInstrument package is hosted on pypi.org, see Readme.txt for more details
from time import time
import numpy as np

from random import uniform
from pipython import GCSDevice, pitools

#CONTROLLERNAME = 'C-863.12'
#STAGES = ('M-061.PD',)  # connect stages to axes
#REFMODE = None #('FNL',)  # reference the connected stages

from pipython import GCSDevice
gcs = GCSDevice('C-863.12')
gcs.InterfaceSetupDlg()
print('connected: {}'.format(gcs.qIDN().strip()))
#print gcs.qIDN()
axis = 1


print('===========================================================================')
print('============= TASK 1 : An ETHERNET connection is established between your PC and the ZNA instrument ...')
print('===========================================================================')
instr = None
try:
	# Adjust the VISA Resource string to fit your instrument
	instr = RsInstrument('TCPIP::169.254.202.203::INSTR', True, True) # Initializing the session
	instr.visa_timeout = 10000  # Timeout for VISA Read Operations -délai d'attente-
	# visa_timeout
	# Passé ce délai, RsInstrument lève une exception. En parlant d'exceptions,
	# une fonctionnalité importante de RsInstrument est la vérification de l'état de l'instrument.
	instr.opc_timeout = 100000  # Timeout for opc-synchronised operations
	instr.instrument_status_checking = True  # Error check after each command (fetch on désactive les erreurs == >
	instr.opc_query_after_write = True
	# opc_query_after_write = True
	#  vous pouvez envoyer le *OPC ? après chaque write_xxx()automatiquement
	# Default value after init is False

except Exception as ex:
	print('Error initializing the instrument session:\n' + ex.args[0])
	exit()

# +++++++++++++++++++++++++++++++ OPTIONS ++++++++++++++++++++++++++++++++++++++++++++
# resource_string_1 = 'TCPIP::169.254.202.203::INSTR'  # Standard LAN connection (also called VXI-11)

print('')
print('... DONE !')
print('')

print('============================================================================')
print('============= TASK 2 : Access to identification properties of ZNA instrument ...')
print('============================================================================')
print(f'Driver Version: {instr.driver_version}')
print(f'SpecAn IDN: {instr.idn_string}')
print(f'visa_manufacturer: {instr.visa_manufacturer}')
print(f'full_instrument_model_name: {instr.full_instrument_model_name}')
print(f'instrument_serial_number: {instr.instrument_serial_number}')
print(f'firmware_version: {instr.instrument_firmware_version}')
print(f'instrument_options: List: {instr.instrument_options}')
print(f'opc_timeout: {instr.opc_timeout}')
print(f'visa_timeout: {instr.visa_timeout}')
print(f'SpecAn Options: {",".join(instr.instrument_options)}')
print('')
print('... DONE !')
print('')

print('===========================================================================')
print('============= TASK 3 : Configuration of Parameters ... ')
print('===========================================================================')
instr.clear_status() # Pour effacer toutes les erreurs du sous-système d'état de l'instrument
instr.write_str('*RST')
instr.write_str('FREQ:STARt 24 GHZ')
instr.write_str('FREQ:STOP  28 GHZ')
instr.write_str('DISP:WIND:TRAC:Y:RLEV 0.0')       #  the Reference Level
instr.write_str('BAND 1 kHz')                       #  the RBW
instr.write_str('SYSTEM:DISPLAY:UPDATE ON')
instr.query_opc()

# +++++++++++++++++++++++++++++++ OPTIONS ++++++++++++++++++++++++++++++++++++++++++++
#instr.reset()
#instr.write_str('INITiate1:CONTinuous ON')
#instr.write_str('INIT1:CONT OFF')  # Switch OFF the continuous sweep (Aucun signal sur la figure) **************************
#instr.write_str('SYST:DISP:UPD ON')
#instr.write_str('SENSe1:FREQuency:STARt 1 GHz; STOP 5.5 GHz')               #  the center frequency
#instr.write_str('FREQ:CENT 28.0 GHz')
#instr.write_str('FREQ:SPAN 100 MHz')                #  the span
#instr.write_str_with_opc('INIT:IMM:DUMM')

print('')
print('... DONE !')
print('')

instr.VisaTimeout = 10000  # Sweep timeout - set it higher than the instrument acquisition time
#instr.write_str_with_opc('INIT1')
instr.write_str_with_opc('INIT1', 50000)


print('===========================================================================')
print('============= TASK 4 : S - Parameters ... ')
print('===========================================================================')
#instr.write_str('CALCULATE1:PARAMETER:SDEFINE "Trc_1","B2/A1"')   # Query ascii array of floats# calculation of parameter ==> B2/A1
#instr.write_str('CALCULATE1:PARAMETER:SDEFINE "Trc_2","A2/A1"')   # calculation of parameter ==> A2/A1
#instr.write_str('CALCULATE1:PARAMETER:SDEFINE "Trc_3","S11"')     # calculation of parameter ==> S11
#instr.write_str('CALCULATE1:PARAMETER:SDEFINE "Trc_4","S22"')     # calculation of parameter ==> S21

#start = time()

t = time() # Start Time
#instr.write_str('DISPLAY:WINDOW1:TRACE1:DELETE')
#instr.write_str_with_opc('SWE:POIN 20') # nombre d'échantillon
#instr.write_str_with_opc('CALC1:PAR:SDEF "Ch1Tr1", "A2/A1"') # calcul parametre S= B2/A1, nom : Ch1Tr1
#instr.write_str_with_opc('CALC1:FORM  MLOGarithmic; :DISP:WIND:TRAC2:FEED "Ch1Tr1"') # Afiichage fig; format : phase;
#instr.write_str_with_opc('CALC1:PAR:SDEF "Ch1Tr2", "B2/A1"') # calcul parametre S= B2/A1, nom : Ch1Tr1
#instr.write_str_with_opc('CALC1:FORM  MLOGarithmic; :DISP:WIND:TRAC3:FEED "Ch1Tr2"') # Afiichage fig; format : phase

instr.write_str('DISPLAY:WINDOW1:TRACE1:DELETE')
instr.query_opc()
instr.write_str_with_opc('SOURce1:PATH1:DIRectaccess B16')
instr.query_opc()
instr.write_str_with_opc('SOURce1:PATH2:DIRectaccess B16')
instr.query_opc()

instr.write_str('DISP:WIND1:STAT ON')
instr.query_opc()

instr.write_str_with_opc('SWE:POIN 21') # nombre d'échantillon
instr.query_opc()

# ====== "Ch1Tr1", "B2/A1D1" (PORT 1) ..... en dB
instr.write_str_with_opc('CALC1:PAR:SDEF "Ch1Tr1", "B2/A1D1"') # calcul parametre S= B2/A1, nom : Ch1Tr1
instr.write_str_with_opc('CALC1:FORM  MLOGarithmic; :DISP:WIND1:TRAC2:FEED "Ch1Tr1"') # Afiichage fig; format : phase;
#instr.write_str_with_opc('CALC1:FORM  PHASe; :DISP:WIND:TRAC2:FEED "Ch1Tr1"')
#instr.write_str_with_op('SWE:AXIS:FREQ ' Port 1; Source'')
instr.query_opc()
# ===== "Ch1Tr2", "B2D2/A2D2" (PORT 2) ..... en dB
instr.write_str_with_opc('CALC2:PAR:SDEF "Ch1Tr2","B2D2/A2D2"') # calcul parametre S= B2/A1, nom : Ch1Tr1
instr.write_str_with_opc('CALC2:FORM  MLOGarithmic; :DISP:WIND1:TRAC3:FEED "Ch1Tr2"') # Afiichage fig; format : phase
#instr.write_str_with_opc('CALC1:FORM  PHASe; :DISP:WIND:TRAC3:FEED "Ch1Tr2"')
instr.query_opc()

# ********************************************
# MOVE 1 - 0
# ********************************************
print('============ MOVING TO RIGHT ...°')
gcs.SVO (axis, 1) # Turn on servo control of axis "A"
#gcs.REF("axis") # Réference
REFMODE = ('FNL',1)
#gcs.MVR(axis, -80.0)
#pitools.waitontarget(gcs, axis)
gcs.MVR(axis, 20.0)
pitools.waitontarget(gcs, axis)
print('MOVE 1 ...... -60.0°')
#  ==================================>  trace 1
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace1 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('-60A.txt', trace1)
print(trace1)
#  ==================================>  trace 2
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace2 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('-60B.txt', trace2)
print(trace2)

# ********************************************
# MOVE 2 - 3
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 3.0)
pitools.waitontarget(gcs, axis)
print('MOVE 2 ...... -50°')
#  ==================================>  trace 3
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace3 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('-57A.txt', trace3)
print(trace3)
#  ==================================>  trace 4
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace4= instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
#pitools.waitontarget(gcs, axis)
np.savetxt('-57B.txt', trace4)
print(trace4)
# ********************************************
# MOVE 3 - 6
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 3.0)
pitools.waitontarget(gcs, axis)
print('MOVE 3 ...... -40°')
#  ==================================>  trace 5
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace5 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('-54A.txt', trace5)
print(trace5)
#  ==================================>  trace 6
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace6 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('-54B.txt', trace6)
print(trace6)

# ********************************************
# MOVE 4 - 9
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 3.0)
pitools.waitontarget(gcs, axis)
print('MOVE 4 ...... -30°')
#  ==================================>  trace 7
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace7 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('-51A.txt', trace7)
print(trace7)
#  ==================================>  trace 8
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace8 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('-51B.txt', trace8)
print(trace8)

# ********************************************
# MOVE 5 12
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 3.0)
pitools.waitontarget(gcs, axis)
print('MOVE 5 ...... -20°')
#  ==================================>  trace 9
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace9 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('-48A.txt', trace9)
print(trace9)
#  ==================================>  trace 10
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace10 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('-48B.txt', trace10)
print(trace10)

# ********************************************
# MOVE 6     15
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 3.0)
pitools.waitontarget(gcs, axis)
print('MOVE 6 ...... -10°')
#  ==================================>  trace 11
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace11 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('-45A.txt', trace11)
print(trace11)
#  ==================================>  trace 12
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace12 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('-45B.txt', trace12)
print(trace12)

# ********************************************
# MOVE 7 -  18
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 3.0)
pitools.waitontarget(gcs, axis)
print('MOVE 7 ...... 0° (Référence)')
#  ==================================>  trace 13
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace13 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('-42A.txt', trace13)
print(trace13)
#  ==================================>  trace 14
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace14 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('-42B.txt', trace14)
print(trace14)

# ********************************************
# MOVE 8 - 21
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 3.0)
pitools.waitontarget(gcs, axis)
print('MOVE 8 ...... + 10°')
#  ==================================>  trace 15
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace15 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('-39A.txt', trace15)
print(trace15)
#  ==================================>  trace 16
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace16 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('-39B.txt', trace16)
print(trace16)

# ********************************************
# MOVE 9 - 24
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 3.0)
pitools.waitontarget(gcs, axis)
print('MOVE 9 ...... + 20°')
#  ==================================>  trace 17
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace17 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('-36A.txt', trace17)
print(trace17)
#  ==================================>  trace 18
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace18 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('-36B.txt', trace18)
print(trace18)

# ********************************************
# MOVE 10 - 27
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 3.0)
pitools.waitontarget(gcs, axis)
print('MOVE 9 ...... + 30°')
#  ==================================>  trace 19
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace19 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('-33A.txt', trace19)
print(trace19)
#  ==================================>  trace 20
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace20 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('-33B.txt', trace20)
print(trace20)

# ********************************************
# MOVE 11     30 °
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 3.0)
pitools.waitontarget(gcs, axis)
print('MOVE 9 ...... + 40°')
#  ==================================>  trace 21
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace21 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('-30A.txt', trace21)
print(trace21)
#  ==================================>  trace 22
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace22 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('-30B.txt', trace22)
print(trace22)

# ********************************************
# MOVE 12      33 °
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 3.0)
pitools.waitontarget(gcs, axis)
print('MOVE 9 ...... + 50°')
#  ==================================>  trace 23
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace23 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('-27A.txt', trace23)
print(trace23)
#  ==================================>  trace 24
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace24 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('-27B.txt', trace24)
print(trace24)

# ********************************************
# MOVE 13      36 °
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 3.0)
pitools.waitontarget(gcs, axis)
print('MOVE 9 ...... + 60°')
#  ==================================>  trace 25
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace25 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('-24A.txt', trace25)
print(trace25)
#  ==================================>  trace 26
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace26 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('-24B.txt', trace26)
print(trace26)


# ********************************************
# MOVE 14      39 °                             ============== NEW MOV  27 - 28
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 3.0)
pitools.waitontarget(gcs, axis)
print('MOVE 9 ...... + 60°')
#  ==================================>  trace 27
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace27 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('-21A.txt', trace27)
#print(trace25)
#  ==================================>  trace 28
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace28 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('-21B.txt', trace28)
#print(trace26)

# ********************************************
# MOVE 13      42 °
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 3.0)
pitools.waitontarget(gcs, axis)
print('MOVE 9 ...... + 60°')
#  ==================================>  trace 25
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace29 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('-18A.txt', trace29)
#print(trace25)
#  ==================================>  trace 26
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace30 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('-18B.txt', trace30)
#print(trace26)

# ********************************************
# MOVE 13      45 °
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 3.0)
pitools.waitontarget(gcs, axis)
print('MOVE 9 ...... + 60°')
#  ==================================>  trace 25
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace31 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('-15A.txt', trace31)
#print(trace25)
#  ==================================>  trace 26
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace32 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('-15B.txt', trace32)
#print(trace26)


# ********************************************
# MOVE 13      48 °
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 3.0)
pitools.waitontarget(gcs, axis)
print('MOVE 9 ...... + 60°')
#  ==================================>  trace 25
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace33 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('-12A.txt', trace33)
#print(trace25)
#  ==================================>  trace 26
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace34 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('-12B.txt', trace34)
#print(trace26)

# ********************************************
# MOVE 13      51 °
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 3.0)
pitools.waitontarget(gcs, axis)
print('MOVE 9 ...... + 60°')
#  ==================================>  trace 25
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace35 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('-9A.txt', trace35)
#print(trace25)
#  ==================================>  trace 26
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace36 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('-9B.txt', trace36)
#print(trace26)

# ********************************************
# MOVE 13      54
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 3.0)
pitools.waitontarget(gcs, axis)
print('MOVE 9 ...... + 60°')
#  ==================================>  trace 25
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace37 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('-6A.txt', trace37)
#print(trace25)
#  ==================================>  trace 26
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace38 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('-6B.txt', trace38)
#print(trace26)

# ********************************************
# MOVE 13      57
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 3.0)
pitools.waitontarget(gcs, axis)
print('MOVE 9 ...... + 60°')
#  ==================================>  trace 39
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace39 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('-3A.txt', trace39)
#print(trace25)
#  ==================================>  trace 40
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace40 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('3B.txt', trace40)
#print(trace26)

# ******************************************** =================================
# MOVE 13      60  °                           ====================== REF 0 Degré
# ******************************************** =================================
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 3.0)
pitools.waitontarget(gcs, axis)
print('MOVE 9 ...... + 60°')
#  ==================================>  trace 25
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace41 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('0a.txt', trace41)
#print(trace25)
#  ==================================>  trace 26
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace42 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('0b.txt', trace42)
#print(trace26)

# ********************************************
# MOVE 13      63  °
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 3.0)
pitools.waitontarget(gcs, axis)
print('MOVE 9 ...... + 60°')
#  ==================================>  trace 25
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace43 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('+3A.txt', trace43)
#print(trace25)
#  ==================================>  trace 26
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace44 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('+3B.txt', trace44)
#print(trace26)

# ********************************************
# MOVE 13      66 °
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 3.0)
pitools.waitontarget(gcs, axis)
print('MOVE 9 ...... + 60°')
#  ==================================>  trace 25
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace45 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('+6A.txt', trace45)
#print(trace25)
#  ==================================>  trace 26
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace46 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('+6B.txt', trace46)
#print(trace26)

# ********************************************
# MOVE 13      69 °
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 3.0)
pitools.waitontarget(gcs, axis)
print('MOVE 9 ...... + 60°')
#  ==================================>  trace 25
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace47 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('+9A.txt', trace47)
#print(trace25)
#  ==================================>  trace 26
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace48 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('+9B.txt', trace48)
#print(trace26)

# ********************************************
# MOVE 13      72 °
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 3.0)
pitools.waitontarget(gcs, axis)
print('MOVE 9 ...... + 60°')
#  ==================================>  trace 25
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace49 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('+12A.txt', trace49)
#print(trace25)
#  ==================================>  trace 26
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace50 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('+12B.txt', trace50)
#print(trace26)

# ********************************************
# MOVE 13      75 °
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 3.0)
pitools.waitontarget(gcs, axis)
print('MOVE 9 ...... + 60°')
#  ==================================>  trace 25
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace51 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('+15A.txt', trace51)
#print(trace25)
#  ==================================>  trace 26
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace52 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('+15B.txt', trace52)
#print(trace26)

# ********************************************
# MOVE 13      78 °
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 3.0)
pitools.waitontarget(gcs, axis)
print('MOVE 9 ...... + 60°')
#  ==================================>  trace 25
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace53 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('+18A.txt', trace53)
#print(trace25)
#  ==================================>  trace 26
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace54 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('+18B.txt', trace54)
#print(trace26)

# ********************************************
# MOVE 13      81 °
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 3.0)
pitools.waitontarget(gcs, axis)
print('MOVE 9 ...... + 60°')
#  ==================================>  trace 25
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace55 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('+21A.txt', trace55)
#print(trace25)
#  ==================================>  trace 26
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace56 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('+21B.txt', trace56)
#print(trace26)

# ********************************************
# MOVE 13      84 °
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 3.0)
pitools.waitontarget(gcs, axis)
print('MOVE 9 ...... + 60°')
#  ==================================>  trace 25
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace57 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('+24A.txt', trace57)
#print(trace25)
#  ==================================>  trace 26
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace58 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('+24B.txt', trace58)
#print(trace26)

# ********************************************
# MOVE 13      87 °
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 3.0)
pitools.waitontarget(gcs, axis)
print('MOVE 9 ...... + 60°')
#  ==================================>  trace 25
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace59 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('+27A.txt', trace59)
#print(trace25)
#  ==================================>  trace 26
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace60 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('+27B.txt', trace60)
#print(trace26)

# ********************************************
# MOVE 13      90 °
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 3.0)
pitools.waitontarget(gcs, axis)
print('MOVE 9 ...... + 60°')
#  ==================================>  trace 25
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace61 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('+30A.txt', trace61)
#print(trace25)
#  ==================================>  trace 26
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace62 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('+30B.txt', trace62)
#print(trace26)

# ********************************************
# MOVE 13      93 °                         ******************************
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 3.0)
pitools.waitontarget(gcs, axis)
print('MOVE 9 ...... + 60°')
#  ==================================>  trace 25
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace63 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('+33A.txt', trace63)
#print(trace25)
#  ==================================>  trace 26
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace64 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('+33B.txt', trace64)
#print(trace26)

# ********************************************
# MOVE 13      96 °
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 3.0)
pitools.waitontarget(gcs, axis)
print('MOVE 9 ...... + 60°')
#  ==================================>  trace 25
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace65 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('+36A.txt', trace65)
#print(trace25)
#  ==================================>  trace 26
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace66 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('+36B.txt', trace66)
#print(trace26)

# ********************************************
# MOVE 13      99 °
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 3.0)
pitools.waitontarget(gcs, axis)
print('MOVE 9 ...... + 60°')
#  ==================================>  trace 25
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace67 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('+39A.txt', trace67)
#print(trace25)
#  ==================================>  trace 26
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace68 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('+39B.txt', trace68)
#print(trace26)

# ********************************************
# MOVE 13      102 °
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 3.0)
pitools.waitontarget(gcs, axis)
print('MOVE 9 ...... + 60°')
#  ==================================>  trace 25
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace69 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('+42A.txt', trace69)
#print(trace25)
#  ==================================>  trace 26
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace70 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('+42A.txt', trace70)
#print(trace26)

# ********************************************
# MOVE 13      105 °
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 3.0)
pitools.waitontarget(gcs, axis)
print('MOVE 9 ...... + 60°')
#  ==================================>  trace 25
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace71 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('+45A.txt', trace71)
#print(trace25)
#  ==================================>  trace 26
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace72 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('+45B.txt', trace72)
#print(trace26)

# ********************************************
# MOVE 13      108 °
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 3.0)
pitools.waitontarget(gcs, axis)
print('MOVE 9 ...... + 60°')
#  ==================================>  trace 25
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace73 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('+48A.txt', trace73)
#print(trace25)
#  ==================================>  trace 26
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace74 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('+48B.txt', trace74)
#print(trace26)

# ********************************************
# MOVE 13      111 °
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 3.0)
pitools.waitontarget(gcs, axis)
print('MOVE 9 ...... + 60°')
#  ==================================>  trace 25
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace75 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('+51A.txt', trace75)
#print(trace25)
#  ==================================>  trace 26
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace76 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('+51B.txt', trace76)
#print(trace26)

# ********************************************
# MOVE 13      114 °
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 3.0)
pitools.waitontarget(gcs, axis)
print('MOVE 9 ...... + 60°')
#  ==================================>  trace 25
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace77 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('+54A.txt', trace77)
#print(trace25)
#  ==================================>  trace 26
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace78 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('+54B.txt', trace78)
#print(trace26)

# ********************************************
# MOVE 13      117 °
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 3.0)
pitools.waitontarget(gcs, axis)
print('MOVE 9 ...... + 60°')
#  ==================================>  trace 25
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace79 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('+57A.txt', trace79)
#print(trace25)
#  ==================================>  trace 26
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace80 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('+57B.txt', trace80)
#print(trace26)

# ********************************************
# MOVE 13      120 °                                ++++++++++++++++ FIN MOV
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 3.0)
pitools.waitontarget(gcs, axis)
print('MOVE 9 ...... + 60°')
#  ==================================>  trace 25
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace81 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('+60A.txt', trace81)
#print(trace25)
#  ==================================>  trace 26
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace82 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('-60B.txt', trace82)
#print(trace26)

# ********************************************
# MOVE 14      - 60 retour a 0 REF
# ********************************************
print('============ MOVING TO RIGHT ...°')
gcs.SVO (axis, 1) # Turn on servo control of axis "A"
#gcs.REF("axis") # Réference
gcs.MVR(axis, -60.0)
pitools.waitontarget(gcs, axis)
print('MOVE 1 ...... - 60.0°')
#instr.write_str('DISP:WIND1:STAT ON')
#instr.write_str('DISP:WIND3:STAT ON')
#instr.write_str('DISP:WIND4:STAT ON')
#instr.write_str('DISPLAY:WINDOW1:TRACE2:FEED "Ch4Tr1"')
#instr.write_str('DISPLAY:WINDOW2:TRACE2:FEED "Ch4Tr1"')
#instr.write_str('DISPLAY:WINDOW3:TRACE2:FEED "Ch4Tr1"')
#instr.write_str('DISPLAY:WINDOW4:TRACE2:FEED "Ch4Tr1"')

#instr.write_str('DISPLAY:WINDOW1:TRACE2:FEED "Trc_1"')            # display Trc_1 ==> B2/A1
#instr.write_str('DISPLAY:WINDOW1:TRACE3:FEED "Trc_2"')            # display Trc_2 ==> A2/A1
#instr.write_str('DISPLAY:WINDOW1:TRACE4:FEED "Trc_3"')            # display Trc_3 ==> S11
#instr.write_str('DISPLAY:WINDOW1:TRACE5:FEED "Trc_4"')            # display Trc_4 ==> S21

#instr.write_str('DISPLAY:WINDOW1:TRACE1:DELETE')
#instr.write_str('DISPLAY:WINDOW1:TRACE2:DELETE')
#instr.write_str('DISPLAY:WINDOW1:TRACE3:DELETE')
#instr.write_str('DISPLAY:WINDOW1:TRACE4:DELETE')
#instr.write_str('DISPLAY:WINDOW1:TRACE5:DELETE')

print('')
print('... DONE ! ')
print('')
print('====== Load 21 -22  =======')
d1 = trace1[20:22]
d2 = trace2[20:22]
d3 = trace3[20:22]
d4 = trace4[20:22]
d5 = trace5[20:22]
d6 = trace6[20:22]
d7 = trace7[20:22]
d8 = trace8[20:22]
d9 = trace9[20:22]
d10 = trace10[20:22]

d11 = trace11[20:22]
d12 = trace12[20:22]
d13 = trace13[20:22]
d14 = trace14[20:22]
d15 = trace15[20:22]
d16 = trace16[20:22]
d17 = trace17[20:22]
d18 = trace18[20:22]
d19 = trace19[20:22]
d20 = trace20[20:22]

d21 = trace21[20:22]
d22 = trace22[20:22]
d23 = trace23[20:22]
d24 = trace24[20:22]
d25 = trace25[20:22]
d26 = trace26[20:22]
d27 = trace27[20:22]
d28 = trace28[20:22]
d29 = trace29[20:22]
d30 = trace30[20:22]

d31 = trace31[20:22]
d32 = trace32[20:22]
d33 = trace33[20:22]
d34 = trace34[20:22]
d35 = trace35[20:22]
d36 = trace36[20:22]
d37 = trace37[20:22]
d38 = trace38[20:22]
d39 = trace39[20:22]
d40 = trace40[20:22]

d41 = trace41[20:22]
d42 = trace42[20:22]
d43 = trace43[20:22]
d44 = trace44[20:22]
d45 = trace45[20:22]
d46 = trace46[20:22]
d47 = trace47[20:22]
d48 = trace48[20:22]
d49 = trace49[20:22]
d50 = trace50[20:22]

d51 = trace51[20:22]
d52 = trace52[20:22]
d53 = trace53[20:22]
d54 = trace54[20:22]
d55 = trace55[20:22]
d56 = trace56[20:22]
d57 = trace57[20:22]
d58 = trace58[20:22]
d59 = trace59[20:22]
d60 = trace60[20:22]

d61 = trace61[20:22]
d62 = trace62[20:22]
d63 = trace63[20:22]
d64 = trace64[20:22]
d65 = trace65[20:22]
d66 = trace66[20:22]
d67 = trace67[20:22]
d68 = trace68[20:22]
d69 = trace69[20:22]
d70 = trace70[20:22]

d71 = trace71[20:22]
d72 = trace72[20:22]
d73 = trace73[20:22]
d74 = trace74[20:22]
d75 = trace75[20:22]
d76 = trace76[20:22]
d77 = trace77[20:22]
d78 = trace78[20:22]
d79 = trace79[20:22]
d80 = trace80[20:22]

d81 = trace81[20:22]
d82 = trace82[20:22]

print('=====BLOCK 26 GHz========')
blockA = np.hstack((d1,d3,d5,d7,d9,d11,d13,d15,d17,d19,d21,d23,d25,d27,d29,d31,d33,d35,d37,d39,d41,d43,d45,d47,d49,d51,d53,d55,d57,d59,d61,d63,d65,d67,d69,d71,d73,d75,d77,d79,d81))
print(blockA)
np.savetxt('blockA.txt', blockA)
print('')
blockB = np.hstack((d2,d4,d6,d8,d10,d12,d14,d16,d18,d20,d22,d24,d26,d28,d30,d32,d34,d36,d38,d40,d42,d44,d46,d48,d50,d52,d54,d56,d58,d60,d62,d64,d66,d68,d70,d72,d74,d76,d78,d80,d82))
print(blockB)
np.savetxt('blockB.txt', blockB)
print('')
# ========================================================================
# ========================================================================
# ========================================================================



print('===========================================================================')
print('============= TASK 5 - 1 : Traces ASCII ... ')
print('===========================================================================')
#start = time()
#t = time()
#instr.write_str('SWE:POIN 10')
#trace = instr.query_bin_or_ascii_float_list_with_opc('FORM ASC;:TRAC? CH1DATA')
#print(f'Instrument returned {len(trace)} points in the ascii trace, query duration {time() - t:.3f} secs')
#np.savetxt('test.txt', trace)
#instr.query_opc()
#print(f'Measured samples #{len(trace)}\nValues:\n{trace}')
print('')

print('===========================================================================')
print('============= TASK 5 - 1 : Traces BINARY ... ')
print('===========================================================================')
#t = time()
#instr.write_str('SWE:POIN 10')
#instr.bin_float_numbers_format = BinFloatFormat.Double_8bytes_swapped # This tells the driver in which format to expect the binary float data
#trace = instr.query_bin_or_ascii_float_list_with_opc('FORM REAL,32;:TRAC? CH1DATA')  # Query binary array of floats - the query function is the same as for the ASCII format
#print(trace)
#print(f'Instrument returned {len(trace)} points in the binary trace, query duration {time() - t:.3f} secs')
print('')

# +++++++++++++++++++++++++++++++ OPTIONS ++++++++++++++++++++++++++++++++++++++++++++
#instr.write_str('SENSe1:SWEep:TIME:AUTO ON')
#instr.write_str('TRIGger1:SEQuence:SOURce IMMediate')
#np.savetxt('test2.txt', trace, fmt='%i')

print('===========================================================================')
print('============= TASK 6 : MARKER ... ')
print('===========================================================================')
instr.write_str_with_opc('CALC1:MARK1:FUNC:DOM:USER 1')
instr.write_str_with_opc('CALCulate1:MARKer1:STATe ON') # Set the marker to the maximum point of the entire trace, wait for it to be set#markerX = instr.query_float('CALC1:MARK1:X?')
instr.write_str_with_opc('CALCulate1:MARKer2:STATe ON')
markerX = instr.query_float('CALC1:MARK1:X?')
markerY = instr.query_float('CALC1:MARK1:Y?')
print(f'Marker Frequency {markerX:.2f} Hz, Level {markerY:.3f} dBm')
print('')

# +++++++++++++++++++++++++++++++ OPTIONS ++++++++++++++++++++++++++++++++++++++++++++
#// Remove all markers and define a limit line for the active trace.
#instr.write_str_with_opc('CALCulate1:MARKer1:AOFF')

print('===========================================================================')
print('============= TASK 7 : Screenshot / Transfert File to PC ... ')
print('===========================================================================')
#instr.write_str_with_opc("HCOP:DEV:LANG BMP")
#instr.query_opc()
#instr.write_str_with_opc(r"MMEM:NAME 'c:\Users\Instrument\Desktop\p4.BMP'")
#instr.query_opc()
#instr.write_str_with_opc("HCOP:IMM")# Faire un screenshot
#instr.query_opc()  # Wait ...
#instr.read_file_from_instrument_to_pc(r'c:\Users\Instrument\Desktop\p4.BMP', r'c:\Temp\p7.BMP')  # Transfer the instrument file to the PC
#print(r" ===> Instrument screenshot saved to PC 'c:\Temp\p7.BMP'")
#instr.query_opc()

instr.write_str('HCOP:DEV:LANG JPG')
#instr.query_opc()
instr.write_str(r"MMEM:NAME 'c:\temp\Dev_Screenshot.png'")
#instr.write_str("MMEM:NAME 'c:Users\Instrument\Desktop\PLOT1.JPG'")
instr.query_opc()
#instr.write_str("HCOP:IMM")
#instr.write_str("HCOP:ITEM:ALL")
instr.write_str_with_opc('HCOP:IMM')
#instr.write_str_with_opc("HCOP:IMM")# Faire un screenshot
#instr.write_str_with_opc("HCOP:DEST 'MMEM'; :HCOP")# Faire un screenshot
instr.query_opc()  # Wait ...
instr.read_file_from_instrument_to_pc(r"c:\temp\Dev_Screenshot.png", r"c:\Temp\PC_Screenshot_4deg.png")
#instr.read_file_from_instrument_to_pc(r"c:\temp\Dev_Screenshot.png", r"c:\Temp\PLOT1.JPG")  # Transfer the instrument file to the PC
instr.query_opc()
print(r" ===> Instrument screenshot saved to PC 'c:\Temp\t1.BMP'")
instr.query_opc()
# +++++++++++++++++++++++++++++++ OPTIONS ++++++++++++++++++++++++++++++++++++++++++++
#instr.write_str("HCOP:ITEM:ALL")

print('')
print('... DONE ! ')
print('')

# Display ERRORS
#errors_list = instr.query_all_errors()
#print('===> List of errors : ')
#print(errors_list)

print('')
print('*************************************** ')
print('******** End of the program ! ********* ')
print('*************************************** ')

#instr.write_str('SYSTem:ERRor:DISPlay:REMote ON')

# Close the session
instr.close()


