#importeer de numpy module als "np"
import numpy as np


#maak een lijst aan van alle temperaturen in Fahrenheit
F = [0, 12, 45.21, 34, 99.91, 32]

#maak een array aan van 1 rij met 6 getallen met allemaal 1
c = np.full((1,6),1)

#print de array c
print(c)

#maak van de lijst een array
f = np.array(F)

#selecteer de waardes van array f vanaf index 0 tot en met index6
getal1 = f[0:6]

#zet de waardes om naar graden Celcius
getal2 = (getal1-32)*5/9

#print de nieuwe array
print(getal2)

