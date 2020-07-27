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
                if key & 0xFF == ord('p'):
                    cv2.drawChessboardCorners(frame, boardsize, corners, ret2)

                    m = imgToWorld(corners)
            
                    s = worldToEnd(frame.shape[1], frame.shape[0])
            
                    transform = warp(s, m, frame)

                    cv2.imshow("Transformada", transform)



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

    k = cv2.findHomography(corners, worldPts) 
    teste = myHomography(corners, worldPts)
    return(teste)

def worldToEnd(width, heigth):
    px = width / w
    py = heigth / h

    s = np.diag([px, py, 1])

    return s

def warp(s, m, frame):
    final = np.dot(s, m)
    projetiva = cv2.warpPerspective(frame, final, (frame.shape[1], frame.shape[0]))

    return projetiva


def myHomography (corners, worldPts):
    a = np.array([
        [sum(corners**2)[0,0], sum(corners[:,:,0]*corners[:,:,1]), sum(corners)[0,0]],
        [sum(corners[:,:,0]*corners[:,:,1]), sum(corners**2)[0,1], sum(corners)[0,1]],
        [sum(corners)[0,0], sum(corners)[0,1], 1]
    ]  ,dtype=float)

    b1 = np.array([sum(corners[:,:,0] * worldPts[:,:,0]), sum(corners[:,:,1]*worldPts[:,:,0]), sum(worldPts)[0,0]],  dtype=float)

    b2 = np.array([sum(corners[:,:,0] * worldPts[:,:,1]), sum(corners[:,:,1]*worldPts[:,:,1]), sum(worldPts)[0,1]], dtype=float)

    b3 = np.array([sum(corners)[0, 0], sum(corners)[0, 1], 1], dtype=float)

    x1 = np.linalg.solve(a, b1)
    x2 = np.linalg.solve(a, b2)
    x3 = np.linalg.solve(a, b3)

    x = np.array([x1, x2, x3],  dtype=float)

    print(a,"\n", b1, "\n", x1)

    return x   
    

if __name__ == "__main__":
    main()