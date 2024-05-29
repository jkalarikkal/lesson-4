import cv2
img = cv2.imread("sunleaf.png")

position = (500,1500)
font = cv2.FONT_ITALIC
fontscale = 15
colour = (100,100,250)
thickness = 40

img = cv2.putText(img, "Hi im JAANVI", position, font, fontscale, colour, thickness)
cv2.imshow("txt", img)

cv2.waitKey(0)
cv2.destroyAllWindows()