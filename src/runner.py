import pygame
from sys import exit
from random import randint

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = test_font.render(f'Score: {current_time}',False,(64,64,64))
    score_rect = score_surface.get_rect(center = (400,50))
    screen.blit(score_surface, score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            if obstacle_rect.bottom  == 300: screen.blit(snail_surface, obstacle_rect)
            else : screen.blit(fly_surface, obstacle_rect)
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
            
        return obstacle_list
    else : return []

def collissions(player,obstacle):
    if obstacle:
        for obstacle_rect in obstacle:
            if player.colliderect(obstacle_rect): return False
    return True

def player_animation():
    global player_surface, player_index 
    if player_rect.bottom < 300 :
        player_surface = player_jump
    else :
        player_index += 0.1
        if player_index >= len(player_walk): player_index = 0 
        player_surface = player_walk[int(player_index)]
    # play walking animation if the player is on floor
    # display the jump surface when player is not on floor
    
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')

clock = pygame.time.Clock()
test_font = pygame.font.Font('/Users/mukulsharma/Desktop/CS/python/pygame/font/Pixeltype.ttf', 50)  
start_time = 0
game_active = False
score = display_score()

sky_surface = pygame.image.load('/Users/mukulsharma/Desktop/CS/python/pygame/graphics/Sky.png').convert()
ground_surface = pygame.image.load('/Users/mukulsharma/Desktop/CS/python/pygame/graphics/ground.png').convert()

#score_surface = test_font.render('My game', False, (64,64,64)) 
#score_rect = score_surface.get_rect(center = (400, 50))

# SNAIL
snail_frame1 = pygame.image.load('/Users/mukulsharma/Desktop/CS/python/pygame/graphics/snail1.png').convert_alpha()
snail_frame2 = pygame.image.load('/Users/mukulsharma/Desktop/CS/python/pygame/graphics/snail2.png').convert_alpha()
snail_frame_index = 0
snail_frames = [snail_frame1, snail_frame2]

# Fly
fly_frame1 =  pygame.image.load('/Users/mukulsharma/Desktop/CS/python/pygame/graphics/Fly1.png').convert_alpha()
fly_frame2 =  pygame.image.load('/Users/mukulsharma/Desktop/CS/python/pygame/graphics/Fly2.png').convert_alpha()
fly_frame_index = 0
fly_frames = [fly_frame1, fly_frame2]
obstacle_rect_list = []

player_walk1 = pygame.image.load('/Users/mukulsharma/Desktop/CS/python/pygame/graphics/player_walk_1.png').convert_alpha()
player_walk2 = pygame.image.load('/Users/mukulsharma/Desktop/CS/python/pygame/graphics/player_walk_2.png').convert_alpha()
player_walk2 = pygame.image.load('/Users/mukulsharma/Desktop/CS/python/pygame/graphics/player_walk_2.png').convert_alpha()
player_walk = [player_walk1, player_walk2]
player_index = 0
player_jump = pygame.image.load('/Users/mukulsharma/Desktop/CS/python/pygame/graphics/jump.png').convert_alpha()

player_surface = player_walk[player_index]
player_rect = player_surface.get_rect(midbottom = (80,300))
player_gravity = 0

#Intro screen
player_stand = pygame.image.load('/Users/mukulsharma/Desktop/CS/python/pygame/graphics/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
#player_stand = pygame.transform.scale2x(player_stand)
#player_stand = pygame.transform.scale(player_stand, (150,300))
player_stand_rect = player_stand.get_rect(center = (400,200))
welcome_text = test_font.render("Welcome to Pixel Runner", False, (111,196,169))
welcome_text_rect = welcome_text.get_rect(center = (400, 80))
start_text = test_font.render("press SPACEBAR to start", False,  (111,196,169))
start_text_rect = start_text.get_rect(center = (400,330))


#loading FILL colour surfaces
#test_surface = pygame.Surface((100,200))
#test_surface.fill('Purple')

#Timer
obstacle_timer = pygame.USEREVENT + 1 # +1 is to avoid conflict with events reserved for pygame
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

while True:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:  
                    player_gravity = -20
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom == 300:  
                    player_gravity = -20
            if event.type == obstacle_timer:
                if randint(0,2):
                    obstacle_rect_list.append(snail_surface.get_rect(midbottom = (randint(900,1100),300)))
                else:
                    obstacle_rect_list.append(fly_surface.get_rect(midbottom = (randint(900,1100),200)))
            if event.type == snail_animation_timer:
                if snail_frame_index == 0 : snail_frame_index = 1
                else: snail_frame_index = 0
                snail_surface = snail_frames[snail_frame_index]
            if event.type == fly_animation_timer:
                if fly_frame_index == 0 : fly_frame_index = 1
                else: fly_frame_index = 0
                fly_surface = fly_frames[fly_frame_index]
        else :
               if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True  
                    start_time = int(pygame.time.get_ticks() / 1000)           
            
        
        #KEYBOARD INPUT USING EVENT            
        #if event.type == pygame.KEYDOWN:
            #print("keydown")
        #if event.key == pygame.K_SPACE:
            #print("jump")
        #if event.type == pygame.KEYUP:
            #print("keyUP")
        
        #MOUSE INPUT USING EVENT
        #if event.type == pygame.MOUSEBUTTONDOWN:
            #print('mouse pressed')
        #if event.type == pygame.MOUSEBUTTONUP:
            #print('mouse released')
        #if event.type == pygame.MOUSEMOTION:\
        #if player_rect.collidepoint(event.pos) : print("collided")  

    if game_active :
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        #pygame.draw.rect(screen,'#c0e8ec', score_rect, 6 , 3)
        #pygame.draw.rect(screen,'#c0e8ec', score_rect)
        #screen.blit(score_surface,score_rect)
        score = display_score()
        
        
        #snail_rect.left -= 4
        #if snail_rect.right <= 0 : snail_rect.left = 800
        
        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300 : player_rect.bottom = 300
        player_animation()
        screen.blit(player_surface, player_rect)
        
        # Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        
        # Collission
        game_active = collissions(player_rect, obstacle_rect_list)

        
        #Drawing and coloring using rectangles etc.
        #pygame.draw.line(screen, 'Gold',(0,0),pygame.mouse.get_pos(),10) follows the mouse
        #pygame.draw.line(screen, color='Red', start_pos= (1,1), end_pos=(1,301), width = 10)
        #pygame.draw.ellipse(screen, 'Brown', pygame.Rect(50,200,100,100))
        
        #MOUSE input
        #if player_rect.colliderect(snail_rect): print("collision")
        #mouse_pos = pygame.mouse.get_pos()
        #if player_rect.collidepoint(mouse_pos): print(pygame.mouse.get_pressed())
        
        #KEYBOARD input
        #keys = pygame.key.get_pressed()
        #if keys[pygame.K_SPACE]: print("JUMP !!")
        
    else : 
        screen.fill((94,129,162))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(start_text, start_text_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80,300)
        player_gravity = 0
        
        score_message = test_font.render(f'Your score : {score}', False, (111,196,169))
        
        score_message_rect = score_message.get_rect(center = (400,80))
        if score == 0:
            screen.blit(welcome_text, welcome_text_rect)
        else:
            screen.blit(score_message, score_message_rect)
        
    pygame.display.update()
    clock.tick(60)