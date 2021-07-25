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
instr.write_str_with_opc('SOURce1:PATH1:DIRectaccess B16')
instr.write_str_with_opc('SOURce1:PATH2:DIRectaccess B16')

instr.write_str('DISP:WIND1:STAT ON')

instr.write_str_with_opc('SWE:POIN 21') # nombre d'échantillon

# ====== "Ch1Tr1", "B2/A1D1" (PORT 1) ..... en dB
instr.write_str_with_opc('CALC1:PAR:SDEF "Ch1Tr1", "B2/A1D1"') # calcul parametre S= B2/A1, nom : Ch1Tr1
instr.write_str_with_opc('CALC1:FORM  MLOGarithmic; :DISP:WIND1:TRAC2:FEED "Ch1Tr1"') # Afiichage fig; format : phase;
#instr.write_str_with_opc('CALC1:FORM  PHASe; :DISP:WIND:TRAC2:FEED "Ch1Tr1"')
#instr.write_str_with_op('SWE:AXIS:FREQ ' Port 1; Source'')

# ===== "Ch1Tr2", "B2D2/A2D2" (PORT 2) ..... en dB
instr.write_str_with_opc('CALC2:PAR:SDEF "Ch1Tr2","B2D2/A2D2"') # calcul parametre S= B2/A1, nom : Ch1Tr1
instr.write_str_with_opc('CALC2:FORM  MLOGarithmic; :DISP:WIND1:TRAC3:FEED "Ch1Tr2"') # Afiichage fig; format : phase
#instr.write_str_with_opc('CALC1:FORM  PHASe; :DISP:WIND:TRAC3:FEED "Ch1Tr2"')


# ********************************************
# MOVE 1
# ********************************************
print('============ MOVING TO RIGHT ...°')
gcs.SVO (axis, 1) # Turn on servo control of axis "A"
#gcs.REF("axis") # Réference
REFMODE = ('FNL',1)
#gcs.MVR(axis, -60.0)
pitools.waitontarget(gcs, axis)
print('MOVE 1 ...... -60.0°')
#  ==================================>  trace 1
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace1 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('trac_A2_-60deg.txt', trace1)
print(trace1)
#  ==================================>  trace 2
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace2 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('trac_B2_-60deg.txt', trace2)
print(trace2)


# ********************************************
# MOVE 2
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 10.0)
pitools.waitontarget(gcs, axis)
print('MOVE 2 ...... -50°')
#  ==================================>  trace 3
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace3 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('trac_A2_-50deg.txt', trace3)
print(trace3)
#  ==================================>  trace 4
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace4= instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('trac_B2_-50deg.txt', trace4)
print(trace4)
# ********************************************
# MOVE 3
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 10.0)
pitools.waitontarget(gcs, axis)
print('MOVE 3 ...... -40°')
#  ==================================>  trace 5
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace5 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('trac_A2_-40deg.txt', trace5)
print(trace5)
#  ==================================>  trace 6
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace6 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('trac_B2_-40deg.txt', trace6)
print(trace6)

# ********************************************
# MOVE 4
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 10.0)
pitools.waitontarget(gcs, axis)
print('MOVE 4 ...... -30°')
#  ==================================>  trace 7
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace7 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('trac_A2_-30deg.txt', trace7)
print(trace7)
#  ==================================>  trace 8
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace8 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('trac_B2_-30deg.txt', trace8)
print(trace8)

# ********************************************
# MOVE 5
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 10.0)
pitools.waitontarget(gcs, axis)
print('MOVE 5 ...... -20°')
#  ==================================>  trace 9
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace9 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('trac_A2_-20deg.txt', trace9)
print(trace9)
#  ==================================>  trace 10
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace10 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('trac_B2_-20deg.txt', trace10)
print(trace10)

# ********************************************
# MOVE 6
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 10.0)
pitools.waitontarget(gcs, axis)
print('MOVE 6 ...... -10°')
#  ==================================>  trace 11
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace11 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('trac_A2_-10deg.txt', trace11)
print(trace11)
#  ==================================>  trace 12
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace12 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('trac_B2_-10deg.txt', trace12)
print(trace12)

# ********************************************
# MOVE 7 - 0 °
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 10.0)
pitools.waitontarget(gcs, axis)
print('MOVE 7 ...... 0° (Référence)')
#  ==================================>  trace 13
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace13 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('trac_A2_0deg.txt', trace13)
print(trace13)
#  ==================================>  trace 14
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace14 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('trac_B2_0deg.txt', trace14)
print(trace14)

# ********************************************
# MOVE 8 - 10 °
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 10.0)
pitools.waitontarget(gcs, axis)
print('MOVE 8 ...... + 10°')
#  ==================================>  trace 15
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace15 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('trac_A2_+10deg.txt', trace15)
print(trace15)
#  ==================================>  trace 16
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace16 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('trac_B2_+10deg.txt', trace16)
print(trace16)

# ********************************************
# MOVE 9 - 20 °
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 10.0)
pitools.waitontarget(gcs, axis)
print('MOVE 9 ...... + 20°')
#  ==================================>  trace 17
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace17 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('trac_A2_+20deg.txt', trace17)
print(trace17)
#  ==================================>  trace 18
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace18 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('trac_B2_+20deg.txt', trace18)
print(trace18)

# ********************************************
# MOVE 10 - 30 °
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 10.0)
pitools.waitontarget(gcs, axis)
print('MOVE 9 ...... + 30°')
#  ==================================>  trace 19
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace19 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('trac_A2_+30deg.txt', trace19)
print(trace19)
#  ==================================>  trace 20
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace20 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('trac_B2_+30deg.txt', trace20)
print(trace20)

# ********************************************
# MOVE 11 - 30 °
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 10.0)
pitools.waitontarget(gcs, axis)
print('MOVE 9 ...... + 40°')
#  ==================================>  trace 21
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace21 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('trac_A2_+40deg.txt', trace21)
print(trace21)
#  ==================================>  trace 22
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace22 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('trac_B2_+40deg.txt', trace22)
print(trace22)

# ********************************************
# MOVE 12 - 30 °
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 10.0)
pitools.waitontarget(gcs, axis)
print('MOVE 9 ...... + 50°')
#  ==================================>  trace 23
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace23 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('trac_A2_+50deg.txt', trace23)
print(trace23)
#  ==================================>  trace 24
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace24 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('trac_B2_+50deg.txt', trace24)
print(trace24)

# ********************************************
# MOVE 13 - 30 °
# ********************************************
print('============ MOVING TO LEFT ...°')
gcs.MVR(axis, 10.0)
pitools.waitontarget(gcs, axis)
print('MOVE 9 ...... + 60°')
#  ==================================>  trace 25
instr.write_str_with_opc(':CALCULATE1:PARAMETER:SELECT "Ch1Tr1"')
trace25 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('trac_A2_+60deg.txt', trace25)
print(trace25)
#  ==================================>  trace 26
instr.write_str_with_opc(':CALCULATE2:PARAMETER:SELECT "Ch1Tr2"')
trace26 = instr.query_bin_or_ascii_float_list_with_opc('FORM ASCII; :TRAC? CH1DATA', 50000)# récupérer un tableau de flottant
instr.query_opc()
np.savetxt('trac_B2_+60deg.txt', trace26)
print(trace26)

# ********************************************
# MOVE 14 - 30 °
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


