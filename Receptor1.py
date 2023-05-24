from PIL import Image
import numpy as np
import serial

def recibir_datos():
    datos_recibidos = []
    while True:
        linea = puerto_serial.readline().decode().strip()
        if linea == "":
            break
        datos_recibidos.append(linea)
    return datos_recibidos

def imprimir_datos(datos):
    for dato in datos:
        print(dato)

def convertir_simbolos(matriz):
    simbolos = {'0': '0000000', '1': '01', '2': '10', '3': '1111111'}
    matriz_simbolos = []
    for fila in matriz:
        fila_simbolos = [simbolos[numero] for numero in fila]
        matriz_simbolos.extend(fila_simbolos)
    return matriz_simbolos

def decode_hamming(encoded_list):
    decoded_matrix = [[''] * 10 for _ in range(10)]
    decoded_list = []
    
    for i, encoded_bits in enumerate(encoded_list):
        if len(encoded_bits) != 7:
            raise ValueError("Se requieren 7 bits en cada elemento de la lista.")
    
    encoded_bits = list(map(int, encoded_bits))
    
    p1 = encoded_bits[0] ^ encoded_bits[2] ^ encoded_bits[4] ^ encoded_bits[6]
    p2 = encoded_bits[1] ^ encoded_bits[2] ^ encoded_bits[5] ^ encoded_bits[6]
    p3 = encoded_bits[3] ^ encoded_bits[4] ^ encoded_bits[5] ^ encoded_bits[6]
    
    error_index = p3 * 4 + p2 * 2 + p1 - 1
    
    if error_index >= 0:
        encoded_bits[error_index] = 1 - encoded_bits[error_index]
    decoded_bits = [encoded_bits[2], encoded_bits[4], encoded_bits[5],
    encoded_bits[6]]
    
    row = i // 10
    col = i % 10
    
    char_value = ''.join(str(bit) for bit in decoded_bits)
    decoded_matrix[row][col] = char_value
    decoded_list.append(char_value)
    return decoded_matrix, decoded_list

puerto_serial = serial.Serial('COM6', 9600)
datos_recibidos = recibir_datos()
print("Datos recibidos:")
imprimir_datos(datos_recibidos)
matriz_simbolos = convertir_simbolos(datos_recibidos)

for simbolo in matriz_simbolos:
    print(simbolo)
decoded_matrix, decoded_list = decode_hamming(matriz_simbolos)

print("\nLista decodificada:")
print(decoded_list)
print("\nMatriz decodificada:")

for row in decoded_matrix:
    print(' '.join(row))

matriz_pixeles = np.array(decoded_matrix, dtype=np.uint8) * 85
imagen = Image.fromarray(matriz_pixeles, mode='L')
imagen.save('imagen_gris.png')
imagen.show()