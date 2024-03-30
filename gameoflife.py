import pygame
from random import random
import time

screen_width = 1400
screen_height = 700
life_size = 6
start_rate = 0.6
delay = 0.1
color = False

def main():
	pygame.init()
	checkBounds()
	window = pygame.display.set_mode((screen_width, screen_height))
	pygame.display.set_caption("Game of Life")
	play(window)

def play(win):
	table = [[[(int)(random()>start_rate) for i in range(screen_width//life_size)] for j in range(screen_height//life_size)] for k in range(2)]
	flag = 0
	run = True
	while(run):
		if not color:
			win.fill("black")
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False;

		for i in range(len(table[0])):
			for j in range(len(table[0][0])):
				numNeighbors = 0
				for h in [-1, 0, 1]:
					for k in [-1, 0, 1]:
						if not (h == 0 and k == 0) and isValid(i+h, j+k, table, flag):
							numNeighbors += 1

				if (numNeighbors == 2 and isAlive(i, j, table, flag)) or numNeighbors == 3:
					table[flag][i][j] = 1
					if color:
						r1 = int(random() * 256)
						r2 = int(random() * 256)
						r3 = int(random() * 256)
					else:
						r1 = r2 = r3 = 255
					pygame.draw.rect(win, pygame.Color(r1, r2, r3), pygame.Rect(life_size*j, life_size*i, life_size, life_size), 0)
				else:
					table[flag][i][j] = 0

		flag = abs(flag-1)
		pygame.display.update()
		time.sleep(delay/50)
	pygame.quit()

def isValid(x, y, table, flag):
	return x >= 0 and x < len(table[0]) and y >= 0 and y < len(table[0][0]) and isAlive(x, y, table, flag)

def isAlive(x, y, table, flag):
	return table[abs(flag-1)][x][y] == 1

def checkBounds():
	global screen_width, screen_height, life_size
	if screen_width > 1400: 
		screen_width = 1400
	elif screen_width < 400: 
		screen_width = 400
	if screen_height > 700: 
		screen_height = 700
	elif screen_height < 400: 
		screen_height = 400
	if life_size < 2:
		life_size = 2
	elif life_size > min(screen_height/10, screen_width)/10:
		life_size = min(screen_height//10, screen_width)//10
	screen_width -= screen_width%life_size
	screen_height -= screen_height%life_size

if __name__ == "__main__":
    main()
