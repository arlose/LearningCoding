# -*- coding:utf-8 -*-
import pygame
import sys
from pygame.locals import *
import random

Width = 1500
Height = 800
white = 255,255,255
blue = 100,0,200

Xoffset = 40
Yoffset = 360
 
pygame.init()
screen = pygame.display.set_mode((Width, Height), pygame.RESIZABLE, 0)
pygame.display.set_caption("Poker")

sample = pygame.image.load('../../PokerImages/card_CA.png')
size = sample.get_rect().size # 455*680

pokers = []

pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_CA.png'),(int(size[0]/2), int(size[1]/2))), 0x0E))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_C2.png'),(int(size[0]/2), int(size[1]/2))), 0x02))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_C2.png'),(int(size[0]/2), int(size[1]/2))), 0x02))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_C3.png'),(int(size[0]/2), int(size[1]/2))), 0x03))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_C4.png'),(int(size[0]/2), int(size[1]/2))), 0x04))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_C5.png'),(int(size[0]/2), int(size[1]/2))), 0x05))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_C6.png'),(int(size[0]/2), int(size[1]/2))), 0x06))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_C7.png'),(int(size[0]/2), int(size[1]/2))), 0x07))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_C8.png'),(int(size[0]/2), int(size[1]/2))), 0x08))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_C9.png'),(int(size[0]/2), int(size[1]/2))), 0x09))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_CT.png'),(int(size[0]/2), int(size[1]/2))), 0x0A))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_CJ.png'),(int(size[0]/2), int(size[1]/2))), 0x0B))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_CQ.png'),(int(size[0]/2), int(size[1]/2))), 0x0C))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_CK.png'),(int(size[0]/2), int(size[1]/2))), 0x0D))

pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_DA.png'),(int(size[0]/2), int(size[1]/2))), 0x1E))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_D2.png'),(int(size[0]/2), int(size[1]/2))), 0x12))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_D3.png'),(int(size[0]/2), int(size[1]/2))), 0x13))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_D4.png'),(int(size[0]/2), int(size[1]/2))), 0x14))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_D5.png'),(int(size[0]/2), int(size[1]/2))), 0x15))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_D6.png'),(int(size[0]/2), int(size[1]/2))), 0x16))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_D7.png'),(int(size[0]/2), int(size[1]/2))), 0x17))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_D8.png'),(int(size[0]/2), int(size[1]/2))), 0x18))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_D9.png'),(int(size[0]/2), int(size[1]/2))), 0x19))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_DT.png'),(int(size[0]/2), int(size[1]/2))), 0x1A))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_DJ.png'),(int(size[0]/2), int(size[1]/2))), 0x1B))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_DQ.png'),(int(size[0]/2), int(size[1]/2))), 0x1C))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_DK.png'),(int(size[0]/2), int(size[1]/2))), 0x1D))

pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_SA.png'),(int(size[0]/2), int(size[1]/2))), 0x2E))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_S2.png'),(int(size[0]/2), int(size[1]/2))), 0x22))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_S3.png'),(int(size[0]/2), int(size[1]/2))), 0x23))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_S4.png'),(int(size[0]/2), int(size[1]/2))), 0x24))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_S5.png'),(int(size[0]/2), int(size[1]/2))), 0x25))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_S6.png'),(int(size[0]/2), int(size[1]/2))), 0x26))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_S7.png'),(int(size[0]/2), int(size[1]/2))), 0x27))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_S8.png'),(int(size[0]/2), int(size[1]/2))), 0x28))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_S9.png'),(int(size[0]/2), int(size[1]/2))), 0x29))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_ST.png'),(int(size[0]/2), int(size[1]/2))), 0x2A))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_SJ.png'),(int(size[0]/2), int(size[1]/2))), 0x2B))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_SQ.png'),(int(size[0]/2), int(size[1]/2))), 0x2C))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_SK.png'),(int(size[0]/2), int(size[1]/2))), 0x2D))

pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_HA.png'),(int(size[0]/2), int(size[1]/2))), 0x3E))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_H2.png'),(int(size[0]/2), int(size[1]/2))), 0x32))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_H3.png'),(int(size[0]/2), int(size[1]/2))), 0x33))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_H4.png'),(int(size[0]/2), int(size[1]/2))), 0x34))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_H5.png'),(int(size[0]/2), int(size[1]/2))), 0x35))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_H6.png'),(int(size[0]/2), int(size[1]/2))), 0x36))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_H7.png'),(int(size[0]/2), int(size[1]/2))), 0x37))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_H8.png'),(int(size[0]/2), int(size[1]/2))), 0x38))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_H9.png'),(int(size[0]/2), int(size[1]/2))), 0x39))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_HT.png'),(int(size[0]/2), int(size[1]/2))), 0x3A))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_HJ.png'),(int(size[0]/2), int(size[1]/2))), 0x3B))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_HQ.png'),(int(size[0]/2), int(size[1]/2))), 0x3C))
pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_HK.png'),(int(size[0]/2), int(size[1]/2))), 0x3D))

random.shuffle(pokers)
length = len(pokers)
length2 = int(length/2)
while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
 
    screen.fill(blue)
    for i in range(length2):
        screen.blit(pokers[i][0], (10+i*Xoffset,20))
    for i in range(length2):
        screen.blit(pokers[i+length2][0], (10+i*Xoffset,20+Yoffset))
    pygame.display.update()

