import pygame


DisplaySizeX,DisplaySizeY = (500,500)

Screen = pygame.display.set_mode((DisplaySizeX,DisplaySizeY))

GravityStr = 10
clock = pygame.time.Clock()
fps = 60

class ball():
    def __init__(self):
        self.Color = (255,255,255)
        self.Pos = [250,250]
        self.Size = 10
        self.Mass = 10
        self.Aceleration = 0

        self.Collisions = False
        
    def groundCheck(self):
        if self.Pos[1] >= 400-self.Size:
            #print("hit Ground enganged feedback")
            self.Collisions = True
        elif self.Aceleration <= 0:
            self.Collisions = False
            #print("no")

    def physicCheck(self):
        self.Gravity()
        self.Transfer()


    def Gravity(self):
        if self.Collisions == False:
            self.Aceleration += ((GravityStr * self.Mass) * delta)
            self.Pos[1] += self.Aceleration
            if self.Pos[1] >= 400-self.Size:
                self.Pos[1] = 400-self.Size

    def Transfer(self):
        if self.Collisions == True:
            self.Aceleration -= ((GravityStr * self.Mass) * delta)
            self.Pos[1] -= self.Aceleration 
            if self.Pos[1] >= 400-self.Size:
                self.Pos[1] = 400-self.Size

ball1 = ball()
ball2 = ball()
ball3 = ball()


ball1.Pos = [300,100]
ball2.Pos = [200,200]
ball3.Pos = [100,300]


def deltaTime():
    deltatime = (clock.tick(fps)/1000)
    return(deltatime)
    
delta = deltaTime()

while True:
    delta = deltaTime()

    ball1.groundCheck()
    ball1.physicCheck()

    ball2.groundCheck()
    ball2.physicCheck()

    ball3.groundCheck()
    ball3.physicCheck()

    Screen.fill((0,0,0))
    pygame.draw.line(Screen,(255,255,255),[0,400],[500,400])

    pygame.draw.circle(Screen, ball1.Color, ball1.Pos, ball1.Size)
    pygame.draw.circle(Screen, ball2.Color, ball2.Pos, ball2.Size)
    pygame.draw.circle(Screen, ball3.Color, ball3.Pos, ball3.Size)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()