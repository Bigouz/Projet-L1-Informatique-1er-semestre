#######

# PAS BESOIN DE CE FICHIER (j'ai tout mis dans SoundSensor.py et test.py et ça fonctionne)

#######

#import grovepi
#import numpy as np
#import time
#import SoundSensor.py as sound

#connect = sqlite3.connect('singonlight.db')
#cursor = connect.execute('SELECT dureeIntervalle, dureePartie FROM parametres;')
#duree_intervalle, duree_parti = cursor.fetchone()
#connect.close()

# definition du décibel minimal a dépasser
#def recuperation_son(n):
#  l = []
#  start = time.time()
#  while time.time() - start<n:
#    l.append(sound.main())
#  return l

#def seuil(bruit):
#  phrase_calibrage = "Veuillez ne pas faire de bruit durant le calibrage du son ambiant"
#  phrase_commence = "Silence"
#  phrase_fin = "Calibrage du son ambiant terminé"
#  n_ambiant = 5 # durée en seconde définit par l'utilisateur dans les paramètre
#  print(phrase_calibrage)
#  time.sleep(5)
#  for i in range(3,0,-1):
#    print("Le calibrage commence dans ",i," secondes")
#    time.sleep(1)
#  print(phrase_commence)
#  start = time.time()
#  while time.time() - start<n:
#    l = np.array(sound.run())
#  S = np.sqrt(np.mean(l**2)) # Calculer le Seuil bas
#  print(phrase_fin)
#  return S