### BRANCHER SUT LE PORT 12 DU BASE HAT
### https://wiki.seeedstudio.com/Grove-Red_LED/
from grove.gpio import GPIO
import sqlite3
import asyncio

class GroveLed(GPIO):
    def __init__(self,pin):
        super(GroveLed, self).__init__(pin, GPIO.OUT)

    def on(self):
        self.write(1)

    def off(self):
        self.write(0)


Grove = GroveLed
pin=12
connect = sqlite3.connect("singonlight.db")
dureeIntervalle = connect.execute("SELECT valeur FROM parametres WHERE cle = 'dureeIntervalle';").fetchone()[0]
connect.close()

async def main(schema_aleatoire:list[int],start_event):
    """utiliser LED.run() a la place car c'edt une fonction async. """
    await start_event.wait()

    led = GroveLed(pin)

    for i in range(len(schema_aleatoire)):
        if schema_aleatoire[i] == 1:
            led.on()
        elif schema_aleatoire[i] == 0:
            led.off()
        
        await asyncio.sleep(dureeIntervalle)
    led.off()
    return schema_aleatoire
    
led = GroveLed(pin)
def change_state(rythme,i):
    if rythme[i] == 1:
        led.on()
    else:
        led.off()
    return rythme
    
def run(schema_aleatoire:list[int]):
    """a utiliser pour executer main()"""
    return asyncio.run(main(schema_aleatoire))

if __name__ == '__main__':
    asyncio.run(main())


