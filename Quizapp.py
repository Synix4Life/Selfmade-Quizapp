import pygame
import csv
import random
import os

questionFile = "QuestionDocument.txt"

'''--------------------Colors--------------------'''
black = (0, 0, 0)
yellow = (255, 255, 0)
green = (0, 247, 0)
red = (255, 0, 0)
white = (255, 255, 255)


'''-------------------Image Loading--------------------'''
picture_1_1 = pygame.image.load(os.path.join('Images', 'pp1.jpg'))
picture_1_2 = pygame.image.load(os.path.join('Images', 'pp2.jpg.'))
picture_2_1 = pygame.image.load(os.path.join('Images', 'pp3.jpg'))
picture_2_2 = pygame.image.load(os.path.join('Images', 'pp2.jpg'))
picture_background = pygame.image.load(os.path.join('Images', 'background.jpg'))


'''-------------------Class--------------------'''
class button():
    def __init__(self, color, x, y, width, height):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)

        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)

    def is_Over(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False


'''--------------------Functions--------------------'''
def buttons():
    global questionButton, answer1Button, answer2Button, scoreButton, skipButton
    questionButton =button(white, xQ, yQ, widthQ, heightQ)
    answer1Button = button(white, xA_1, yA_1, widthA_1, heightA_1)
    answer2Button = button(white, xA_2, yA_1, widthA_1, heightA_1)
    scoreButton = button(white, xC, yC, widthC, heightC)
    skipButton = button(white, xS, yC, widthC, heightC)

def find_Question():
    def alreadyDoneQuestions(qIndex):
        if questionArray.__len__() == 0:
            return True
        else:
            for i in questionArray:
                if i == index:
                    return False
            return True    

    global direction
    questionArray = []
    mikroRun = True
    while(mikroRun):
        index = random.randint(1,40)
        if alreadyDoneQuestions:
            mikroRun = False
    direction = random.randint(1,2)
    with open(questionFile, "r") as file:
        fieldname = ["Number", "Question", "TrueAnswer", "WrongAnswer"]
        reader = csv.DictReader(file, fieldnames = fieldname)
        for line in reader:
            if line["Number"] == str(index):
                global question, answer1, answer2
                question = line["Question"]
                if direction == 1:
                    answer1 = line["TrueAnswer"]
                    answer2 = line["WrongAnswer"]
                elif direction == 2:
                    answer2 = line["TrueAnswer"]
                    answer1 = line["WrongAnswer"]

def question_Finished(accuracy):
    global count
    def method():
        global run
        if count == "3":
            run = False
            print("\n\n", "You won!!! Congratulations!!!")
        elif count == "-3":
            run = False
            print("\n\n", "You lost!")
        else:
            find_Question()
            buttons()
            text(count, answer1, answer2, question)
            redraw_Window(0)

    if accuracy == 0:
        count = int(count) + 1
        count = str(count)
        method()
    elif accuracy == 1:
        count = int(count) - 1
        count = str(count)
        method()

def redraw_StartWindow(number):
    TextSButton.draw(screen, white)
    answer1SButton.draw(screen, white)
    answer2SButton.draw(screen, white)
    answer3SButton.draw(screen, white)
    answer4SButton.draw(screen, white)
    screen.fill(black)
    screen.blit(textB, (0,0))
    if number == 1:
        screen.blit(selectedImage, (0,100))
        screen.blit(image1_2, (0,200))
        screen.blit(image2_1, (0,300))
        screen.blit(image2_2, (0,400))
    elif number == 2:
        screen.blit(image1_1, (0,100))
        screen.blit(selectedImage, (0,200))
        screen.blit(image2_1, (0,300))
        screen.blit(image2_2, (0,400))
    elif number == 3:
        screen.blit(image1_1, (0,100))
        screen.blit(image1_2, (0,200))
        screen.blit(selectedImage, (0,300))
        screen.blit(image2_2, (0,400))
    elif number == 4:
        screen.blit(image1_1, (0,100))
        screen.blit(image1_2, (0,200))
        screen.blit(image2_1, (0,300))
        screen.blit(selectedImage, (0,400))
    else:
        screen.blit(image1_1, (0,100))
        screen.blit(image1_2, (0,200))
        screen.blit(image2_1, (0,300))
        screen.blit(image2_2, (0,400))
    screen.blit(outputSB, (TextSButton.x + (TextSButton.width/2 - outputSB.get_width()/2), TextSButton.y + (TextSButton.height/2 - outputSB.get_height()/2)))
    screen.blit(outputA1, (answer1SButton.x + (answer1SButton.width/2 - outputA1.get_width()/2), answer1SButton.y + (answer1SButton.height/2 - outputA1.get_height()/2)))
    screen.blit(outputA2, (answer2SButton.x + (answer2SButton.width/2 - outputA2.get_width()/2), answer2SButton.y + (answer2SButton.height/2 - outputA2.get_height()/2)))
    screen.blit(outputA3, (answer3SButton.x + (answer3SButton.width/2 - outputA3.get_width()/2), answer3SButton.y + (answer3SButton.height/2 - outputA3.get_height()/2)))
    screen.blit(outputA4, (answer4SButton.x + (answer4SButton.width/2 - outputA4.get_width()/2), answer4SButton.y + (answer4SButton.height/2 - outputA4.get_height()/2)))

def redraw_Window(turn):
    questionButton.draw(win, white)
    answer1Button.draw(win, white)
    answer2Button.draw(win, white)
    scoreButton.draw(win, white)
    skipButton.draw(win, white)
    win.blit(bg, (0,0))
    win.blit(pic_Score, (xC,yC))
    win.blit(pic_Question, (xQ,yQ))
    if turn == 1:
        win.blit(selected1, (xA_1,yA_1))
        win.blit(pic_Answer2, (xA_2,yA_1))
        win.blit(pic_Skip, (xS,yC))
    elif turn == 2:
        win.blit(selected1, (xA_2,yA_1))
        win.blit(pic_Answer1, (xA_1,yA_1))
        win.blit(pic_Skip, (xS,yC))
    elif turn == 3:
        win.blit(selected2, (xS,yC))
        win.blit(pic_Answer1, (xA_1,yA_1))
        win.blit(pic_Answer2, (xA_2,yA_1))
    else:
        win.blit(pic_Answer1, (xA_1,yA_1))
        win.blit(pic_Answer2, (xA_2,yA_1))
        win.blit(pic_Skip, (xS,yC))
    text(count, answer1, answer2, question)
    win.blit(outputScore, (scoreButton.x + (scoreButton.width/2 - outputScore.get_width()/2), scoreButton.y + (scoreButton.height/2 - outputScore.get_height()/2)))
    win.blit(outputSkip, (skipButton.x + (skipButton.width/2 - outputSkip.get_width()/2), skipButton.y + (skipButton.height/2 - outputSkip.get_height()/2)))
    win.blit(outputAnswer1, (answer1Button.x + (answer1Button.width/2 - outputAnswer1.get_width()/2), answer1Button.y + (answer1Button.height/2 - outputAnswer1.get_height()/2)))
    win.blit(outputAnswer2, (answer2Button.x + (answer2Button.width/2 - outputAnswer2.get_width()/2), answer2Button.y + (answer2Button.height/2 - outputAnswer2.get_height()/2)))
    win.blit(outputQuestion, (questionButton.x + (questionButton.width/2 - outputQuestion.get_width()/2), questionButton.y + (questionButton.height/2 - outputQuestion.get_height()/2)))

def rightQuestion(n):
    global outprint
    if n == 0:
        outprint = "Richtige Antwort!"
        outPrintColor = green
    elif n == 1:
        outprint = "Falsche Antwort"
        outPrintColor = red

    def redraw_It():
        win.blit(bg, (0,0))
        win.blit(outputting, (screenWidth/2 - outputting.get_width()/2, screenHeight/2 - outputting.get_height()/2))

    if screenSizeStore == 1:
        font = pygame.font.SysFont('times new roman', 50)
    elif screenSizeStore == 2:
        font = pygame.font.SysFont('times new roman', 70)
    elif screenSizeStore == 3:
        font = pygame.font.SysFont('times new roman', 90)
    else: #screenSizeStore = 4
        font = pygame.font.SysFont('times new roman', 110)
    outputting = font.render(outprint, True, outPrintColor)

    wait = True
    while wait:
        pygame.time.delay(100)
        redraw_It()
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN:
                wait = False

        pygame.display.update()

def text(count, answer1, answer2, question):
    global outputScore, outputSkip, outputAnswer1, outputAnswer2, outputQuestion

    textScore = count
    textSkip = "Skip"
    textAnswer1 = answer1
    textAnswer2 = answer2
    textQuestion = question

    if screenSizeStore == 1:
        font2 = pygame.font.SysFont('times new roman', 20)
    elif screenSizeStore == 2:
        font2 = pygame.font.SysFont('times new roman', 22)
    elif screenSizeStore == 3:
        font2 = pygame.font.SysFont('times new roman', 28)
    else: #screenSizeStore = 4
        font2 = pygame.font.SysFont('times new roman', 40)

    outputScore = font2.render(textScore, True, white)
    outputSkip = font2.render(textSkip, True, white)
    outputAnswer1 = font2.render(textAnswer1, True, white)
    outputAnswer2 = font2.render(textAnswer2, True, white)
    outputQuestion = font2.render(textQuestion, True, white)

def variables(screenWidth, screenHeight):
    global xQ, yQ, widthQ, heightQ, xA_1, yA_1, widthA_1, heightA_1, xA_2, xC, yC, widthC, heightC, xS, size, sizeToBorder
    # Dimensions for tiles (Q= Question; A= Answer; _X= Indicates the number)
    xQ, yQ = 10, (screenHeight/10)  #(screenWidth/20)
    widthQ = int(screenWidth - (2*xQ))
    heightQ = int(1/2 * screenHeight)
    # Count Rect
    xC, yC = (4*screenWidth/10), 5
    widthC = int(screenWidth - (2*xC))
    heightC = int(screenHeight/10 - 15)
    # 2- Answer Design
    xA_1, yA_1 = 10, (heightQ+ (1.25*yQ))   #(screenWidth/20)
    widthA_1 = int((screenWidth/2) - 15)
    heightA_1 = int(screenHeight - heightQ - heightC - 3.5*xQ)
    xA_2 = xQ + widthQ - widthA_1
    # skip- button
    xS = screenWidth - widthC - (2*yC)



'''--------------------StartConsoleLoop--------------------'''
pygame.init()
screen = pygame.display.set_mode((300, 500))
pygame.display.set_caption("Scale mesurement")

running = True
screen.fill((255, 0, 0))

TextSButton = button(white, 0, 0, 300, 90)
answer1SButton = button(white, 0, 100, 300, 90)
answer2SButton = button(white, 0, 200, 300, 90)
answer3SButton = button(white, 0, 300, 300, 90)
answer4SButton = button(white, 0, 400, 300, 90)

textSB = 'Pick a screen resolution:'
textA1 = '480p'
textA2 = 'PyGame Custom Size (800*500)'
textA3 = '720p'
textA4 = '1080p'

textB = pygame.transform.scale(picture_2_1, (300,90))
image1_1 = pygame.transform.scale(picture_1_1, (300,90))
image1_2 = pygame.transform.scale(picture_1_1, (300,90))
image2_1 = pygame.transform.scale(picture_1_1, (300,90))
image2_2 = pygame.transform.scale(picture_1_1, (300,90))

selectedImage = pygame.transform.scale(picture_1_2, (300,90))

font = pygame.font.SysFont('times new roman', 20)

outputSB = font.render(textSB, True, white)
outputA1 = font.render(textA1, True, white)
outputA2 = font.render(textA2, True, white)
outputA3 = font.render(textA3, True, white)
outputA4 = font.render(textA4, True, white)

screenSizeStore = 0

redraw_StartWindow(0)
while running:
    pygame.time.delay(100)

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if TextSButton.is_Over(pos):
                pass
            if answer1SButton.is_Over(pos):
                screenWidth = 640
                screenHeight = 480
                screenSizeStore = 1
                running = False
            if answer2SButton.is_Over(pos):
                screenWidth = 800
                screenHeight = 500
                screenSizeStore = 2
                running = False
            if answer3SButton.is_Over(pos):
                screenWidth = 1280
                screenHeight = 720
                screenSizeStore = 3
                running = False
            if answer4SButton.is_Over(pos):
                screenWidth = 1920
                screenHeight = 1080
                screenSizeStore = 4
                running = False

        if event.type == pygame.MOUSEMOTION:
            if answer1SButton.is_Over(pos):
                redraw_StartWindow(1)
            elif answer2SButton.is_Over(pos):
                redraw_StartWindow(2)
            elif answer3SButton.is_Over(pos):
                redraw_StartWindow(3)
            elif answer4SButton.is_Over(pos):
                redraw_StartWindow(4)
            else:
                redraw_StartWindow(0)

    pygame.display.update()

pygame.quit()



'''--------------------Creating the Window--------------------'''
pygame.init()
win = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Quiz Application")

bg = pygame.transform.scale(picture_background, (screenWidth, screenHeight))

run = True
count = "0"
question, answer1, answer2 = '', '', ''

variables(screenWidth,screenHeight)
find_Question()
buttons()
text(count, answer1, answer2, question)

pic_Score = pygame.transform.scale(picture_2_1, (widthC,heightC))
pic_Skip = pygame.transform.scale(picture_1_1, (widthC,heightC))
pic_Answer1 = pygame.transform.scale(picture_1_1, (widthA_1,heightA_1))
pic_Answer2 = pygame.transform.scale(picture_1_1, (widthA_1,heightA_1))
pic_Question = pygame.transform.scale(picture_2_1, (widthQ,heightQ))

selected1 = pygame.transform.scale(picture_1_2, (widthA_1,heightA_1))
selected2 = pygame.transform.scale(picture_2_2, (widthC,heightC))

'''--------------------Main-Loop--------------------'''
redraw_Window(0)
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if answer1Button.is_Over(pos):
                if direction == 1:
                    rightQuestion(0)
                    question_Finished(0)
                elif direction == 2:
                    rightQuestion(1)
                    question_Finished(1)
            if answer2Button.is_Over(pos):
                if direction == 1:
                    rightQuestion(1)
                    question_Finished(1)
                elif direction == 2:
                    rightQuestion(0)
                    question_Finished(0)

            if skipButton.is_Over(pos):
                find_Question()
                buttons()
                redraw_Window(0)

        if event.type == pygame.MOUSEMOTION:
            if answer1Button.is_Over(pos):
                redraw_Window(1)
            elif answer2Button.is_Over(pos):
                redraw_Window(2)
            elif skipButton.is_Over(pos):
                redraw_Window(3)
            else:
                redraw_Window(0)

    pygame.display.update()

pygame.quit()

Sicherung = input()
