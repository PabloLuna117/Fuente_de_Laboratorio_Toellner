import pyvisa
from time import sleep # for delays

rm = pyvisa.ResourceManager()
# List all connected resources
#print("Resources detected\n{}\n".format(rm.list_resources()))

#CONFIGURACIONES INICIALES DE FUENTE
def SETconfiguracionesDeFuenteToellner(port):
    global conexionOK
    #port='ASRL6::INSTR'
    global answer
    try:
        conexionOK=rm.open_resource(port)
        conexionOK.write('SYST:REM')
        conexionOK.write('SYST:LANG CIIL')
        conexionOK.query('*IDN?')
        conexionOK.write('*CLS')
        answer="Configuracion OK"
    except:
        answer="Error en fuente Toellner"
    return answer
#control de voltaje y corriente, activar o desactivar salida
def SETvoltajeANDCorriente(voltage, current,ONOFF):
    global conexionOK
    global answer
    if answer=="Configuracion OK":
        if(ONOFF=="TRUE"):
            ONOFF="1"
        elif(ONOFF=="FALSE"):
            ONOFF="0"
        conexionOK.write(";:CURR "+current)
        conexionOK.write(";:VOLT "+voltage)
        conexionOK.write(";:OUTP "+ONOFF)
        if (ONOFF=="0"):
            conexionOK.write('SYST:LOC')
def GETVoltajeCurrent():
    global conexionOK
    answer=str(conexionOK.query(";:MEAS:VOLT?;CURR?;POW?;:SENSE:AVER?"))
    Voltaje=float(answer[:6])
    Corriente=float(answer[7:13])
    return Voltaje, Corriente

#SETconfiguracionesDeFuenteToellner()
#SETvoltajeANDCorriente("14","2","TRUE")
#sleep(3)
#GETVoltajeCurrent()

