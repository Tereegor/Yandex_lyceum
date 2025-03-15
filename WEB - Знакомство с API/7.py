import requests
import pygame
import sys
from io import BytesIO

api_key = "23e13d6a-fa45-4007-a3c9-c8a414778dfb"
ll = "29.895,59.885"
spn = "0.4,0.4"
coords = [
    "29.895,59.885",  # Петергоф
    "29.910,59.900",
    "29.950,59.920",
    "29.960,59.940",
    "30.000,59.950",
    "30.050,59.935",
    "30.100,59.930",
    "30.200,59.940",
    "30.304,59.941",  # Эрмитаж
]
pl = ",".join(coords)

static_api_url = f"https://static-maps.yandex.ru/v1?ll={ll}&spn={spn}&size=600,450&pl={pl}&apikey={api_key}"

response = requests.get(static_api_url)
image_data = BytesIO(response.content)
map_image = pygame.image.load(image_data)

pygame.init()
screen = pygame.display.set_mode((600, 450))
pygame.display.set_caption("Маршрут судна")

screen.blit(map_image, (0, 0))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()