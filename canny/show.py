import cv2 as cv

img = cv.imread(
    "C:\\Users\\User\\Documents\\jsh\\2022-03-05-dlaanfdl\\canny\\Lenna.png", cv.IMREAD_GRAYSCALE)

threshold1 = 100
threshold2 = 100
canny1 = cv.Canny(img, threshold1, threshold2)

threshold1 = 150
threshold2 = 150
canny2 = cv.Canny(img, threshold1, threshold2)

threshold1 = 200
threshold2 = 200
canny3 = cv.Canny(img, threshold1, threshold2)

threshold1 = 250
threshold2 = 250
canny4 = cv.Canny(img, threshold1, threshold2)

threshold1 = 300
threshold2 = 300
canny5 = cv.Canny(img, threshold1, threshold2)

cv.imshow("Lenna", img)
cv.imshow("Canny1", canny1)
cv.imshow("Canny2", canny2)
cv.imshow("Canny3", canny3)
cv.imshow("Canny4", canny4)
cv.imshow("Canny5", canny5)

cv.waitKey(0)
cv.destroyAllWindows()

cv.imwrite(
    "C:\\Users\\User\\Documents\\jsh\\2022-03-05-dlaanfdl\\canny\\Canny1.png", canny1)
cv.imwrite(
    "C:\\Users\\User\\Documents\\jsh\\2022-03-05-dlaanfdl\\canny\\Canny2.png", canny2)
cv.imwrite(
    "C:\\Users\\User\\Documents\\jsh\\2022-03-05-dlaanfdl\\canny\\Canny3.png", canny3)
cv.imwrite(
    "C:\\Users\\User\\Documents\\jsh\\2022-03-05-dlaanfdl\\canny\\Canny4.png", canny4)
cv.imwrite(
    "C:\\Users\\User\\Documents\\jsh\\2022-03-05-dlaanfdl\\canny\\Canny5.png", canny5)
