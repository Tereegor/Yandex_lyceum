from io import BytesIO

import pygame
import requests

api_key = "23e13d6a-fa45-4007-a3c9-c8a414778dfb"

slides = [
    {"ll": "37.6176,55.7558", "spn": "0.1,0.1"},  # Москва
    {"ll": "30.3351,59.9343", "spn": "0.1,0.1"},  # Санкт-Петербург
    {"ll": "39.7231,43.5855", "spn": "0.1,0.1"},  # Сочи
    {"ll": "131.8856,43.1155", "spn": "0.1,0.1"},  # Владивосток
    {"ll": "49.1088,55.7963", "spn": "0.1,0.1"},  # Казань
    {"ll": "56.2294,58.0105", "spn": "0.1,0.1"},  # Пермь
]


def load_map(ll, spn):
    url = f"https://static-maps.yandex.ru/v1?ll={ll}&spn={spn}&size=600,450&l=map&apikey={api_key}"
    response = requests.get(url)
    return pygame.image.load(BytesIO(response.content))


pygame.init()
screen = pygame.display.set_mode((600, 450))
pygame.display.set_caption("Слайд-шоу")

slide_images = []
for slide in slides:
    image = load_map(slide["ll"], slide["spn"])
    if image:
        slide_images.append(image)

current_slide = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            current_slide = (current_slide + 1) % len(slide_images)

    if slide_images:
        screen.blit(slide_images[current_slide], (0, 0))
        pygame.display.flip()

pygame.quit()
