import pygame

class Display:
    def __init__(self, scale: int = 10, title: str = "CHIP-8 Emulator"):
        self.width = 64
        self.height = 32
        self.scale = scale
        self.fg_color = (255, 255, 255)
        self.bg_color = (0, 0, 0)

        self.buffer = bytearray((self.width * self.height) // 8)

        if not pygame.get_init():
            pygame.init()

        self.window = pygame.display.set_mode(
            (self.width * self.scale, self.height * self.scale)
        )
        pygame.display.set_caption(title)

        self.surface = pygame.Surface((self.width, self.height))
        self.clear()

    def clear(self) -> None:
        self.buffer[:] = b"\x00" * len(self.buffer)

    def set_pixel(self, x: int, y: int) -> bool:
        if not (0 <= x < self.width and 0 <= y < self.height):
            return False

        idx = (y * self.width + x) // 8
        mask = 1 << (7 - (x % 8))

        # Detect if an active pixel is about to be erased
        collision = bool(self.buffer[idx] & mask)
        self.buffer[idx] ^= mask
        return collision

    def render(self) -> None:
        self.surface.fill(self.bg_color)
        
        for y in range(self.height):
            for x in range(self.width):
                idx = (y * self.width + x) // 8
                mask = 1 << (7 - (x % 8))
                if self.buffer[idx] & mask:
                    self.surface.set_at((x, y), self.fg_color)

        scaled = pygame.transform.scale(self.surface, self.window.get_size())
        self.window.blit(scaled, (0, 0))
        pygame.display.flip()

