import pygame
import time

from lge.LittleGameEngine import LittleGameEngine
from lge.Sprite import Sprite
from lge.Rectangle import Rectangle


class Rana(Sprite):

    def __init__(self, x, y):
        super().__init__("rana-idle", (x, y))

        # acceso a LGE
        self.lge = LittleGameEngine.getInstance()
        w, h = self.lge.getCameraSize()
        self.setBounds(Rectangle((3, 20), (w - 6, h - 22)))

        # mis atributos
        self.x0, self.y0 = x, y
        self.enableCollider(True, True)
        self.start()

    def start(self):
        self.moving = False
        self.alive = True
        self.tdead = 0
        self.setPosition(self.x0, self.y0)
        self.setImage("rana-up", 0)
        self.obgobj = None

    # @Override
    def onUpdate(self, dt):
        if(not self.alive):
            t = time.time()
            if(t - self.tdead > 3):
                self.start()
            return

        pixels = 36

        x, y = self.getPosition()

        if(not self.moving):
            if (self.lge.keyPressed(pygame.K_UP)):
                self.setPosition(x, y - pixels)
                self.setImage("rana-up", 1)
                self.moving = True
            elif (self.lge.keyPressed(pygame.K_DOWN)):
                self.setPosition(x, y + pixels)
                self.setImage("rana-down", 1)
                self.moving = True
            elif (self.lge.keyPressed(pygame.K_LEFT)):
                self.setPosition(x - pixels, y)
                self.setImage("rana-left", 1)
                self.moving = True
            elif (self.lge.keyPressed(pygame.K_RIGHT)):
                self.setPosition(x + pixels, y)
                self.setImage("rana-right", 1)
                self.moving = True
        else:
            if(not self.lge.keyPressed(pygame.K_UP) and
               not self.lge.keyPressed(pygame.K_DOWN) and
               not self.lge.keyPressed(pygame.K_LEFT) and
               not self.lge.keyPressed(pygame.K_RIGHT)):
                self.nextImage();
                self.moving = False

    # @Override
    def onCollision(self, dt, gobjs):
        if(not self.alive):
            return

        for gobj in gobjs:
            tag = gobj.getTag()
            if(tag == "agua" or tag == "auto"):
                self.setImage("rana-dead")
                self.tdead = time.time()
                self.alive = False
                return
            if(tag == "tronco"):
                return

