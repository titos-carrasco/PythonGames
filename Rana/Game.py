import pygame

from lge.LittleGameEngine import LittleGameEngine
from lge.Sprite import Sprite
from lge.GameObject import GameObject

from Rana import Rana
from Vehiculo import Vehiculo
from Tortuga import Tortuga
from Tronco import Tronco


class Game():

    def __init__(self):
        self.winSize = (544, 416)

        self.lge = LittleGameEngine(self.winSize, "La Rana", (0, 0, 0))
        self.lge.setOnMainUpdate(self.onMainUpdate)
        self.lge.showColliders((255, 0, 0))

        # cargamos los recursos que usaremos
        resourceDir = "./resources"
        self.lge.loadImage("fondo", resourceDir + "/world.png")
        self.lge.loadImage("rana-idle", resourceDir + "/rana-idle.png")
        self.lge.loadImage("rana-dead", resourceDir + "/rana-dead.png")
        self.lge.loadImage("rana-up", resourceDir + "/rana-up*.png")
        self.lge.loadImage("rana-down", resourceDir + "/rana-up*.png", 1, (False, True))
        self.lge.loadImage("rana-left", resourceDir + "/rana-left*.png")
        self.lge.loadImage("rana-right", resourceDir + "/rana-left*.png", 1, (True, False))
        self.lge.loadImage("auto-azul", resourceDir + "/auto_azul.png")
        self.lge.loadImage("auto-rojo", resourceDir + "/auto_rojo.png", 1 , (True, False))
        self.lge.loadImage("tortuga", resourceDir + "/tortuga_*.png")
        self.lge.loadImage("tronco-largo", resourceDir + "/tronco_largo.png")

        # el fondo
        fondo = Sprite("fondo", (0, 0))
        self.lge.addGObject(fondo, 0)


        # el hogar
        for i in range(5):
            home = GameObject((42 + i * 108, 22), (30, 30));
            home.enableCollider(True);
            home.setTag("home-" + str(i));
            self.lge.addGObject(home, 1);

        # las tortugas
        tortuga = Tortuga("tortuga", "R", 10, 60, 1)
        self.lge.addGObject(tortuga, 1)

        # los troncos
        tronco = Tronco("tronco-largo", "R", 80, 100, 2)
        self.lge.addGObject(tronco, 1)

        tronco = Tronco("tronco-largo", "R", 200, 172, 2)
        self.lge.addGObject(tronco, 1)

        # el agua
        agua = GameObject((0, 53), (544, 144));
        agua.enableCollider(True);
        agua.setTag("agua");
        self.lge.addGObject(agua, 1);

        # los vehiculos
        car = Vehiculo("auto-azul", "R", 10, 310)
        self.lge.addGObject(car, 1)
        car = Vehiculo("auto-rojo", "L", 190, 238, 1)
        self.lge.addGObject(car, 1)

        # la rana
        rana = Rana(255, 380)
        self.lge.addGObject(rana, 1)

    def onMainUpdate(self, dt):
        # abortamos con la tecla Escape
        if (self.lge.keyPressed(pygame.K_ESCAPE)):
            self.lge.quit()

    # main loop
    def run(self, fps):
        self.lge.run(fps)


# show time
game = Game()
game.run(60)
print("Eso es todo!!!")

