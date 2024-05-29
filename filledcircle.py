import cv2

img = cv2.imread("sunleaf.png")

center_coordinates = (1000,1200)
radius = 80
colour = (0,250,0)
thickness = -1

img = cv2.circle(img, center_coordinates, radius, colour, thickness)

cv2.imshow("circle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()