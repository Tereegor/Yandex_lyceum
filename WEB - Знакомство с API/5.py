import requests
import pygame
import sys
import os

api_key = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"
ll = "133,-25.5"
spn = "40,20"
static_api_url = f"https://static-maps.yandex.ru/v1?ll={ll}&spn={spn}&size=600,450&apikey={api_key}"

response = requests.get(static_api_url)
map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

pygame.init()
screen = pygame.display.set_mode((600, 450))
pygame.display.set_caption("Карта Австралии")

screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            os.remove(map_file)
            sys.exit()