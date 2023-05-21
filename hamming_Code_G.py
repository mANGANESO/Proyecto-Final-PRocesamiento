import serial

# Configurar el puerto serial
puerto = serial.Serial('COM7', 9600)  # Reemplaza 'COM1' por el puerto serial que estés utilizando

# Arreglo de números enteros
arreglo = [1, 2, 3, 4, 5, 6, 7, 8]

# Convertir el arreglo a una cadena de texto separada por comas
cadena = ','.join(str(num) for num in arreglo)

# Transmitir la cadena a través del puerto serial
puerto.write(cadena.encode())

# Cerrar el puerto serial
puerto.close()

#################################################################
def calculate_parity_bits(data):
    p1 = data[0] ^ data[1] ^ data[3]
    p2 = data[0] ^ data[2] ^ data[3]
    p3 = data[1] ^ data[2] ^ data[3]
    return [p1, p2, data[0], p3, data[1], data[2], data[3]]

def hamming_encode_image(image):
    encoded_image = []
    for pixel in image:
        # Convert the pixel value to binary string
        pixel_binary = format(pixel, '08b')
        data_bits = [int(bit) for bit in pixel_binary[:4]]

        # Calculate the parity bits
        parity_bits = calculate_parity_bits(data_bits)

        # Create the Hamming code
        hamming_code = parity_bits + data_bits

        # Convert the Hamming code back to decimal
        encoded_pixel = int(''.join(str(bit) for bit in hamming_code), 2)
        encoded_image.append(encoded_pixel)

    return encoded_image

def hamming_decode_image(encoded_image):
    decoded_image = []
    for encoded_pixel in encoded_image:
        # Convert the encoded pixel value to binary string
        encoded_binary = format(encoded_pixel, '07b')
        encoded_bits = [int(bit) for bit in encoded_binary]

        # Extract the data and parity bits
        data_bits = encoded_bits[2:6]
        parity_bits = encoded_bits[:2] + [0] + encoded_bits[6:]

        # Calculate the syndrome
        syndrome = [
            (parity_bits[0] ^ data_bits[0] ^ data_bits[1] ^ data_bits[3]),
            (parity_bits[1] ^ data_bits[0] ^ data_bits[2] ^ data_bits[3]),
            (parity_bits[3] ^ data_bits[1] ^ data_bits[2] ^ data_bits[3])
        ]

        # Correct the error (if any)
        error_position = sum(i * bit for i, bit in enumerate(syndrome))
        if error_position != 0:
            error_position -= 1
            data_bits[error_position] ^= 1  # Flip the erroneous bit

        # Convert the data bits back to decimal
        decoded_pixel = int(''.join(str(bit) for bit in data_bits), 2)
        decoded_image.append(decoded_pixel)

    return decoded_image

# Example usage
original_image = [125, 211, 42, 99]  # Original image pixel values

# Encoding
encoded_image = hamming_encode_image(original_image)
print("Encoded image:", encoded_image)

# Decoding
decoded_image = hamming_decode_image(encoded_image)
print("Decoded image:", decoded_image)
