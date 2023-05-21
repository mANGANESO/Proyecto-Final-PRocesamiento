from PIL import Image
import numpy as np

class Codificacion:
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

    def codificar_imagen(self, imagen_path):
        imagen_bn = self.convertir_a_bn(imagen_path)
        codificacion = []
        
        for fila in imagen_bn:
            bits_codificados = self.codificar_fila(fila)
            codificacion.extend(bits_codificados)
        
        return codificacion

    def convertir_a_bn(self, imagen_path):
        imagen = Image.open(imagen_path).convert('L')
        imagen_array = np.array(imagen)
        imagen_bn = np.where(imagen_array > 127, 1, 0)
        return imagen_bn

    def codificar_fila(self, fila):
        bits_codificados = []
        num_bits = len(fila)
        num_bloques = num_bits // 4

        for i in range(num_bloques):
            bloque = fila[i * 4 : (i + 1) * 4]
            bits_codificados.extend(self.codificar_bloque(bloque))
        
        return bits_codificados

    def codificar_bloque(self, bloque):
        bloque_codificado = np.dot(self.hamming_matrix, bloque) % 2
        return bloque_codificado.tolist()

def Decodificacion(codificacion):
    hamming_matrix_p = np.linalg.pinv(Codificacion().hamming_matrix)
    decodificacion = []
    num_bloques = len(codificacion) // 7

    for i in range(num_bloques):
        bloque_codificado = codificacion[i * 7 : (i + 1) * 7]
        bloque_decodificado = np.dot(hamming_matrix_p, bloque_codificado) % 2
        decodificacion.extend(bloque_decodificado[:4].tolist())

    return decodificacion

# Ejemplo de uso
imagen_path = 'Mickey_Mouse.png'
codificador = Codificacion()
codificacion = codificador.codificar_imagen(imagen_path)
print("Codificación:", codificacion)

decodificacion = Decodificacion(codificacion)
print("Decodificación:", decodificacion)
