import cv2
import numpy as np 

def main():
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()

        if ret == True:
            frmTri = np.array( [[0, 0], [frame.shape[1] - 1, 0], [0, frame.shape[0] - 1]] ).astype(np.float32)
            extTri = np.array( [[0, frame.shape[1]*0.33], [frame.shape[1]*0.85, frame.shape[0]*0.25], [frame.shape[1]*0.15, frame.shape[0]*0.7]] ).astype(np.float32)

            warp_mat = cv2.getAffineTransform(frmTri, extTri)
            warp_ext = cv2.warpAffine(frame, warp_mat, (frame.shape[1], frame.shape[0]))

            center = (warp_ext.shape[1]//2, warp_ext.shape[0]//2)
            angle = -50
            scale = 0.6
            rot_mat = cv2.getRotationMatrix2D( center, angle, scale )
            warp_rotate_ext = cv2.warpAffine(warp_ext, rot_mat, (warp_ext.shape[1], warp_ext.shape[0]))

            cv2.imshow("Imagem original", frame)
            cv2.imshow("Imagem transladada", warp_ext)
            cv2.imshow("Imagem transladada e rotacionada", warp_rotate_ext)

        key = cv2.waitKey(1)

        if key & 0xFF == ord('q'):
            print("Saindo...")
            break

if __name__ == "__main__":
    main()