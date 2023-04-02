import cv2
import numpy as np
import matplotlib.pyplot as pyplot

def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray, (5, 5), 0)
    canny_image = cv2.Canny(blur, 50, 150)
    return canny_image


def display_lines(image, lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2  = line.reshape(4)
            cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 6)
    return line_image

def region_of_interest(image):
    height = image.shape[0]
    polygons = np.array([(200, height), (1100, height), (550, 250)])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, pts = [polygons], color = (255,255,255))
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image


image = cv2.imread('test_image.jpg')
lane_image = np.copy(image)
canny_img = canny(lane_image)
#cv2.imshow('result',canny_img)
cropped_image = region_of_interest(canny_img)
lines = cv2.HoughLinesP(cropped_image, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=5)
line_image = display_lines(lane_image, lines)
combo_image = cv2.addWeighted(lane_image, 0.8, line_image, 1, 1)
cv2.imshow('result', combo_image)
cv2.waitKey(0)
