import cv2

img = cv2.imread("sunleaf.png")

start = (900,800)
end = (1200,1000)
colour = (0,0,250)
thickness = 4

img=cv2.line(img, start, end, colour, thickness)
cv2.imshow("line", img)
cv2.waitKey(0)
cv2.destroyAllWindows()