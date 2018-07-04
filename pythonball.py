#pythonball.py

import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Pythonball") #pygame

white_balls = list(range(1,69))
red_balls = list(range(1,26))
five_balls = []
one_ball = []
p1_score = 100
white = (255,255,255)
red = (255,0,0)

def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',72)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/5))
    gameDisplay.blit(TextSurf, TextRect) #pygame

message_display("~~PYTHONBALL~~")
#print("~~PYTHONBALL~~")
print("Good evening and welcome to Pythonball.")

print("PLAYER ONE")
pick_one = input("Please pick a number between 1 and 69: ")
pick_two = input("Please pick a number between 1 and 69: ")
pick_three = input("Please pick a number between 1 and 69: ")
pick_four = input("Please pick a number between 1 and 69: ")
pick_five = input("Please pick a number between 1 and 69: ")
pythonball_pick = input("Finally, please pick a Pythonball, a number between 1 and 26: ")
'''print("You have $" + p1_score + ".")

def p1_bet():
	bet = int(input("Place your bet: ")
	p1_score = p1_score - bet

p1_bet'''

counter_w = 0
random.shuffle(white_balls)

while white_balls:
    five_balls.append(white_balls.pop()) 
    counter_w += 1
    if counter_w == 5:
        break

random.shuffle(red_balls)
one_ball.append(red_balls.pop())		

print("RESULTS")
print(five_balls)
print("Pythonball", one_ball)

#PLAYER ONE MATCHES
p1_matches = 1
pythonball_match = False
if pick_one in five_balls:
	print("First pick matched!")
	p1_matches += 1
if pick_one not in five_balls:
	print("First pick not matched.")
if pick_two in five_balls:
	print("Second pick matched!")
	p1_matches += 1
if pick_two not in five_balls:
	print("Second pick not matched.")
if pick_three in five_balls:
	print("Third pick matched!")
	p1_matches += 1
if pick_three not in five_balls:
	print("Third pick not matched.")
if pick_four in five_balls:
	print("Fourth pick matched!")
	p1_matches += 1
if pick_four not in five_balls:
	print("Fourth pick not matched.")
if pick_five in five_balls:
	print("Fifth pick matched!")
	p1_matches += 1
if pick_five not in five_balls:
	print("Fifth pick not matched.")
if pythonball_pick in one_ball:
	print("Pythonball matched!!")
	pythonball_match = True
if pythonball_pick not in one_ball:
	print("Pythonball not matched.")
	print("GAME OVER")
	
#p1_score = bet * p1_matches
if pythonball_match == True:
	p1_score = p1_score * 2

