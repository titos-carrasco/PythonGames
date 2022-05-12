import pygame

from lge.LittleGameEngine import LittleGameEngine
from lge.Sprite import Sprite
from lge.Rectangle import Rectangle


class Tortuga(Sprite):

    def __init__(self, iname, dir, x, y, pixels=2):
        super().__init__(iname, (x, y))

        # acceso a LGE
        self.lge = LittleGameEngine.getInstance()

        # los eventos que recibiremos
        self.setOnEvents(LittleGameEngine.E_ON_UPDATE)
        self.setOnEvents(LittleGameEngine.E_ON_COLLISION)

        # mis atributos
        self.setTag("tortuga")
        self.enableCollider(True)
        self.dir = dir
        self.pixels = pixels

    def onUpdate(self, dt):
        self.nextImage(dt, 0.5)

        cw, ch = self.lge.getCameraSize()

        x, y = self.getPosition()
        w, h = self.getSize()

        if(self.dir == "R"):
            x = x + self.pixels
            if(x > cw):
                x = 0 - w
        else:
            x = x - self.pixels
            if(x + w < 0):
                x = cw - 1

        self.setPosition(x, y)

    def onCollision(self, dt, gobjs):
        pass
