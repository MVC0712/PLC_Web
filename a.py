def split_to_8bit(decimal):
    # convert DEC number to BIN number
    binary = bin(decimal)[2:].zfill(16) # fill 0 to space

    # split 8bit + 8bit
    first_8bit = binary[:8]
    second_8bit = binary[8:]

    return first_8bit, second_8bit

def convert_to_hex(binary):
    # convert BIN number to HEX number
    hex_value = hex(int(binary, 2))[2:].zfill(2)

    return hex_value

# テスト用の10進数
decimal = 16973

first_8bit, second_8bit = split_to_8bit(decimal)

first_8bit_hex = convert_to_hex(first_8bit)
second_8bit_hex = convert_to_hex(second_8bit)

print("First 8 bits (hex):", first_8bit_hex)
print("Second 8 bits (hex):", second_8bit_hex)