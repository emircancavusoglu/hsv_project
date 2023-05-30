import cv2


def click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        h = hsv[y, x, 0]
        s = hsv[y, x, 1]
        v = hsv[y, x, 2]
        hsv_uzayi = 'HSV: ' + str(h) + ' ' + str(s) + ' ' + str(v)
        cv2.putText(img, hsv_uzayi, (x, y), cv2.FONT_HERSHEY_PLAIN, 1, (100, 20, 0), 1)
        cv2.imshow("Goruntu", img)


img = cv2.imread('cloud.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("Goruntu", img)
cv2.setMouseCallback('Goruntu', click)
cv2.waitKey(0)
cv2.destroyAllWindows()
