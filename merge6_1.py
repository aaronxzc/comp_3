import pygame
import time
import random
import keyboardlayout as kl
import keyboardlayout.pygame as klp
import argparse


class InputBox:

    def __init__(self, x, y, w, h, text='',ref_text='',
        ref_text_color = (0,0,0),
        error_text_color = (255,0,0)
    ):

        # text related vars:

        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.ref_text = ref_text
        self.display_text = ref_text.replace(" ","_")
        self.error_text = (' '*len(ref_text))
        self.ref_text_color = ref_text_color
        self.error_text_color = error_text_color
        
        # Renders out the text: it has 3 layers to show the different colours
        self.ref_txt_surface = FONT.render(self.display_text, True, self.ref_text_color)
        self.txt_surface = FONT.render(text, True, self.color)
        self.error_text_surface = FONT.render(self.error_text, True, self.error_text_color)
        
        # Sets the input box to be active the instant the user joins the singleplayer screen
        self.active = True
        self.color = COLOR_ACTIVE

        self.ref_text_length = len(ref_text)



        

    def handle_event(self, event, ref_text_pos):
       
        if ref_text_pos >= self.ref_text_length:
            # Returns 2; user has finished typing
            return 2
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            # self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE

            if self.active:
                self.color = COLOR_ACTIVE            
            else:
                self.color = COLOR_INACTIVE

        if event.type == pygame.KEYDOWN:

            prs = event.key
            if self.active:
                # if event.key == pygame.K_RETURN:
                    # print(self.text)
                    # self.text = ''
                # elif event.key == pygame.K_BACKSPACE:
                    # self.text = self.text[:-1]
                if prs != pygame.K_LSHIFT and prs != pygame.K_RSHIFT and prs != pygame.K_BACKSPACE and prs != pygame.K_LCTRL and prs != pygame.K_RCTRL and prs != pygame.K_LSUPER and prs != pygame.K_CAPSLOCK and prs!= pygame.K_RETURN:
                    if event.unicode != self.ref_text[ref_text_pos]:
                        #print(event.key)
                        self.color = red
                                                                  
                        list_error_text = list(self.error_text)
                        list_error_text[ref_text_pos] = self.display_text[ref_text_pos]
                        self.error_text = "".join(list_error_text)

                        print(self.error_text)            
                        #print(self.ref_text[ref_text_pos])
                        
                        
                        self.txt_surface = FONT.render(self.text.replace(" ","_"), True, grey)
                        
                        self.error_text_surface = FONT.render(self.error_text, True, self.error_text_color)
                        self.ref_txt_surface = FONT.render(self.display_text, True, self.ref_text_color)
                        
                        
                        
                        
                    elif event.unicode == self.ref_text[ref_text_pos]:
                        self.text += event.unicode
                        self.color = COLOR_ACTIVE
                        # print(self.text)
                        
                        list_display_text = list(self.display_text)
                        list_display_text[ref_text_pos] = cursor_black
                        for char in range(0, ref_text_pos):
                            list_display_text[char] = ' '
                        self.display_text = "".join(list_display_text)

                        
                        self.txt_surface = FONT.render(self.text.replace(" ","_"), True, (grey))
                        
                        self.error_text_surface = FONT.render(self.error_text, True, self.error_text_color)
                        self.ref_txt_surface = FONT.render(self.display_text, True, self.ref_text_color)
                        
                        # Returns 1; user has correctly typed that character
                        return 1
                        
                        
                        
                        
                        
                        #ref_text_pos = ref_text_pos + 1
                # Re-render the text.
                
                
                

    def update(self):
        # Resize the box if the text is too long.
        width = max(1500, self.txt_surface.get_width()+10)
        self.rect.w = width
        

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        
        screen.blit(self.error_text_surface, (self.rect.x+5, self.rect.y+5))
        screen.blit(self.ref_txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

class GameState():
    def __init__(self):
        self.state = 'm_menu'

    def m_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    button_click("Lessons",660,450,600,60,grey,light_grey,"lsn_game")
                    button_click("Singleplayer",660,530,600,60,grey,light_grey,"mode_select")
                    button_click("Options",660,610,290,60,grey,light_grey,"options")
                    button_click("Quit",970,610,290,60,grey,light_grey,"quit")
                    button_click("Profile",1550,50,100,60,grey,light_grey,"profile")
                    button_click("Log Out",1670,50,100,60,grey,light_grey,"login")
                
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',120)
        TextSurf, TextRect = text_objects("KeyGlide", largeText)
        TextRect.center = ((display_width/2),(display_height/4))
        gameDisplay.blit(TextSurf, TextRect)

        button_draw("Lessons",660,450,600,60,grey,light_grey,"lsn_game")
        button_draw("Singleplayer",660,530,600,60,grey,light_grey,"mode_select")
        button_draw("Options",660,610,290,60,grey,light_grey,"options")
        button_draw("Quit",970,610,290,60,grey,light_grey,"quit")
        button_draw("Profile",1550,50,100,60,grey,light_grey,"profile")
        button_draw("Log Out",1670,50,100,60,grey,light_grey,"login")

        pygame.display.update()

    def sp_game(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            '''if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = 'm_menu'
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    button_click("Quit",970,610,290,60,grey,light_grey,"quit")'''

        gameDisplay.fill(white)
        # button_draw("Quit",970,610,290,60,grey,light_grey,"quit")
        parser = argparse.ArgumentParser()  
        parser.add_argument(
            'layout_name',
            nargs='?',
            type=kl.LayoutName,
            default=kl.LayoutName.QWERTY,
            help='the layout_name to use'
        )
        args = parser.parse_args()
        keyboard_example(args.layout_name)
        
            
        pygame.display.update()

    def lsn_game(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = 'm_menu'

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',120)
        TextSurf, TextRect = text_objects("Lessons", largeText)
        TextRect.center = ((display_width/2),(display_height/4))
        gameDisplay.blit(TextSurf, TextRect)
        
        pygame.display.update()
    
    def options(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = 'm_menu'

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',120)
        TextSurf, TextRect = text_objects("Options", largeText)
        TextRect.center = ((display_width/2),(display_height/4))
        gameDisplay.blit(TextSurf, TextRect)
        
        pygame.display.update()
    
    def profile(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = 'm_menu'

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',120)
        TextSurf, TextRect = text_objects("Profile", largeText)
        TextRect.center = ((display_width/2),(display_height/4))
        gameDisplay.blit(TextSurf, TextRect)
        
        pygame.display.update()

    def login(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = 'm_menu'

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',120)
        TextSurf, TextRect = text_objects("Login", largeText)
        TextRect.center = ((display_width/2),(display_height/4))
        gameDisplay.blit(TextSurf, TextRect)
        
        pygame.display.update()

    def retry(self):
        self.state = 'sp_game'
        
    
    def mode_select(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = 'm_menu'

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',120)
        TextSurf, TextRect = text_objects("Mode Selection", largeText)
        TextRect.center = ((display_width/2),(display_height/4))
        gameDisplay.blit(TextSurf, TextRect)
        
        pygame.display.update()        
    
    
    def state_manager(self):
        if self.state == 'm_menu':
            self.m_menu()
        if self.state == 'sp_game':
            self.sp_game()
        if self.state == 'lsn_game':
            self.lsn_game()
        if self.state == 'options':
            self.options()
        if self.state == 'profile':
            self.profile()
        if self.state == 'login':
            self.login()
        if self.state == 'retry':
            self.retry()
        if self.state == 'mode_select':
            self.mode_select()

layout_name = 'qwerty'

# General Setup
pygame.init()
clock = pygame.time.Clock()
game_state = GameState()

# Game Screen
display_width = 1920    
display_height = 1080
fps = 60
gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)
pygame.display.set_caption('KeyGlide')


# Colours
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
grey = (191,191,191)
dark_grey = ~pygame.Color('grey')
light_grey = (220, 220, 220)
light_black = (69, 69, 69)
dark_white = (242, 242, 242)
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
#FONT = pygame.font.Font('courier.ttf', 20)
#FONT = pygame.font.Font('RobotoMono-Regular.ttf', 20)
FONT = pygame.font.Font('UbuntuMono-Regular.ttf', 35)


 
block_color = (53,115,255)
 
car_width = 73
 
# carImg = pygame.image.load('racecar.png')

#cursors
cursor_black = '█'
cursor_white = '␣'
cursor_light = '░'
cursor_medium = '▒'
cursor_dark = '▓'



 
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()    

def button_click(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # checks if mouse is over button
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        if click[0] == 1 and action != None:
            
            if action == "quit":
                # Quits the application if the action is quit
                pygame.quit()
                quit()
            else:
                # action -> state_manager() -> screen function call in GameState class
                game_state.state = action


def button_draw(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

    else:
        # displays button normally when user is not hovering over it
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)



def get_keyboard(
    layout_name: kl.LayoutName,
    key_size: int,
    key_info: kl.KeyInfo
) -> klp.KeyboardLayout:
    keyboard_info = kl.KeyboardInfo(
        position=(500, 100),
        padding=2,
        color=dark_white
    )
    letter_key_size = (key_size, key_size)  # width, height
    keyboard_layout = klp.KeyboardLayout(
        layout_name,
        keyboard_info,
        letter_key_size,
        key_info
    )
    return keyboard_layout

def run_until_user_closes_window(
    screen: pygame.Surface,
    keyboard: klp.KeyboardLayout,
    key_size: int,
    released_key_info: kl.KeyInfo,
):
    pressed_key_info = kl.KeyInfo(
        margin=14,
        color=light_black,
        txt_color=pygame.Color('white'),
        txt_font=pygame.font.SysFont('Arial', key_size//4),
        txt_padding=(key_size//6, key_size//10)
    )
    
    ref_text_pos = 0
    txt2type = text_generator_sp(83)
    input_box1 = InputBox(250, 500, 500, 100, '',txt2type)
    input_boxes = [input_box1]
    done = False

    while not done:
        for event in pygame.event.get():
            
            if game_state.state == 'quit':
                done = True
                pygame.quit()
                quit()
            elif game_state.state != 'sp_game':
                done = True
                
                
            '''elif event.key == pygame.K_ESCAPE:
                playing = False
                break'''

            key = keyboard.get_key(event)
            

            if event.type == pygame.KEYDOWN:
                keyboard.update_key(key, pressed_key_info)
            if event.type == pygame.KEYUP:
                keyboard.update_key(key, released_key_info)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    button_click("Quit",970,610,290,60,grey,light_grey,"m_menu")
                    button_click("Next",660,610,290,60,grey,light_grey,"retry")
            for box in input_boxes:
                finished = box.handle_event(event, ref_text_pos)
                if finished == 1:
                    ref_text_pos = ref_text_pos + 1
            
                elif finished == 2:
                    print("finish")
                    done = True
                    
                    

        for box in input_boxes:
            box.update()

        screen.fill(white)
        for box in input_boxes:
            box.draw(screen)

        button_draw("Quit",970,610,290,60,grey,light_grey,"quit")
        button_draw("Next",660,610,290,60,grey,light_grey,"retry")
        

        keyboard.draw(screen)
        
        pygame.display.update()
    #game_state.state = 'm_menu'


def keyboard_example(layout_name: kl.LayoutName):
    # block events that we don't want
    # pygame.event.set_blocked(None)
    # pygame.event.set_allowed([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT])

    key_size = 60
    key_info = kl.KeyInfo(
        margin=10,
        color=light_grey,
        txt_color=dark_grey,
        txt_font=pygame.font.SysFont('Arial', key_size//4),
        txt_padding=(key_size//6, key_size//10)
    )
    keyboard = get_keyboard(layout_name, key_size, key_info)


    keyboard.draw(gameDisplay)
    pygame.display.update()
    run_until_user_closes_window(gameDisplay, keyboard, key_size, key_info)

def text_generator_sp(max_chars):
    file = open('top1000.txt', 'r')
    file_list = []
    for line in file:
        stripped_line = line.strip()
        file_list.append(stripped_line)

    gen_txt = []
    gen_txt_str = ''

    while len(gen_txt_str) < max_chars:
        random_line_no = random.randint(0,len(file_list)-1)
        random_word = file_list[random_line_no]
        random_word_length = len(random_word)
        gen_txt.append(random_word)
        gen_txt_str = " ".join(gen_txt)

    if len(gen_txt_str) > max_chars:
        gen_txt_str = gen_txt_str[:-(random_word_length+1)]


    file.close()
    return gen_txt_str



while True:
    game_state.state_manager()
    clock.tick(fps)
