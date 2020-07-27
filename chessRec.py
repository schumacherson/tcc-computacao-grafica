import cv2
import numpy as np 

def main():
    img = cv2.VideoCapture(0)

    while img.isOpened():
        ret1, frame = img.read()

        board_size = (9, 6)

        key = cv2.waitKey(1)

        if ret1 == True:
            ret2, corners = cv2.findChessboardCorners(frame, board_size, None)

            row = frame.shape[0]
            col = frame.shape[1]
            # achar transformação da imagem original para o mundo
            # achar transformação do mundo pra imagem que eu quer (escala)
            # mostrar essa última
            # usar todos os pontos do tabuleiro pro find homography
            # size é o tamanho do retangulo detectado 
                        
            if ret2 == True:
                cv2.drawChessboardCorners(frame, board_size, corners, ret2)

                src_points = np.array([ corners[0], corners[8], corners[45], corners[53]])

                ext_points = np.array([ ([col*(6/7), row*(1/10)]),
                                        ([col*(6/7), row*(9/10)]),
                                        ([col*(1/7), row*(1/10)]),
                                        ([col*(1/7), row*(9/10)]) ])

                ext_points2 = np.array([ ([col*(0.785714286), row*(0.168350168)]),
                                        ([col*(0.785714286), row*(0.828282828)]),
                                        ([col*(0.228571429), row*(0.168350168)]),
                                        ([col*(0.228571429), row*(0.828282828)]) ])

                h = cv2.findHomography(src_points, ext_points2, cv2.RANSAC)

                projetiva = cv2.warpPerspective(frame, h[0], (col, row))
                cv2.imshow("Transformada", projetiva)
                if key & 0xFF == ord('p'):
                    print(corners)
                
                

            cv2.imshow("Bordas xadrez", frame)             
                   

        if key & 0xFF == ord('q'):
            break


        




if __name__ == "__main__":
    main()