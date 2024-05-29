import cv2

img = cv2.imread("sunleaf.png")

start = (1500,2000)
end = (600,950)
thickness = 80
colour = (100,0,250)

img = cv2.rectangle(img, start, end, colour, thickness)
cv2.imshow("rectangle", img)

cv2.waitKey(0)
cv2.destroyAllWindows()