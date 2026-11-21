class CHIP8:
    def __init__(self):
        self.memory = bytearray(4096)   # Initialize 4kb of RAM for the CHIP-8 system

# Initialize an instance and test memory read/write operations
chip = CHIP8()

# Read Write test
chip.memory[0] = 0x00A
print(f"Value: {chip.memory[0]}, Test Successful!")

# Memory address test
print(f"Memory adress: 0x000, Value: {chip.memory[0x000]}, Test Successful!")