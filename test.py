import asyncio
from ws_manager import broadcast

### Fichier test pour pouvoir tester la calibration sans le raspberry PI.
### Pour tester, il faut decommenter l'import dans app.py

async def calibrage(n):
    """
    n = durée en secondes
    Renvoie le seuil bas du son ambiant (0)
    """
    taux_interpolation = 0.1

    await broadcast("Veuillez ne pas faire de bruit durant le calibrage du son ambiant")
    print("Veuillez ne pas faire de bruit durant le calibrage du son ambiant")
    await asyncio.sleep(5)
    for i in range(3,0,-1):
        await broadcast("Le calibrage commence dans " + str(i) + " secondes")
        print("Le calibrage commence dans ",i," secondes")
        await asyncio.sleep(1)
    await broadcast("Calibrage du son ambiant en cours... Veuillez rester silencieux.")
    print("Silence")
    L = []
    for _ in range(int(n*(1/taux_interpolation))):
        L.append(0)
        await asyncio.sleep(taux_interpolation)
    S = (sum(x**2 for x in L)/len(L))**0.5 # Calcul du Seuil bas
    await broadcast("Calibrage du son ambiant terminé. (" + str(S) + ")")
    print("Calibrage du son ambiant terminé")
    return S