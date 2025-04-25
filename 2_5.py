#importeer de numpy module als "np"
import numpy as np

#maak een array van 5x5 met alleen maar nullen en print deze
a = np.full((5, 5), 1)
print(a)

#vervang alle waardes vanad rij 1 tot en met rij 4 vanaf index 1 tot en met 4 naar 0
a[1:4,1:4] = 0

#print matrix a
print(a)

