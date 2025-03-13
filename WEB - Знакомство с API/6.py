import os
import sys

import pygame
import requests

api_key = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"
ll = "37.617698,55.755819"
spn = "0.1,0.1"
coords = {
    "Спартак": "37.539982,55.817776",
    "Динамо": "37.558889,55.790278",
    "Лужники": "37.560278,55.715833"
}

pt = "~".join([f"{coord},pm2lbl{z + 1}" for z, (_, coord) in enumerate(coords.items())])
static_api_url = f"https://static-maps.yandex.ru/v1?ll={ll}&spn={spn}&size=600,450&pt={pt}&apikey={api_key}"

response = requests.get(static_api_url)
map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

pygame.init()
screen = pygame.display.set_mode((600, 450))
pygame.display.set_caption("Карта Москвы")

screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            os.remove(map_file)
            sys.exit()
