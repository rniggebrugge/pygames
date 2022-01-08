from random import randint
import numpy as np

class Field():
    
    def __init__(self, w, h):
        self.monsters = []
        self.width = w
        self.height = h
        self.field = np.zeros((w,h))
        self.build_walls()
        for x in range(w):
            self.field[x,0]=randint(1,5)
            self.field[x,h-1]=randint(1,5)
        for y in range(h):
            self.field[0,y]=randint(1,5)
            self.field[w-1,y]=randint(1,5)
    
    def build_walls(self):
        total_area = self.width*self.height
        to_build = 0.15*total_area
        built = 0
        while built<to_build:
            length = randint(4,13)
            orientation = randint(0,1)
            start_x = randint(1,self.width-3)
            start_y = randint(1, self.height-3)
            for i in range(length):
                px, py = start_x, start_y
                if orientation:
                    px+=i
                else:
                    py+=i
                if px>=self.width or py>=self.height:
                    break
                if self.brick_at(px, py):
                    continue
                self.field[px,py]=randint(1,5)
                built+=1

                            
    def add_monsters(self, number):
        for i in range(number):
            self.monsters.append((4,3))
            
    def update_monsters(self, xpos, ypos):
        for i in range(len(self.monsters)):
            x = self.monsters[i][0]
            y = self.monsters[i][1]
            if randint(0,10)<7:
                r=randint(1,4)
                if r==1:
                    x-=1
                elif r==2:
                    x+=1
                elif r==3:
                    y-=1
                else:
                    y+=1
            elif randint(0,1):
                if xpos>x:
                    x+=1
                else:
                    x-=1
            else:
                if ypos>y:
                    y+=1
                else:
                    y-=1
            if not self.brick_at(x,y):
                self.monsters[i]=(x,y)

    # def add_monsters(self, number):
    #     for i in range(number):
    #         self.monsters.append((4,3, randint(0,3)))
            
    # def update_monsters(self, xpos, ypos):
    #     for i in range(len(self.monsters)):
    #         x = self.monsters[i][0]
    #         y = self.monsters[i][1]
    #         d = self.monsters[i][2]
    #         if d==0:
    #             x+=1
    #         elif d==1:
    #             y+=1
    #         elif d==2:
    #             x-=1
    #         else:
    #             y-=1
    #         if not self.brick_at(x,y):
    #             self.monsters[i]=(x,y,d)
    #         else:
    #             if randint(0,4):
    #                 # with 80% chance make reasonable decision
    #                 if randint(0,1):
    #                     if xpos>x:
    #                         d=0
    #                     elif xpos<x:
    #                         d=2
    #                     elif ypos>y:
    #                         d=1
    #                     else:
    #                         d=3
    #                 else:
    #                     if ypos>y:
    #                         d=1
    #                     elif ypos<y:
    #                         d=3
    #                     elif xpos>x:
    #                         d=0
    #                     else:
    #                         d=2
    #             else:
    #                 d=randint(0,3)
    #             self.monsters[i]=(self.monsters[i][0], self.monsters[i][1],d)
            
    def brick_at(self, x, y):
        x,y = int(x), int(y)
        return self.field[x,y]>0
    
    def monster_at(self, x, y):
        for m in self.monsters:
            if m[:2]==(x,y):
                return True
        return False
    
    def window(self, x,y, w, h):
        x = int(x-w/2)
        y = int(y-h/2)
        sub = np.zeros((w,h))
        for xx in range(w):
            for yy in range(h):
                if x+xx<0 or y+yy<0 \
                    or (x+xx)>=self.width or (y+yy)>=self.height:
                        sub[xx,yy]=0
                else:
                    sub[xx,yy]=self.field[x+xx,y+yy]
                    for m in self.monsters:
                        if m[:2]==(x+xx,y+yy):
                            sub[xx,yy]=99
                            break
        return sub