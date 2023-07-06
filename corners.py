import cv2
import numpy as np

path = 'photos/chessboard.jpg'
img = cv2.imread(path, -1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
corners = np.int0(corners)

flattenedCorners = []
for corner in corners:
    x, y = corner.ravel()
    flattenedCorners.append(corner.ravel())
    cv2.circle(img, (x, y), 2, (0, 0, 255), -1)

for i in range(len(flattenedCorners)):
    for j in range(i + 1, len(flattenedCorners)):
        corner1 = tuple(flattenedCorners[i])
        corner2 = tuple(flattenedCorners[j])
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
        cv2.line(img, corner1, corner2, color, 1)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()