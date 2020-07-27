import cv2
import numpy as np

def main():
    print("Hello world")
    print("Opencv version %s"%(cv2.__version__))

    cap = cv2.VideoCapture(0)

    if cap.isOpened() == True:
        print("Video aberto com sucesso")

    while cap.isOpened() :
        ret, frame = cap.read() ##ret diz se deu certo

        if ret == True:
            cv2.imshow("Output", frame)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            cv2.imshow("Gray Scale", gray)

            print (type(frame), frame.shape)
        
        key = cv2.waitKey(1)

        if key & 0xFF == ord('q'):
            print("Saindo...")
            break

if __name__ == "__main__": 
    main()

    #findchessbordercorners
    #drawchessbordercorners
    #board size 9, 6