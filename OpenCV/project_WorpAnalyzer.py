# Libraries voor beeldverwerking, arraybewerkingen en grafieken importeren.
import cv2
import numpy as np

# Video importeren. De video moet in dezelfde map als de code staan.
cap = cv2.VideoCapture("Video1.mp4")
if not cap.isOpened():
    print("Video kan niet geopend worden.")
    exit(0)

# Achtergrondsubtractor instellen
backSub = cv2.createBackgroundSubtractorMOG2(detectShadows=True, history=50, varThreshold=30)

# Coördinaten van het balspoor
coördinaten = []

# Continu uitvoeren.
while True:
    ret, frame = cap.read()
    if frame is None:
        break

    # Achtergrond wegfilteren
    fgMask = backSub.apply(frame)

    # Schaduwen wegfilteren
    _, mask_thresh = cv2.threshold(fgMask, 200, 255, cv2.THRESH_BINARY)

    # Morfologische filtering (ruis verminderen)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    mask_open = cv2.morphologyEx(mask_thresh, cv2.MORPH_OPEN, kernel)
    mask_clean = cv2.morphologyEx(mask_open, cv2.MORPH_CLOSE, kernel)

    # Contouren zoeken
    contours, _ = cv2.findContours(mask_clean, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    min_contour_area = 100
    large_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_contour_area]

    # Frame kopiëren voor visualisatie
    frame_out = frame.copy()

    # Alleen de grootste contour gebruiken
    if large_contours:
        cnt = max(large_contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(cnt)

        # Filter op redelijke grootte van een bal (bijvoorbeeld diameter tussen 10 en 100 pixels)
        if 10 < w < 100 and 10 < h < 100:
            a = int(x + w / 2)
            b = int(y + h / 2)
            coördinaten.append((a, b))

            # Lijst beperken
            if len(coördinaten) > 50:
                coördinaten = coördinaten[-50:]

            # Teken rechthoek rond bal
            cv2.rectangle(frame_out, (x, y), (x + w, y + h), (0, 0, 200), 3)


    # Lijn tekenen tussen opeenvolgende punten
    for i in range(1, len(coördinaten)):
        pt1 = coördinaten[i - 1]
        pt2 = coördinaten[i]
        cv2.line(frame_out, pt1, pt2, (0, 255, 0), 2)
        print(pt1,pt2)

    # Masker en eindbeeld tonen
    cv2.imshow('FG Mask', mask_clean)
    cv2.imshow("Frame_final", frame_out)

    # Stoppen met 'q'
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
