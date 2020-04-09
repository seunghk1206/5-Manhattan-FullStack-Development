from network import network
import pygame

width = 500
height = 500

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Manhattan")

clientNumber = 0

n = network()
n.send((p1.x, p1.y))

