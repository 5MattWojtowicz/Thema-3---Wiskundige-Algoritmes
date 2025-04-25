#importeer de numpy module als "np"
import numpy as np

#maak een array aan van 8x8 met alleen 1
a = np.full((8,8),1)

#print array a
print(a)

#verander rijen met index 0 tot en met index 7 met stapgroote 2, index 1 tot en met index 7 met stapgroote 2 naar 0
a[0:7:2, 1:8:2] = 0

#verander rijen met index 1 tot en met index 8 met stapgroote 2, index 0 tot en met index 7 met stapgroote 2 naar 0
a[1:8:2, 0:7:2] = 0

#print matrix a
print(a)