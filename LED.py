### BRANCHER SUT LE PORT 12 DU BASE HAT
### https://wiki.seeedstudio.com/Grove-Red_LED/
from grove.gpio import GPIO
import sqlite3
import asyncio

class GroveLed(GPIO):
    def __init__(self,pin):
        super(GroveLed, self).__init__(pin, GPIO.OUT)

    def on(self):
        """ allume la LED """
        self.write(1)

    def off(self):
        """ eteint la LED """
        self.write(0)


Grove = GroveLed
pin=12
connect = sqlite3.connect("singonlight.db")
dureeIntervalle = connect.execute("SELECT valeur FROM parametres WHERE cle = 'dureeIntervalle';").fetchone()[0]
connect.close()
    
led = GroveLed(pin)
def change_state(rythme,i):
    """ change l'etat de la LED selon le rythme et l'indice i
        si rythme[i] == 1, alors la led s'allume, elle s'éteint sinon. 
    """
    if rythme[i] == 1:
        led.on()
    else:
        led.off()
    return rythme