import numpy as np


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



