import cv2 as cv

img1 = cv.imread('../input/imagem1.jpg')
img2 = cv.imread('../input/imagem2.jpg')


def none(x):
    pass


def fadeApply(img1, img2, alpha):
    newImage = img1 * alpha + img2 * (1 - alpha)

    path = "../output/img_fade_" + str(alpha) + ".jpg"
    cv.imwrite(path, newImage)

    return cv.imread(path)


if __name__ == '__main__':
    alpha = 0

    cv.namedWindow('Set Alpha (Press ESC to leave)')
    cv.createTrackbar('Alpha', 'Set Alpha (Press ESC to leave)', 0, 100, none)

    img = img1

    while(1):

        cv.imshow('Set Alpha (Press ESC to leave)', img)
        k = cv.waitKey(1) & 0xFF
        if k == 27:
            break

        alpha = cv.getTrackbarPos('Alpha', 'Set Alpha (Press ESC to leave)')/100.0
        img = fadeApply(img1, img2, alpha)

