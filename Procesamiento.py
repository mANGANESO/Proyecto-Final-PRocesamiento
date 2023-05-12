import cv2
import serial

# Inicializar la cámara
#cap = cv2.VideoCapture(0)  # 0 para la cámara predeterminada, puedes cambiarlo si tienes varias cámaras

# Capturar imagen
#ret, frame = cap.read()
#cv2.imshow('Imagen', frame)


# Redimensionar la imagen a 8x8 píxeles
#resized_frame = cv2.resize(frame, (8, 8), interpolation=cv2.INTER_LINEAR)

# Convertir la imagen a escala de grises
#gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)

# Obtener el valor entero de 8 dígitos
#value = int(gray_frame.flatten().tolist())

# Inicializar la conexión serial
#ser = serial.Serial('COM6', 9600)  # Reemplaza 'COM3' con el puerto serial correcto y 9600 con la velocidad de comunicación adecuada

# Enviar el valor entero a Arduino
#ser.write(str(value).encode())

# Cerrar la conexión serial
#ser.close()

# Liberar la cámara
#cap.release()

# Cerrar todas las ventanas abiertas
#cv2.destroyAllWindows()

# Inicializar la cámara
cap = cv2.VideoCapture(0)  # 0 para la cámara predeterminada, puedes cambiarlo si tienes varias cámaras

while True:
    # Capturar imagen
    ret, frame = cap.read()

    # Mostrar la imagen en una ventana
    cv2.imshow('Imagen', frame)

    # Detener el bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara
cap.release()

# Cerrar todas las ventanas abiertas
cv2.destroyAllWindows()
