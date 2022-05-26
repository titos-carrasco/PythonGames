import pygame

from lge.LittleGameEngine import LittleGameEngine
from lge.Sprite import Sprite
from lge.Rectangle import Rectangle


class Tortuga(Sprite):

    def __init__(self, iname, dir, x, y, velocity=120):
        super().__init__(iname, (x, y))

        # acceso a LGE
        self.lge = LittleGameEngine.getInstance()

        # mis atributos
        self.setTag("tortuga")
        self.enableCollider(True, True)
        self.dir = dir
        self.velocity = velocity

    # @Override
    def onUpdate(self, dt):
        self.nextImage(dt, 0.5)

        cw, ch = self.lge.getCameraSize()

        x, y = self.getPosition()
        w, h = self.getSize()

        if(self.dir == "R"):
            x = x + self.velocity * dt
            if(x > cw):
                x = 0 - w
        else:
            x = x - self.velocity * dt
            if(x + w < 0):
                x = cw - 1

        self.setPosition(x, y)

    # @Override
    def onCollision(self, dt, gobjs):
        pass
