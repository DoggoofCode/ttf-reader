import pygame
from vector_types import *


class BinaryReader:
    def __init__(self, file_data: bytes):
        self.file = list(map(lambda x: hex(x) if len(hex(x)) == 4 else hex(x)[:2] + '0' + hex(x)[2:], list(file_data)))
        self.position = 0

    def basic_read(self, *, bytes_size: int):
        size = bytes_size
        data = self.file[self.position:self.position + size]
        return data

    def read(self, *, bytes_size: int):
        size = bytes_size
        data = self.basic_read(bytes_size=size)
        self.move(size)
        return data

    def move(self, offset: int):
        self.position += offset


def parseTTF(file_path: str, file_name: str):
    with open(fr"{file_path}\{file_name}.ttf", "rb") as file:
        reader = BinaryReader(file.read())
    reader.move(4)
    num_tables = IntX(reader.read(bytes_size=2))
    reader.move(6)
    # print(num_tables)
    for i in range(num_tables):
        table_tag = reader.read(bytes_size=4)
        checksum = IntX(reader.read(bytes_size=4))
        offset = IntX(reader.read(bytes_size=4), little_endian=False)
        length = IntX(reader.read(bytes_size=4))
        print(f"Tag: {ReadText(table_tag)}, [Raw: {table_tag}], Offset: {offset}")



def create_bezier_curve(screen, p0: Vec2, p1: Vec2, p2: Vec2, resolution):
    for i in range(resolution):
        t = i / resolution
        """
        Bezier Interpolation Explanation
        (((1 - t) ** 2) * _) + (2 * (1 - t) * t * _) + ((t ** 2) * _)
                           p0.x                 control.x        p2.x
                            ^                       ^              ^
        x = (1 - t) ** 2 * 100 + 2 * (1 - t) * t * 200 + t ** 2 * 250
        y = (1 - t) ** 2 * 150 + 2 * (1 - t) * t * 175 + t ** 2 * 300
        """
        b_inter = BezierInterpolation(p0, p1, p2, t)
        screen.set_at((int(b_inter.x), int(b_inter.y)), (255, 255, 255))


def main():
    pygame.init()
    pygame.display.set_caption("Bezier💀")
    window_width = 800
    window_height = 600
    size = (window_width, window_height)
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)

    resolution = 400

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                # The window has been resized, so update the width, height, and size
                window_width = event.w
                window_height = event.h
                size = (window_width, window_height)
                screen = pygame.display.set_mode(size, pygame.RESIZABLE)
        screen.fill((0, 0, 0))

        pygame.draw.circle(screen, (255, 0, 0), (100, 150), 10)

        pygame.draw.circle(screen, (0, 255, 0), (200, 175), 10)

        pygame.draw.circle(screen, (0, 0, 255), (250, 300), 10)

        create_bezier_curve(screen, Vec2(100, 150), Vec2(200, 175), Vec2(250, 300), resolution)

        pygame.display.flip()


if __name__ == "__main__":
    parseTTF(r"fonts\jet_brains_mono", "JetBrainsMono-Bold")
