import numpy as np
from PIL import Image

class CodificacionM:
    def __init__(self):
        self.hamming_matrix = np.array([
            [1, 1, 0, 1],
            [1, 0, 1, 1],
            [1, 0, 0, 0],
            [0, 1, 1, 1],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])
        
      
class Decodificacion():
    def __init__(self, codificacion):
        self.codificacion = codificacion
        hamming_matrix_p = np.linalg.pinv(CodificacionM().hamming_matrix)
        decodificacion = []
        num_bloques = len(codificacion) // 7

        for i in range(num_bloques):
            bloque_codificado = codificacion[i * 7 : (i + 1) * 7]
            bloque_decodificado = np.dot(hamming_matrix_p, bloque_codificado) % 2
            decodificacion.extend(bloque_decodificado[:4].tolist())
        print("Decodificacion: ",decodificacion)
        imagen_path = 'Mickey_Mouse.png'
        Decodificacion.mostrar_imagen(decodificacion, imagen_path)
        
    def mostrar_imagen(decodificacion, imagen_path):
        # Obtener el tamaño de la imagen original
        imagen_original = Image.open(imagen_path)
        ancho, alto = imagen_original.size
    
        # Convertir la decodificación en un array numpy y redimensionarlo al tamaño de la imagen original
        decodificacion_array = np.array(decodificacion).reshape((alto, 284))
    
        # Crear una imagen en escala de grises a partir de la decodificación
        imagen_decodificada = Image.fromarray(decodificacion_array.astype(np.uint8) * 255, 'L')
    
        # Mostrar la imagen decodificada
        imagen_decodificada.show()


   