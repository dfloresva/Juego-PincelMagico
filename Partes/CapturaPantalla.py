import cv2

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

#'''
#Supuesta Funcion para la captura de la imagen en los dos frame
cont=0
#def capturarPantalla(frame,imAux):
def capturarPantalla():
    ret,frame=cap.read()
    cv2.imwrite('captura'+str(cont)+'1.png',frame)
    return
    
    #cv2.imwrite('captura'+str(cont)+'2.png',imAux)
    
#captura=input("capturar pantalla?:")
#'''

################## Primera Captura
capturarPantalla()
print("primera captura")
cont+=1
################## Segunda Captura
capturarPantalla()
print("segunda captura")

###################
cap.release()
cv2.destroyAllWindows()


'''
ret,frame=cap.read()
cv2.imwrite('captura'+str(cont)+'1.png',frame)
cont+=1
cap.release()
cv2.destroyAllWindows()
'''