import cv2
import numpy as np

dis = 0.0195

w = 0.2
h = 0.15

def main():
    img = cv2.VideoCapture (0)

    while img.isOpened():
        ret1, frame = img.read()

        boardsize = (9, 6)

        key = cv2.waitKey(1)

        if ret1 == True:
            ret2, corners = cv2.findChessboardCorners(frame, boardsize, None)

            if ret2 == True: 
                cv2.drawChessboardCorners(frame, boardsize, corners, ret2)

                m, worldPts = imgToWorld(corners)
        
                s = worldToEnd(frame.shape[1], frame.shape[0])
        
                transform = warp(s, m, frame)

                cv2.imshow("Transformada", transform)

                if key & 0xFF == ord('p'):
                    print(sum(worldPts), sum(corners))

        cv2.imshow("Bordas Xadrez", frame)

        if key & 0xFF == ord('q'):
            break
        
        

def imgToWorld (corners):
    worldPts = np.zeros((54, 1), dtype=(float, 2))
    l = 0
    for i in range (0, 6):
        for j in range (0, 9):
            worldPts[l] = (j*dis, i*dis)
            l += 1

    h = cv2.findHomography(corners, worldPts, cv2.RANSAC)    
    return(h[0], worldPts)

def worldToEnd(width, heigth):
    px = width / w
    py = heigth / h

    s = np.diag([px, py, 1])

    return s

def warp(s, m, frame):
    final = np.dot(s, m)
    projetiva = cv2.warpPerspective(frame, final, (frame.shape[1], frame.shape[0]))

    return projetiva


if __name__ == "__main__":
    main()