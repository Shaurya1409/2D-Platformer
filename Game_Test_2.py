import pygame
from pygame import *

win_width = 800
win_height = 640
half_width = 400
half_height = 320
crash = False
box = None
game_over = False
game_won = False
class Platform(pygame.sprite.Sprite):
    def __init__(self,x,y,block_type):
        pygame.sprite.Sprite.__init__(self)

        d = {
             "ba": "boxAlt.png",
             "be": "boxExplosive.png",
             "bw": "brickWall.png",
             "bg": "bridgeLogs.png",
             "tl": "tochLit.png",
             "gc": "grassCenter.png",
             "gl": "grassCliffLeft.png",
             "gs": "grass.png",
             "gr": "grassCliffRight.png",
             "gm": "grassMid.png",
             "rk": "keyRed.png",
             "bk": "keyBlue.png",
             "gk": "keyGreen.png",
             "wm": "liquidWater.png",
             "wt": "liquidWaterTop_mid.png",
             "ct": "cactus.png",
             "cc": "castleCenter.png",
             "c1": "castle.png",
             "cl": "castleCliffLeft.png",
             "cr": "castleCliffRight.png",
             "sn": "snow.png",
             "sl": "snowCliffLeft.png",
             "sr": "snowCliffRight.png",
             "sc": "snowCenter.png",
             "s1": "rock.png",
             "dm": "door_closedMid.png",
             "dt": "door_closedTop.png",
             "d1": "door_openMid.png",
             "d2": "door_openTop.png",
             "ww": "window.png",
             "lm": "liquidLava.png",
             "lt": "liquidLavaTop_mid.png",
             "in": "instructions.png",
             "cm": "castleMid.png",
             "sk": "cloud1.png"
             }

        self.image = pygame.image.load(d[block_type]).convert_alpha()
        self.image = pygame.transform.scale(self.image,(32,32))
        self.rect = Rect(x,y,32,32)
    def update(self):
        pass


class ExitBlock(Platform):
    def __init__(self,x,y,Block_Type):
        Platform.__init__(self,x,y,Block_Type)
        self.type = Block_Type


class GameOverBox(Platform):
    def __init__(self,x,y,Block_Type):
        Platform.__init__(self, x, y, Block_Type)

class EnemyBox(Platform):
    def __init__(self,x,y,Block_Type):
        Platform.__init__(self, x, y, Block_Type)

class Collectible(Platform):
    def __init__(self,x,y,Block_Type):
        Platform.__init__(self, x, y, Block_Type)
        self.type = Block_Type

class Explosive(Platform):
    animate_1 = pygame.image.load("Ex1.png")
    animate_1 = pygame.transform.scale(animate_1, (32, 32))
    animate_2 = pygame.image.load("Ex2.png")
    animate_2 = pygame.transform.scale(animate_2, (32, 32))
    animate_3 = pygame.image.load("Ex3.png")
    animate_3 = pygame.transform.scale(animate_3, (32, 32))
    animate_4 = pygame.image.load("Ex4.png")
    animate_4 = pygame.transform.scale(animate_4, (32, 32))
    animate_5 = pygame.image.load("Ex5.png")
    animate_5 = pygame.transform.scale(animate_5, (32, 32))
    animate_6 = pygame.image.load("Ex6.png")
    animate_6 = pygame.transform.scale(animate_6, (32, 32))
    animate_7 = pygame.image.load("Ex7.png")
    animate_7 = pygame.transform.scale(animate_7, (32, 32))
    animate_8 = pygame.image.load("Ex8.png")
    animate_8 = pygame.transform.scale(animate_8, (32, 32))
    animate_9 = pygame.image.load("Ex9.png")
    animate_9 = pygame.transform.scale(animate_9, (32, 32))

    def __init__(self,x,y,Block_Type):
       Platform.__init__(self,x,y,Block_Type)
       self.counter = 0

    def update(self,group):
        global crash, game_over
        if self.counter == 0:
            self.image = Explosive.animate_1
        elif self.counter == 2:
            self.image = Explosive.animate_2
        elif self.counter == 4:
            self.image = Explosive.animate_3
        elif self.counter == 6:
            self.image = Explosive.animate_4
        elif self.counter == 8:
            self.image = Explosive.animate_5
        elif self.counter == 8:
            self.image = Explosive.animate_6
        elif self.counter == 10:
            self.image = Explosive.animate_7
        elif self.counter == 12:
            self.image = Explosive.animate_8
        elif self.counter == 14:
            self.image = Explosive.animate_9
        elif self.counter >= 16:
            self.kill()
            self.remove(group)
            crash = False
            game_over = True
            return
        self.counter += 1



class Player(pygame.sprite.Sprite):
    stand = pygame.image.load("p3_front.png")
    stand = pygame.transform.scale(stand, (32, 32))
    jump = pygame.image.load("p3_jump.png")
    jump = pygame.transform.scale(jump, (32, 32))
    walk_1 = pygame.image.load("p3_walk01.png")
    walk_1 = pygame.transform.scale(walk_1, (32, 32))
    walk_2 = pygame.image.load("p3_walk02.png")
    walk_2 = pygame.transform.scale(walk_2, (32, 32))
    walk_3 = pygame.image.load("p3_walk03.png")
    walk_3 = pygame.transform.scale(walk_3, (32, 32))
    walk_4 = pygame.image.load("p3_walk04.png")
    walk_4 = pygame.transform.scale(walk_4, (32, 32))
    walk_5 = pygame.image.load("p3_walk05.png")
    walk_5 = pygame.transform.scale(walk_5, (32, 32))
    walk_6 = pygame.image.load("p3_walk06.png")
    walk_6 = pygame.transform.scale(walk_6, (32, 32))
    walk_7 = pygame.image.load("p3_walk07.png")
    walk_7 = pygame.transform.scale(walk_7, (32, 32))
    walk_8 = pygame.image.load("p3_walk08.png")
    walk_8 = pygame.transform.scale(walk_8, (32, 32))
    walk_9 = pygame.image.load("p3_walk09.png")
    walk_9 = pygame.transform.scale(walk_9, (32, 32))
    walk_10 = pygame.image.load("p3_walk10.png")
    walk_10 = pygame.transform.scale(walk_10, (32, 32))
    walk_11 = pygame.image.load("p3_walk11.png")
    walk_11 = pygame.transform.scale(walk_11, (32, 32))

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.onGround = False
        self.faceright = True
        self.image = Player.stand
        self.rect = Rect(x, y, 32, 32)
        self.counter = 0
        self.airborn = True
        self.heart = 3
        self.rkey = False
        self.gkey = False
        self.bkey = False

    def update(self,up,down,left,right,platforms,enemies):
        if up:
            if self.onGround: self.yvel -= 10
        if down:
            pass
        if left:
            self.xvel = -8
            self.faceright = False
        if right:
            self.xvel = 8
            self.faceright = True
        if not self.onGround:
            self.yvel += 0.3
            if self.yvel > 100: self.yvel = 100
        if not(left or right):
            self.xvel = 0
        if self.yvel < 0 or self.yvel > 1.2:
            self.airborn = True

        self.rect.left += self.xvel
        self.collide(self.xvel, 0, platforms,enemies)
        self.rect.top += self.yvel
        self.onGround = False;
        self.collide(0, self.yvel, platforms,enemies)
        self.animate()

    def collide(self,xvel,yvel,platforms,enemies):
        global crash,box,game_over,game_won
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, ExitBlock):
                    if self.gkey and self.rkey and self.bkey:
                        game_won = True
                    else:
                        print("Door Locked")
                        self.rect.right = p.rect.left

                elif isinstance(p,Explosive):
                    crash = True
                    box = p
                elif isinstance(p,GameOverBox):
                    self.heart = 0
                elif isinstance(p,EnemyBox):
                    pass
                elif isinstance(p,Collectible):
                    if p.type == "rk":
                        self.rkey = True
                    elif p.type == "bk":
                        self.bkey = True
                    elif p.type == "gk":
                        self.gkey = True
                    p.kill()
                elif xvel > 0:
                    self.rect.right = p.rect.left
                    print("collide right")
                elif xvel < 0:
                    self.rect.left = p.rect.right
                    print("collide left")
                elif yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.airborn = False
                    self.yvel = 0
                elif yvel < 0:
                    self.rect.top = p.rect.bottom
        for e in enemies:
            if pygame.sprite.collide_rect(self,e):
                hurt = pygame.image.load("p3_hurt.png")
                hurt = pygame.transform.scale(hurt, (32, 32))
                if xvel > 0:
                    self.heart -= 1
                    self.rect.right = e.rect.left - 64
                    print("collide right")
                    self.updatechar(hurt)
                elif xvel < 0:
                    self.heart -= 1
                    self.rect.left = e.rect.right + 64
                    self.updatechar(hurt)
                elif yvel > 0:
                    self.rect.bottom = e.rect.top
                    self.yvel = -8
                    self.onGround = False
                    self.airborn = True
                    e.destroyed = True
                    print(e.destroyed)

                if self.heart == 0:
                    game_over = True

    def animate(self):
        if self.xvel > 0 or self.xvel < 0:
            self.walkloop()
            if self.airborn:
                self.updatechar(Player.jump)
        else:
            self.updatechar(Player.stand)
            if self.airborn:
                self.updatechar(Player.jump)


    def walkloop(self):
        if self.counter == 2:
            self.updatechar(Player.walk_1)
        elif self.counter == 4:
            self.updatechar(Player.walk_2)
        elif self.counter == 6:
            self.updatechar(Player.walk_3)
        elif self.counter == 8:
            self.updatechar(Player.walk_4)
        elif self.counter == 10:
            self.updatechar(Player.walk_5)
        elif self.counter == 12:
            self.updatechar(Player.walk_6)
        elif self.counter == 14:
            self.updatechar(Player.walk_7)
        elif self.counter == 16:
            self.updatechar(Player.walk_8)
        elif self.counter == 18:
            self.updatechar(Player.walk_9)
        elif self.counter == 20:
            self.updatechar(Player.walk_10)
        elif self.counter == 22:
            self.updatechar(Player.walk_11)
            self.counter = 0
        self.counter += 1
    def updatechar(self,animage):
        if not self.faceright:
            animage = pygame.transform.flip(animage,True,False)
        self.image = animage



class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

def complex_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t, _, _ = -l+half_width, -t+half_height, w, h
    l = min(0, l)
    l = max(-(camera.width-win_width), l)
    t = max(-(camera.height-win_height), t)
    t = min(0, t)
    return Rect(l, t, w, h)

class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        walk_01 = pygame.image.load("slimeWalk1.png")
        walk_01 = pygame.transform.scale(walk_01, (32, 32))
        self.xvel = 1
        self.yvel = 0
        self.onGround = False
        self.faceright = True
        self.image = walk_01
        self.rect = Rect(x, y, 32, 32)
        self.counter = 0
        self.airborn = True
        self.destroyed = False

    def update(self, platforms,entities,enemies):
        self.rect.left += self.xvel
        self.collide(self.xvel, 0, platforms, entities)
        self.rect.top += self.yvel
        self.onGround = False;
        self.collide(0, self.yvel, platforms, entities)

        if self.xvel > 0:
            self.faceright = True
        elif self.xvel < 0:
            self.faceright = False
        if not self.onGround:
            self.yvel += 0.3
            if self.yvel > 100:
                self.yvel = 100
        self.animate()

    def collide(self,xvel,yvel,platforms,entities):
        global game_over
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if xvel > 0:
                    self.rect.right = p.rect.left
                    self.xvel = -1*xvel
                    print("collide right")
                elif xvel < 0:
                    self.rect.left = p.rect.right
                    self.xvel = abs(xvel)
                    walk_01 = pygame.image.load("slimeWalk1.png")
                    walk_01 = pygame.transform.scale(walk_01, (32, 32))
                    self.updatechar(walk_01)
                    print("collide left")
                elif yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.airborn = False
                    self.yvel = 0
                elif yvel < 0:
                    self.rect.top = p.rect.bottom
        for i in entities:
            if pygame.sprite.collide_rect(self,i):
                if isinstance(i,Player):
                    i.heart -= 1
                    hurt = pygame.image.load("p3_hurt.png")
                    hurt = pygame.transform.scale(hurt, (32, 32))
                    i.updatechar(hurt)

                    if xvel > 0:
                        i.rect.left = self.rect.right + 64
                        self.rect.right = i.rect.left - 64
                        print("collide right")
                    elif xvel < 0:
                        i.rect.left = self.rect.right - 64
                        self.rect.right = i.rect.left + 64

                    if i.heart == 0:
                        game_over = True

    def animate(self):
        if self.destroyed:
            self.destroyloop()
        else:
            self.walkloop()

    def walkloop(self):
        walk_01 = pygame.image.load("slimeWalk1.png")
        walk_01 = pygame.transform.scale(walk_01,(32,32))
        walk_02 = pygame.image.load("slimeWalk2.png")
        walk_02 = pygame.transform.scale(walk_02, (32, 32))
        if self.counter == 8:
            self.updatechar(walk_01)
        elif self.counter == 16:
            self.updatechar(walk_02)
            self.counter = 0
        self.counter = self.counter + 1

    def destroyloop(self):
        dead = pygame.image.load("slimeDead.png")
        dead = pygame.transform.scale(dead,(32,32))
        for i in range(0,20):
            self.updatechar(dead)
        self.kill()

    def updatechar(self,animage):
        if self.faceright:
            animage = pygame.transform.flip(animage,True,False)
        self.image = animage

def main():
    global game_over
    pygame.init()
    screen = pygame.display.set_mode((win_width,win_height),0,32)
    pygame.display.set_caption("Collect All 3 Keys To Unlock Door and Win")
    timer = pygame.time.Clock()

    up = down = left = right = False
    bg = pygame.image.load("Sky.png").convert()
    entities = pygame.sprite.Group()
    player = Player(32,32*34)
    platforms = []
    x = y = 0
    level = [
            ["gc", "gc", "gc", "gc", "gc", "gc", "gc", "gc", "gc", "gc", "gc", "gc", "gc", "gc", "gc", "gc", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "dt"],
            ["gc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "d1", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "dm"],
            ["gc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "d1", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "sn", "sc"],
            ["gc", "gk", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "gl", "gm", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "sc"],
            ["gc", "gl", "gr", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "sc"],
            ["gc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "gm", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "sn", "  ", "  ", "sc"],
            ["gc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "sc"],
            ["gc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "sc"],
            ["gc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "sn", "  ", "  ", "  ", "sc"],
            ["gc", "  ", "  ", "  ", "  ", "ct", "  ", "  ", "  ", "  ", "  ", "ct", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "sc"],
            ["gc", "  ", "  ", "  ", "  ", "gl", "gm", "gm", "gm", "gm", "gm", "gr", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "sc"],
            ["gc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "s1", "  ", "  ", "  ", "s1", "  ", "  ", "  ", "  ", "  ", "sc"],
            ["gc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "sl", "sn", "sn", "sn", "sr", "  ", "  ", "  ", "  ", "  ", "sc"],
            ["gc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "sn", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "sc"],
            ["gc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "sc"],
            ["gc", "gl", "gr", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "sc"],
            ["gc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "sc"],
            ["gc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "bk", "  ", "s1", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "sc"],
            ["gc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "sn", "sn", "sn", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "sc"],
            ["gc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "d1", "  ", "  ", "sc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "sc"],
            ["gc", "  ", "  ", "gl", "gs", "gr", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "d1", "  ", "  ", "sc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "sc"],
            ["gc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cm", "  ", "  ", "sc", "  ", "  ", "s1", "  ", "  ", "s1", "  ", "  ", "  ", "  ", "sc"],
            ["gc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "sc", "  ", "  ", "sl", "sn", "sn", "sr", "  ", "  ", "  ", "  ", "sc"],
            ["gc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "tl", "  ", "  ", "  ", "cc", "  ", "  ", "sc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "sc"],
            ["gc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "gl", "gm", "gm", "gm", "gr", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cl", "cm", "cm", "cm", "cc", "  ", "  ", "sc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "sc"],
            ["gc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "sc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "sc"],
            ["gc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "sc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "sc"],
            ["gc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "sc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "sl", "sr", "  ", "sc"],
            ["gc", "ct", "  ", "  ", "  ", "ct", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cl", "cr", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "sc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "sc"],
            ["gc", "gl", "gm", "gm", "gm", "gr", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "sc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "sc"],
            ["gc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "sc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "sc"],
            ["gc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "sc", "  ", "  ", "s1", "  ", "  ", "  ", "s1", "  ", "  ", "  ", "sc"],
            ["gc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "gl", "gm", "gm", "gr", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "sl", "sn", "sn", "sn", "sr", "  ", "  ", "  ", "sc"],
            ["gc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "rk", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cl", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "sc"],
            ["gc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cm", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "s1", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "sc"],
            ["gc", "  ", "in", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cm", "cc", "cm", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "cc", "sn", "sn", "sn", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "sc"],
            ["gc", "gm", "gm", "gm", "gm", "wm", "wm", "wm", "wm", "wm", "wm", "wm", "wm", "wm", "wm", "wm", "cc", "lm", "lm", "lm", "lm", "lm", "lm", "cm", "cc", "cc", "cc", "cm", "lm", "lm", "lm", "lm", "lm", "lm", "cc", "sc", "sc", "sc", "sk", "sk", "sk", "sk", "sk", "sk", "sk", "sk", "sk", "sk", "sc"],
            ]
    for row in level:
        for col in row:
            if col == "  ":
                pass
            elif col == "tl" or col == "d1" or col == "d2" or col == "ct" or col == "s1" or col == "s2" or col == "in":
                enb = EnemyBox(x, y, col)
                platforms.append(enb)
                entities.add(enb)
            elif col == "dm" or col == "dt":
                e = ExitBlock(x, y,col)
                platforms.append(e)
                entities.add(e)
            elif col == "be":
                ex = Explosive(x, y,col)
                platforms.append(ex)
                entities.add(ex)
            elif col == "wm" or col == "wt" or col == "lm" or col == "lt" or col == "sk":
                gob = GameOverBox(x,y,col)
                platforms.append(gob)
                entities.add(gob)
            elif col == "rk" or col == "bk" or col == "gk":
                k = Collectible(x,y,col)
                platforms.append(k)
                entities.add(k)
            else:
                p = Platform(x,y,col)
                platforms.append(p)
                entities.add(p)
            x += 32
        y += 32
        x = 0

    total_level_width = len(level[0]) * 32
    total_level_height = len(level) * 32
    camera = Camera(complex_camera, total_level_width, total_level_height)
    entities.add(player)
    enemies = pygame.sprite.Group()
    enemies.add(Enemy(32*3,32*27))
    enemies.add(Enemy(32*7, 32 * 8))
    enemies.add(Enemy(32 * 32, 32 * 23))
    enemies.add(Enemy(32 * 40, 32 * 10))


    while 1:
        timer.tick(60)

        for e in pygame.event.get():
            if e.type == QUIT:
                raise SystemExit
            elif e.type == KEYDOWN:
                if e.key == K_UP:
                    up = True
                elif e.key == K_DOWN:
                    down = True
                elif e.key == K_LEFT:
                    left = True
                elif e.key == K_RIGHT:
                    right = True
            elif e.type == KEYUP:
                if e.key == K_UP:
                    up = False
                elif e.key == K_DOWN:
                    down = False
                elif e.key == K_LEFT:
                    left = False
                elif e.key == K_RIGHT:
                    right = False

        if game_over:
            for x1 in entities:
                x1.kill()
            for x2 in enemies:
                x2.kill()
            ls = pygame.image.load("Game_over.png")
            ls = pygame.transform.scale(ls, (800, 640))
            screen.blit(ls, (0, 0))
        else:
            screen.blit(bg,(0,0))
        camera.update(player)
        player.update(up, down, left, right, platforms,enemies)

        if game_won:
            for x1 in entities:
                x1.kill()
            for x2 in enemies:
                x2.kill()
            gw = pygame.image.load("Game_won.png")
            gw = pygame.transform.scale(gw, (800, 640))
            screen.blit(gw, (0, 0))

        for hostile in enemies:
            hostile.update(platforms,entities,enemies)

        if crash:
            box.update(entities)

        for s in enemies:
            screen.blit(s.image, camera.apply(s))

        for e in entities:
            if isinstance(e,ExitBlock):
                if player.bkey and player.rkey and player.gkey:
                    if e.type == "dm":
                        door = pygame.image.load("door_openMid.png")
                        door = pygame.transform.scale(door, (32, 32))
                        e.image = door
                    elif e.type == "dt":
                        door = pygame.image.load("door_openTop.png")
                        door = pygame.transform.scale(door, (32, 32))
                        e.image = door
            screen.blit(e.image, camera.apply(e))


        if game_over:
            for a in entities:
                a.kill()
            for b in enemies:
                b.kill()
            pygame.display.update()

        h_box = pygame.image.load("boxEmpty.png")
        h_box = pygame.transform.scale(h_box, (32, 32))
        heart = pygame.image.load("hud_heartFull.png")
        heart = pygame.transform.scale(heart, (32, 32))
        d = {3: "hud_3.png",2: "hud_2.png",1: "hud_1.png"}
        if player.rkey:
            screen.blit(h_box, (23*32, 32))
            rkey = pygame.image.load("hud_keyRed.png")
            rkey = pygame.transform.scale(rkey, (32, 32))
            screen.blit(rkey, (23*32, 32))
        if player.bkey:
            screen.blit(h_box, (22*32, 32))
            bkey = pygame.image.load("hud_keyBlue.png")
            bkey = pygame.transform.scale(bkey, (32, 32))
            screen.blit(bkey, (22 * 32, 32))
        if player.gkey:
            screen.blit(h_box, (21*32, 32))
            gkey = pygame.image.load("hud_keyGreen.png")
            gkey = pygame.transform.scale(gkey, (32, 32))
            screen.blit(gkey, (21 * 32, 32))

        try:
            no = pygame.image.load(d[player.heart])
            no = pygame.transform.scale(no, (32, 32))
            screen.blit(h_box,(32,32))
            screen.blit(h_box,(64, 32))
            screen.blit(heart,(64, 32))
            screen.blit(no ,(32, 32))
            pygame.display.update()

        except KeyError:
            game_over = True
            continue

if __name__ == '__main__':
    main()