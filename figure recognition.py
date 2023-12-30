# import potrzebnych bibliotek (w przypadku błedów wcisnąć lampkę i zainstalować)

import numpy as np
import cv2

# wczytywanie obrazku
img = cv2.imread('obraz.bmp')

# przekształcenie obrazka, bo funkcja findContours działa tylko w skali szarości
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, 1)

# wyszukiwanie konturów
contours, h = cv2.findContours(thresh, 1, 2)

# liczniki poszukiwanych figur
kwadraty = 0
kolka = 0
pienciokat = 0
trojkat = 0

for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
    print(len(approx))

    # pienciokanty
    if len(approx) == 5:
        cv2.drawContours(img, [cnt], 0, 255, -1)
        pienciokat += 1

    # trojkąty
    elif len(approx) == 3:
        cv2.drawContours(img, [cnt], 0, (0, 255, 0), -1)
        trojkat += 1

    # kwadraty
    elif len(approx) == 4:
        cv2.drawContours(img, [cnt], 0, (0, 0, 255), -1)
        kwadraty += 1

    # kolka
    elif len(approx) > 9:
        cv2.drawContours(img, [cnt], 0, (255, 255, 0), -1)
        kolka += 1

# Wywodze dane o figurach do konsoli
print("Liczba kwadratów: ", (kwadraty / 2))
print("Liczba kolkow: ", (kolka / 2))
print("Liczba pięciokątów: ", (pienciokat / 2))
print("Liczba trojkątów: ", (pienciokat / 2))

cv2.imshow('img', img)
cv2.imwrite('wynik.png', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
