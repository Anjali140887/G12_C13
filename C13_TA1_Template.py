import pygame,sys,random
pygame.init()
clock=pygame.time.Clock()
screen = pygame.display.set_mode((400,600))
pygame.display.set_caption('Bird Game')
images={}
images["bg1"] = pygame.image.load("bg1.png").convert_alpha()
images["base"] = pygame.image.load("base.png").convert_alpha()
images["bird"] = pygame.image.load("bird.png").convert_alpha()
images["pipe"] = pygame.image.load("pipe.png").convert_alpha()
images["invertedpipe"]=pygame.transform.flip(images["pipe"], False, True)
class Bird:
    bird=pygame.Rect(100,250,30,30)
    speed=1
    g=0.5
    def flap(self):
        self.speed=-10
    def gravity(self):
        self.speed=self.speed+self.g
        self.bird.y=self.bird.y+self.speed
    def display(self):
        screen.blit(images["bird"],self.bird)

class Pipe:
    def __init__(self,x):
        self.gap=random.randint(150, 400)
        self.rtop=pygame.Rect(x,self.gap-400,40,320)
        self.rbot=pygame.Rect(x,self.gap+100,40,500)
    def move(self):
        self.rtop.x-=2
        self.rbot.x-=2
    def display(self):
        screen.blit(images["pipe"],self.rbot)
        screen.blit(images["invertedpipe"],self.rtop)
         
        
pipe1 = Pipe(150)    
        
bird1=Bird()
    
groundx=0
while True:
    screen.blit(images["bg1"],[0,0])
    bird1.gravity()
    groundx-=5
    if groundx < -330:
        groundx=0
    screen.blit(images["base"],[groundx,550])
    bird1.display()
    pipe1.display()
    pipe1.move()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird1.flap()

    
    pygame.display.update()   
    clock.tick(30)