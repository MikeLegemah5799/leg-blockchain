from backend.util.hex_to_binary import hex_to_binary

def test_hex_to_binary():
    original_number = 789
    hex_number = hex(original_number)[2:] # use [:2] to cut off 2 leading zeroes
    binary_number = hex_to_binary(hex_number)
    
    
    assert int(binary_number, 2) == original_number