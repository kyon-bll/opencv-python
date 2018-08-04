import cv2

# 読み込み
img = cv2.imread('ichigo_hunt.jpg', cv2.IMREAD_GRAYSCALE)

# 表示
cv2.namedWindow('ichigo_hunt', cv2.WINDOW_NORMAL)
cv2.imshow('ichigo_hunt', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 保存
cv2.imwrite('ichigo_gray.png', img)
