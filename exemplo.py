import serial
import glob
import sys



def Porta():  # Lista as portas disponiveis

        if sys.platform.startswith('win'):
            ports = ['COM' + str(i + 1) for i in range(256)] # testei apenas no windows - nao sei se nos demais funciona corretamente
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')

        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass

        return result

print(Porta())
