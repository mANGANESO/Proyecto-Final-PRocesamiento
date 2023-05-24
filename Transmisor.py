import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def calculate_parity_bit(data):
    parity = 0
    for bit in data:
        parity ^= int(bit)
    return str(parity)

def apply_hamming_code(data):
    p1 = calculate_parity_bit(data[0] + data[1] + data[3])
    p2 = calculate_parity_bit(data[0] + data[2] + data[3])
    p3 = calculate_parity_bit(data[1] + data[2] + data[3])
    return p1 + p2 + data[0] + data[1] + data[2] + p3 + data[3]

def convert_to_hamming_code(matrix):
    flat_list = matrix.flatten()
    hamming_list = [apply_hamming_code(data) for data in flat_list]
    return hamming_list

def grayscale_to_binary(gray_value):
    if gray_value < 0 or gray_value > 15:
        raise ValueError("El valor de escala de grises debe estar entre 0 y 15.")
    binary_value = bin(gray_value)[2:].zfill(4)
    return binary_value

image_path = "mario.png"
image = Image.open(image_path).convert("L")

normalized_image = np.array(image)
normalized_image = (normalized_image - np.min(normalized_image)) /
(np.max(normalized_image) - np.min(normalized_image))
normalized_image = np.round(normalized_image * 15)

binary_image = np.array([[grayscale_to_binary(int(pixel)) for pixel in row] for row in
normalized_image])

hamming_code_image = np.array([convert_to_hamming_code(row) for row in
binary_image])

def rearrange_bits(number):
    binary_number = format(number, '07b')
    rearranged_list = [binary_number[i:i+2] for i in range(0, len(binary_number), 2)]
    if len(binary_number) % 2 != 0:
        rearranged_list[-1] += '0'
    return rearranged_list

rearranged_bits = [rearrange_bits(int(number, 2)) for number in
hamming_code_image.flatten()]

print("Bits reorganizados:")

for bits in rearranged_bits:
    print(bits)

qpsk_symbols = []
height, width = hamming_code_image.shape

symbol_matrix = np.empty((10, 10), dtype=str)

for i in range(10):
    for j in range(10):
        pixel = hamming_code_image[i, j]
        symbol = ""
    if pixel == '0000000':
        symbol = "0"
    elif pixel == '1010':
        symbol = "01"
    elif pixel == '0101':
        symbol = "10"
    elif pixel == '1111111':
        symbol = "3"
    symbol_matrix[i, j] = symbol

print("Imagen en escala de grises:")
print(normalized_image)
print("\nImagen en representación binaria:")
print(binary_image)
print("\nImagen en código de Hamming (7,4):")
print(hamming_code_image)
print("\nMatriz de símbolos QPSK:")
print(symbol_matrix)

plt.imshow(normalized_image, cmap='gray', vmin=0, vmax=15)
plt.title('Imagen en escala de grises')
plt.axis('off')
plt.show()

def qpsk_modulation(symbol_matrix):
    modulated_symbols = []
    for symbol in symbol_matrix.flatten():
        if symbol == '0':
            I = -1
            Q = -1
        elif symbol == '01':
            I = 1
            Q = -1
        elif symbol == '10':
            I = 1
            Q = -1
        elif symbol == '3':
            I = 1
            Q = 1
        modulated_symbols.append(complex(I, Q))
    return np.array(modulated_symbols).reshape(symbol_matrix.shape)

sym_matrix = symbol_matrix
modulated_symbols = qpsk_modulation(sym_matrix)

print("\nModulación QPSK:")
print(modulated_symbols)

x = np.real(modulated_symbols.flatten())
y = np.imag(modulated_symbols.flatten())

plt.scatter(x, y, color='b')
plt.axhline(0, color='k', linestyle='--')
plt.axvline(0, color='k', linestyle='--')
plt.xlabel('I')
plt.ylabel('J')
plt.title('Diagrama de constelación QPSK')
plt.grid(True)
plt.show()