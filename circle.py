import cv2

img = cv2.imread("sunleaf.png")

center_coordinates = (250,200)
radius  = 60
colour = (200,150,0)
thickness = 2

img=cv2.circle(img, center_coordinates, radius, colour, thickness)

cv2.imshow("Circle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()