# import the pygame library and initialise the game engine
import pygame
pygame.init()


# Open a new window, caption it "pong"
screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("Pong")


#ball variadles
bx = 350
by = 250
bVx = 5
bVy = 5


# here's the variable that runs our game loop
doExit = False

p1x = 20
p1y = 200
p2x = 660
p2y = 200
p1Score = 0
p2Score = 0
# The clock will be used to control how fast the screen update
clock = pygame.time.Clock()

while not doExit: #Game loop
    
    #event queue stuff
    clock.tick(60) #set the fps
    
    for event in pygame.event.get(): #check if user did something
        if event.type == pygame.QUIT: #check if user clicked close
            doExit = True #Flag that we are done so we exit game loop
   
    
    #game logic will go here------------
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        p1y-=5
    if keys[pygame.K_s]:
        p1y+=5
    
    if keys[pygame.K_UP]:
        p2y-=5
    if keys[pygame.K_DOWN]:
        p2y+=5         
            
    #left paddle
    if bx < p1x + 20 and by + 20 > p1y and by < p1y + 100:
        bVx *= -1
            
    #right paddle
    if bx+20 > p2x and by + 20 > p2y and by < p2y + 100:
        bVx *= -1        
    
        #reflect ball off side walls of screen     
    
    if by < 0 or by + 20 > 500:
        bVy *= -1
        
    if bx+20 > 700:
        bVx *= -1
        p1Score += 1
        
        
    if bx < 0:
        bVx *= -1
        p2Score += 1
        
    # ball movement
    bx += bVx
    by += bVy
    
    #render section----------------------- 
    screen.fill((0,0,0))
            
    pygame.draw.line(screen, (240,248,255), [349,0],[349,500], 5)
    
    pygame.draw.rect(screen, (218,112,214), (p1x, p1y, 20, 100), 1)
    
    pygame.draw.rect(screen, (255,207,241), (p2x, p2y, 20, 100), 1)
    
    pygame.draw.circle(screen, (230,230,250), (bx,by), 10)
    
    font = pygame.font.Font(None, 74)
    text = font.render(str(p1Score), 1, (190,190,190))
    screen.blit(text, (250,10))
    text = font.render(str(p2Score), 1, (190,190,190))
    screen.blit(text, (420,10))
    
    pygame.display.flip()           
#END GAME LOOP----------------------------------------------------------
            
pygame.quit()#when game is done close down pygame


