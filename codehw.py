import cv2

img = cv2.imread("greenbg.jpeg")

start = (100,400)
end = (420,550)
thickness = -1
colour = (117,90,87)

img = cv2.rectangle(img, start, end, colour, thickness)
cv2.imshow("rectangle", img)

start = (140,300)
end = (380,400)
thickness = -1
colour = (38,48,56)

img = cv2.rectangle(img, start, end, colour, thickness)
cv2.imshow("rectangle", img)




position = (120, 150)
font = cv2.FONT_ITALIC
fontscale = 2
colour = (50,28,32)
thickness = 4

img = cv2.putText(img, "HOUSE", position, font, fontscale, colour, thickness)
cv2.imshow("rectangle", img)


cv2.waitKey(0)
cv2.destroyAllWindows()