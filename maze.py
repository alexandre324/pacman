#import everything
import pygame
from tkinter import *
from tkinter import ttk
import time
from multiprocessing import Process
import random

#maze grid
maze = [
    [1,1,1,1,1,0,0,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,1,1,1,1,1,0,3,1],
    [1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,1,1,0,0,1,1],
    [1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1,1,0,1,0,1,0,1,0,0,1,1,1],
    [1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,1,1,0,1,0,0,0,1,1,0,1,1,1],
    [1,0,0,0,1,0,0,1,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,1,1,0,0,0,0,1],
    [1,0,1,1,1,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1],
    [1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,0,1],
    [1,0,0,0,1,0,1,0,0,0,0,1,0,1,0,1,1,0,1,0,1,0,1,0,0,0,1,0,1,1],
    [1,0,1,1,1,0,0,0,1,1,0,1,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,1],
    [1,0,0,0,0,0,1,0,1,0,0,1,1,1,0,1,0,1,1,0,1,1,0,1,1,1,0,1,0,1],
    [1,0,1,0,1,1,1,1,1,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,1,1,1],
    [1,0,0,0,1,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,1,1,1,1,0,1,0,0,0,1],
    [1,1,1,1,1,0,0,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,1,1,1,1,1,0,0,1],
    [1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,1,1,0,0,1,1],
    [1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1,1,0,1,0,1,0,1,0,0,1,1,1],
    [1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,1,1,0,1,0,0,0,1,1,0,1,1,1],
    [1,0,0,0,1,0,0,1,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,1,1,0,0,0,0,1],
    [1,0,1,1,1,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1],
    [1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,0,1],
    [1,0,0,0,1,0,1,0,0,0,0,1,0,1,0,1,1,0,1,0,1,0,1,0,0,0,1,0,1,1],
    [1,0,1,1,1,0,0,0,1,1,0,1,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,1],
    [1,0,0,0,0,0,1,0,1,0,0,1,1,1,0,1,0,1,1,0,1,1,0,1,1,1,0,1,0,1],
    [1,0,1,0,1,1,1,1,1,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,1,1,1],
    [1,2,0,0,1,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,1,1,1,1,0,1,0,0,0,1]
]

#draw all the maze
def draw_the_maze(maze, screen, wall_size):
    #create colors
    black = (18, 17, 17)
    blue = (0, 0, 255)
    red = (255, 0, 0)
    yellow = (255, 255, 0)
    orange = (255, 200, 0)
    really_light_gray = (107, 100, 100)
    white = (33, 32, 32)
    light_gray = (46, 44, 44)

    for i in range(len(maze[0])):
        for o in range(len(maze)):
            if maze[o][i] == 1:
                pygame.draw.rect(screen, black, pygame.Rect(i*wall_size, o*wall_size, wall_size, wall_size))
            elif maze[o][i] == 4:
                pygame.draw.rect(screen, white, pygame.Rect(i*wall_size, o*wall_size, wall_size, wall_size))
            elif maze[o][i] == 5:
                pygame.draw.rect(screen, white, pygame.Rect(i*wall_size, o*wall_size, wall_size, wall_size))
            elif maze[o][i] == 8:
                pygame.draw.rect(screen, white, pygame.Rect(i*wall_size, o*wall_size, wall_size, wall_size))
            elif maze[o][i] == 9:
                pygame.draw.rect(screen, white, pygame.Rect(i*wall_size, o*wall_size, wall_size, wall_size))
            elif maze[o][i] == 0:
                pygame.draw.rect(screen, white, pygame.Rect(i*wall_size, o*wall_size, wall_size, wall_size))
    pygame.display.flip()

# draw the starting and ending flags 
def draw_starting_ending_points(maze, screen, window_width):
    wall_size = window_width // len(maze[0])
    for i in range(len(maze[0])):
        for o in range(len(maze)):
            if maze[o][i] == 2:
                image = pygame.image.load("fantome.png").convert_alpha()
                image_sized = pygame.transform.scale(image,(wall_size-5, wall_size-5))
                screen.blit(image_sized, ((i*wall_size)+2, (o*wall_size)+2))
                starting_point_x, starting_point_y = i, o

            if maze[o][i] == 3:
                image = pygame.image.load("pacman.png").convert_alpha()
                image_sized = pygame.transform.scale(image, (wall_size-7, wall_size-7))
                screen.blit(image_sized, ((i*wall_size)+5, (o*wall_size)+5))

    return starting_point_x, starting_point_y, wall_size

#test if a position is possibe
def can_go_up(actual_y):
    if actual_y == 0:
        return False
    else:
        return True
def can_go_down(actual_y, maze):
    if actual_y == len(maze) - 1:
        return False
    else:
        return True
def can_go_left(actual_x):
    if actual_x == 0:
        return False
    else:
        return True
def can_go_right(actual_x, maze):
    if actual_x == len(maze[0]):
        return False
    else:
        return True

#find the next move if the arrival is on the right and up
def right_up(actual_x, actual_y, maze, come_from):
    if can_go_right(actual_x, maze):
        if maze[actual_y][actual_x + 1] == 0 or maze[actual_y][actual_x + 1] == 2:
            maze[actual_y][actual_x + 1] = 4
            come_from.append("right")
            return actual_x + 1, actual_y, maze, come_from
    if can_go_up(actual_y):
        if maze[actual_y - 1][actual_x] == 0 or maze[actual_y - 1][actual_x] == 2:
            maze[actual_y - 1][actual_x] = 4
            come_from.append("up")
            return actual_x, actual_y - 1, maze, come_from
    if can_go_left(actual_x):
        if maze[actual_y][actual_x - 1] == 0 or maze[actual_y][actual_x - 1] == 2:
            maze[actual_y][actual_x - 1] = 4
            come_from.append("left")
            return actual_x - 1, actual_y, maze, come_from
    if can_go_down(actual_y, maze):
        if maze[actual_y + 1][actual_x] == 0 or maze[actual_y + 1][actual_x] == 2 :
            maze[actual_y + 1][actual_x] = 4
            come_from.append("down")
            return actual_x, actual_y + 1, maze, come_from
        else: 
            actual_x, actual_y, maze, come_from = go_back(actual_x, actual_y, maze, come_from)
            return actual_x, actual_y, maze, come_from
    else:
        actual_x, actual_y, maze, come_from = go_back(actual_x, actual_y, maze, come_from)
        return actual_x, actual_y, maze, come_from

#find the next move if the arrival is on the right and down
def right_down(actual_x, actual_y, maze, come_from):
    if can_go_right(actual_x, maze):
        if maze[actual_y][actual_x + 1] == 0 or maze[actual_y][actual_x + 1] == 2:
            maze[actual_y][actual_x + 1] = 4
            come_from.append("right")
            return actual_x + 1, actual_y, maze, come_from
    if can_go_down(actual_y, maze):
        if maze[actual_y + 1][actual_x] == 0 or maze[actual_y + 1][actual_x] == 2 :
            maze[actual_y + 1][actual_x] = 4
            come_from.append("down")
            return actual_x, actual_y + 1, maze, come_from
    if can_go_up(actual_y):
        if maze[actual_y - 1][actual_x] == 0 or maze[actual_y - 1][actual_x] == 2:
            maze[actual_y - 1][actual_x] = 4
            come_from.append("up")
            return actual_x, actual_y - 1, maze, come_from
    if can_go_left(actual_x):
        if maze[actual_y][actual_x - 1] == 0 or maze[actual_y][actual_x - 1] == 2:
            maze[actual_y][actual_x - 1] = 4
            come_from.append("left")
            return actual_x - 1, actual_y, maze, come_from
        else: 
            actual_x, actual_y, maze, come_from = go_back(actual_x, actual_y, maze, come_from)
            return actual_x, actual_y, maze, come_from
    else:
        actual_x, actual_y, maze, come_from = go_back(actual_x, actual_y, maze, come_from)
        return actual_x, actual_y, maze, come_from

#find the next move if the arrival is on the lefts and up
def left_up(actual_x, actual_y, maze, come_from):
    if can_go_left(actual_x):
        if maze[actual_y][actual_x - 1] == 0 or maze[actual_y][actual_x - 1] == 2:
            maze[actual_y][actual_x - 1] = 4
            come_from.append("left")
            return actual_x - 1, actual_y, maze, come_from
    if can_go_up(actual_y):
        if maze[actual_y - 1][actual_x] == 0 or maze[actual_y - 1][actual_x] == 2:
            maze[actual_y - 1][actual_x] = 4
            come_from.append("up")
            return actual_x, actual_y - 1, maze, come_from
    if can_go_right(actual_x, maze):
        if maze[actual_y][actual_x + 1] == 0 or maze[actual_y][actual_x + 1] == 2:
            maze[actual_y][actual_x + 1] = 4
            come_from.append("right")
            return actual_x + 1, actual_y, maze, come_from
    if can_go_down(actual_y, maze):
        if maze[actual_y + 1][actual_x] == 0 or maze[actual_y + 1][actual_x] == 2 :
            maze[actual_y + 1][actual_x] = 4
            come_from.append("down")
            return actual_x, actual_y + 1, maze, come_from
        else: 
            actual_x, actual_y, maze, come_from = go_back(actual_x, actual_y, maze, come_from)
            return actual_x, actual_y, maze, come_from
    else:
        actual_x, actual_y, maze, come_from = go_back(actual_x, actual_y, maze, come_from)
        return actual_x, actual_y, maze, come_from

#find the next move if the arrival is on the left and down
def left_down(actual_x, actual_y, maze, come_from):
    if can_go_left(actual_x):
        if maze[actual_y][actual_x - 1] == 0 or maze[actual_y][actual_x - 1] == 2 or maze[actual_y][actual_x - 1] == 3:
            maze[actual_y][actual_x - 1] = 4
            come_from.append("left")
            return actual_x - 1, actual_y, maze, come_from
    if can_go_down(actual_y, maze):
        if maze[actual_y + 1][actual_x] == 0 or maze[actual_y + 1][actual_x] == 2 :
            maze[actual_y + 1][actual_x] = 4
            come_from.append("down")
            return actual_x, actual_y + 1, maze, come_from
    if can_go_up(actual_y):
        if maze[actual_y - 1][actual_x] == 0 or maze[actual_y - 1][actual_x] == 2:
            maze[actual_y - 1][actual_x] = 4
            come_from.append("up")
            return actual_x, actual_y - 1, maze, come_from
    if can_go_right(actual_x, maze):
        if maze[actual_y][actual_x + 1] == 0 or maze[actual_y][actual_x + 1] == 2:
            maze[actual_y][actual_x + 1] = 4
            come_from.append("right")
            return actual_x + 1, actual_y, maze, come_from
        else: 
            actual_x, actual_y, maze, come_from = go_back(actual_x, actual_y, maze, come_from)
            return actual_x, actual_y, maze, come_from
    else:
        actual_x, actual_y, maze, come_from = go_back(actual_x, actual_y, maze, come_from)
        return actual_x, actual_y, maze, come_from

#find the next move if the arrival is on the up and left
def up_left(actual_x, actual_y, maze, come_from):
    if can_go_up(actual_y):
        if maze[actual_y - 1][actual_x] == 0 or maze[actual_y - 1][actual_x] == 2 or maze[actual_y - 1][actual_x] == 3:
            maze[actual_y - 1][actual_x] = 4
            come_from.append("up")
            return actual_x, actual_y - 1, maze, come_from
    if can_go_left(actual_x):
        if maze[actual_y][actual_x - 1] == 0 or maze[actual_y][actual_x - 1] == 2 or maze[actual_y][actual_x - 1] == 3: 
            maze[actual_y][actual_x - 1] = 4
            come_from.append("left")
            return actual_x - 1, actual_y, maze, come_from
    if can_go_right(actual_x, maze):
        if maze[actual_y][actual_x + 1] == 0 or maze[actual_y][actual_x + 1] == 2 or maze[actual_y][actual_x + 1] == 3:
            maze[actual_y][actual_x + 1] = 4
            come_from.append("right")
            return actual_x + 1, actual_y, maze, come_from
    if can_go_down(actual_y, maze):
        if maze[actual_y + 1][actual_x] == 0 or maze[actual_y + 1][actual_x] == 2 or maze[actual_y + 1][actual_x] == 3:
            maze[actual_y + 1][actual_x] = 4
            come_from.append("down")
            return actual_x, actual_y + 1, maze, come_from
        else: 
            actual_x, actual_y, maze, come_from = go_back(actual_x, actual_y, maze, come_from)
            return actual_x, actual_y, maze, come_from
    else:
        actual_x, actual_y, maze, come_from = go_back(actual_x, actual_y, maze, come_from)
        return actual_x, actual_y, maze, come_from

#find the next move if the arrival is on the up and right
def up_right(actual_x, actual_y, maze, come_from):
    if can_go_up(actual_y):
        if maze[actual_y - 1][actual_x] == 0 or maze[actual_y - 1][actual_x] == 2 or maze[actual_y - 1][actual_x] == 3:
            maze[actual_y - 1][actual_x] = 4
            come_from.append("up")
            return actual_x, actual_y - 1, maze, come_from
    if can_go_right(actual_x, maze):
        if maze[actual_y][actual_x + 1] == 0 or maze[actual_y][actual_x + 1] == 2 or maze[actual_y][actual_x + 1] == 3:
            maze[actual_y][actual_x + 1] = 4
            come_from.append("right")
            return actual_x + 1, actual_y, maze, come_from
    if can_go_left(actual_x):
        if maze[actual_y][actual_x - 1] == 0 or maze[actual_y][actual_x - 1] == 2 or maze[actual_y][actual_x - 1] == 3:
            maze[actual_y][actual_x - 1] = 4
            come_from.append("left")
            return actual_x - 1, actual_y, maze, come_from
    if can_go_down(actual_y, maze):
        if maze[actual_y + 1][actual_x] == 0 or maze[actual_y + 1][actual_x] == 2 or maze[actual_y + 1][actual_x] == 3 :
            maze[actual_y + 1][actual_x] = 4
            come_from.append("down")
            return actual_x, actual_y + 1, maze, come_from
        else: 
            actual_x, actual_y, maze, come_from = go_back(actual_x, actual_y, maze, come_from)
            return actual_x, actual_y, maze, come_from
    else:
        actual_x, actual_y, maze, come_from = go_back(actual_x, actual_y, maze, come_from)
        return actual_x, actual_y, maze, come_from

#find the next move if the arrival is on the down and left
def down_left(actual_x, actual_y, maze, come_from):
    if can_go_down(actual_y, maze):
        if maze[actual_y + 1][actual_x] == 0 or maze[actual_y + 1][actual_x] == 2 or maze[actual_y + 1][actual_x] == 3 :
            maze[actual_y + 1][actual_x] = 4
            come_from.append("down")
            return actual_x, actual_y + 1, maze, come_from
    if can_go_left(actual_x):
        if maze[actual_y][actual_x - 1] == 0 or maze[actual_y][actual_x - 1] == 2 or maze[actual_y][actual_x - 1] == 3:
            maze[actual_y][actual_x - 1] = 4
            come_from.append("left")
            return actual_x - 1, actual_y, maze, come_from
    if can_go_right(actual_x, maze):
        if maze[actual_y][actual_x + 1] == 0 or maze[actual_y][actual_x + 1] == 2 or maze[actual_y][actual_x + 1] == 3:
            maze[actual_y][actual_x + 1] = 4
            come_from.append("right")
            return actual_x + 1, actual_y, maze, come_from
    if can_go_up(actual_y):
        if maze[actual_y - 1][actual_x] == 0 or maze[actual_y - 1][actual_x] == 2 or maze[actual_y - 1][actual_x] == 3:
            maze[actual_y - 1][actual_x] = 4
            come_from.append("up")
            return actual_x, actual_y - 1, maze, come_from
        else: 
            actual_x, actual_y, maze, come_from = go_back(actual_x, actual_y, maze, come_from)
            return actual_x, actual_y, maze, come_from
    else:
        actual_x, actual_y, maze, come_from = go_back(actual_x, actual_y, maze, come_from)
        return actual_x, actual_y, maze, come_from

#find the next move if the arrival is on the down and right
def down_right(actual_x, actual_y, maze, come_from):
    if can_go_down(actual_y, maze):
        if maze[actual_y + 1][actual_x] == 0 or maze[actual_y + 1][actual_x] == 2 or maze[actual_y + 1][actual_x] == 3:
            maze[actual_y + 1][actual_x] = 4
            come_from.append("down")
            return actual_x, actual_y + 1, maze, come_from
    if can_go_right(actual_x, maze):
        if maze[actual_y][actual_x + 1] == 0 or maze[actual_y][actual_x + 1] == 2 or maze[actual_y][actual_x + 1] == 3:
            maze[actual_y][actual_x + 1] = 4
            come_from.append("right")
            return actual_x + 1, actual_y, maze, come_from
    if can_go_up(actual_y):
        if maze[actual_y - 1][actual_x] == 0 or maze[actual_y - 1][actual_x] == 2 or maze[actual_y - 1][actual_x] == 3:
            maze[actual_y - 1][actual_x] = 4
            come_from.append("up")
            return actual_x, actual_y - 1, maze, come_from
    if can_go_left(actual_x):
        if maze[actual_y][actual_x - 1] == 0 or maze[actual_y][actual_x - 1] == 2 or maze[actual_y][actual_x - 1] == 3:
            maze[actual_y][actual_x - 1] = 4
            come_from.append("left")
            return actual_x - 1, actual_y, maze, come_from
        else: 
            actual_x, actual_y, maze, come_from = go_back(actual_x, actual_y, maze, come_from)
            return actual_x, actual_y, maze, come_from
    else:
        actual_x, actual_y, maze, come_from = go_back(actual_x, actual_y, maze, come_from)
        return actual_x, actual_y, maze, come_from


#find the next move
def find_next_step(actual_x, actual_y, maze, come_from, priority):
    if priority[0] == "right" and priority[1] == "up":
        actual_x, actual_y, maze, come_from = right_up(actual_x, actual_y, maze, come_from)
    elif priority[0] == "right" and priority[1] == "down":
        actual_x, actual_y, maze, come_from = right_down(actual_x, actual_y, maze, come_from)
    elif priority[0] == "left" and priority[1] == "up":
        actual_x, actual_y, maze, come_from = left_up(actual_x, actual_y, maze, come_from)
    elif priority[0] == "left" and priority[1] == "down":
        actual_x, actual_y, maze, come_from = left_down(actual_x, actual_y, maze, come_from)
    elif priority[0] == "up" and priority[1] == "left":
        actual_x, actual_y, maze, come_from = up_left(actual_x, actual_y, maze, come_from)
    elif priority[0] == "up" and priority[1] == "right":
        actual_x, actual_y, maze, come_from = up_right(actual_x, actual_y, maze, come_from)
    elif priority[0] == "down" and priority[1] == "left":
        actual_x, actual_y, maze, come_from = down_left(actual_x, actual_y, maze, come_from)
    elif priority[0] == "down" and priority[1] == "right":
        actual_x, actual_y, maze, come_from = down_right(actual_x, actual_y, maze, come_from)
    return actual_x, actual_y, maze, come_from

#move the fantom
def move_fantom(fantom_x, fantom_y, wall_size, screen, maze):
    maze[fantom_y][fantom_x] = 0
    image = pygame.image.load("fantome.png").convert_alpha()
    image_sized = pygame.transform.scale(image,(wall_size-3, wall_size-3))
    if can_go_down(fantom_y, maze):
        if maze[fantom_y + 1][fantom_x] == 4 or maze[fantom_y + 1][fantom_x] == 3:
            maze[fantom_y + 1][fantom_x] = 8
            for i in range(4):  
                pygame.draw.rect(screen, (32, 32, 32), pygame.Rect(fantom_x*wall_size, fantom_y*wall_size, wall_size, wall_size))   
                screen.blit(image_sized, ((fantom_x*wall_size), (fantom_y* wall_size-1)+i))
                pygame.display.flip()
            return fantom_x, fantom_y + 1, maze
    if can_go_up(fantom_y):
        if maze[fantom_y - 1][fantom_x] == 4 or maze[fantom_y - 1][fantom_x] == 3:
            maze[fantom_y - 1][fantom_x] = 8
            for i in range(4):     
                pygame.draw.rect(screen, (32, 32, 32), pygame.Rect(fantom_x*wall_size, fantom_y*wall_size, wall_size, wall_size))
                screen.blit(image_sized, ((fantom_x*wall_size), (fantom_y* wall_size+1)-i))
                pygame.display.flip()
            return fantom_x, fantom_y - 1, maze
    if can_go_left(fantom_x):
        if maze[fantom_y][fantom_x - 1] == 4 or maze[fantom_y][fantom_x - 1] == 3:
            maze[fantom_y][fantom_x - 1] = 8
            pygame.draw.rect(screen, (32, 32, 32), pygame.Rect(fantom_x*wall_size, fantom_y*wall_size, wall_size, wall_size))
            for i in range(4):     
                pygame.draw.rect(screen, (32, 32, 32), pygame.Rect(fantom_x*wall_size, fantom_y*wall_size, wall_size, wall_size))
                screen.blit(image_sized, ((fantom_x*wall_size-1)-i, (fantom_y* wall_size)))
                pygame.display.flip()
            return fantom_x - 1, fantom_y, maze
    if can_go_right(fantom_x, maze):
        if maze[fantom_y][fantom_x + 1] == 4 or maze[fantom_y][fantom_x + 1] == 3:
            maze[fantom_y][fantom_x + 1] = 8
            for i in range(4):     
                pygame.draw.rect(screen, (32, 32, 32), pygame.Rect(fantom_x*wall_size, fantom_y*wall_size, wall_size, wall_size))
                screen.blit(image_sized, ((fantom_x*wall_size+1)+i, (fantom_y* wall_size)))
                pygame.display.flip()
            return fantom_x + 1, fantom_y, maze

#move the pacman
def move_pacman(direction, pacman_x, pacman_y, wall_size, screen, maze, fantom_x, fantom_y):
    image2 = pygame.image.load("pacman.png").convert_alpha()
    image_sized2 = pygame.transform.scale(image2,(wall_size-3, wall_size-3))
    if direction == "down" and can_go_down(pacman_y, maze):
        if maze[pacman_y + 1][pacman_x] != 1:
            pygame.draw.rect(screen, (32, 32, 32), pygame.Rect(pacman_x*wall_size, pacman_y*wall_size, wall_size, wall_size))
            pacman_y += 1
            for i in range(4):  
                pygame.draw.rect(screen, (32, 32, 32), pygame.Rect(pacman_x*wall_size, pacman_y*wall_size, wall_size, wall_size))   
                screen.blit(image_sized2, ((pacman_x*wall_size), (pacman_y* wall_size-1)+i))
                pygame.display.flip()
            screen.blit(image_sized2, ((pacman_x*wall_size), (pacman_y* wall_size)))
            pygame.display.flip()
            maze = find_fantom_way(maze, fantom_x, fantom_y, pacman_x, pacman_y)
            return pacman_x, pacman_y, maze
        else:
            screen.blit(image_sized2, ((pacman_x*wall_size), (pacman_y* wall_size)))
            pygame.display.flip()
            return pacman_x, pacman_y, maze
    elif direction == "up" and can_go_up(pacman_y):
        if maze[pacman_y - 1][pacman_x] != 1 :
            pygame.draw.rect(screen, (32, 32, 32), pygame.Rect(pacman_x*wall_size, pacman_y*wall_size, wall_size, wall_size))
            pacman_y -= 1
            for i in range(4):     
                pygame.draw.rect(screen, (32, 32, 32), pygame.Rect(pacman_x*wall_size, pacman_y*wall_size, wall_size, wall_size))
                screen.blit(image_sized2, ((pacman_x*wall_size), (pacman_y* wall_size+1)-i))
                pygame.display.flip()
            screen.blit(image_sized2, ((pacman_x*wall_size), (pacman_y* wall_size)))
            pygame.display.flip()
            maze = find_fantom_way(maze, fantom_x, fantom_y, pacman_x, pacman_y)
            return pacman_x, pacman_y, maze
        else:
            screen.blit(image_sized2, ((pacman_x*wall_size), (pacman_y* wall_size)))
            pygame.display.flip()
            return pacman_x, pacman_y, maze
    elif direction == "left" and can_go_left(pacman_x):
        if maze[pacman_y][pacman_x - 1] != 1:
            pygame.draw.rect(screen, (32, 32, 32), pygame.Rect(pacman_x*wall_size, pacman_y*wall_size, wall_size, wall_size))
            pacman_x -= 1
            pygame.draw.rect(screen, (32, 32, 32), pygame.Rect(pacman_x*wall_size, pacman_y*wall_size, wall_size, wall_size))
            for i in range(4):     
                pygame.draw.rect(screen, (32, 32, 32), pygame.Rect(pacman_x*wall_size, pacman_y*wall_size, wall_size, wall_size))
                screen.blit(image_sized2, ((pacman_x*wall_size-1)-i, (pacman_y* wall_size)))
                pygame.display.flip()
            screen.blit(image_sized2, ((pacman_x*wall_size), (pacman_y* wall_size)))
            pygame.display.flip()
            maze = find_fantom_way(maze, fantom_x, fantom_y, pacman_x, pacman_y)
            return pacman_x, pacman_y, maze
        else:
            screen.blit(image_sized2, ((pacman_x*wall_size), (pacman_y* wall_size)))
            pygame.display.flip()
            return pacman_x, pacman_y, maze
    elif direction == "right" and can_go_right(pacman_x, maze):
        if maze[pacman_y][pacman_x + 1] != 1 :
            pygame.draw.rect(screen, (32, 32, 32), pygame.Rect(pacman_x*wall_size, pacman_y*wall_size, wall_size, wall_size))
            pacman_x += 1
            for i in range(4):     
                pygame.draw.rect(screen, (32, 32, 32), pygame.Rect(pacman_x*wall_size, pacman_y*wall_size, wall_size, wall_size))
                screen.blit(image_sized2, ((pacman_x*wall_size+1)+i, (pacman_y* wall_size)))
                pygame.display.flip()
            screen.blit(image_sized2, ((pacman_x*wall_size), (pacman_y* wall_size)))
            pygame.display.flip()
            maze = find_fantom_way(maze, fantom_x, fantom_y, pacman_x, pacman_y)
            return pacman_x, pacman_y, maze
        else:
            screen.blit(image_sized2, ((pacman_x*wall_size), (pacman_y* wall_size)))
            pygame.display.flip()
            return pacman_x, pacman_y, maze
    else:
        screen.blit(image_sized2, ((pacman_x*wall_size), (pacman_y* wall_size)))
        pygame.display.flip()
        return pacman_x, pacman_y, maze

#go back when ever i can't go forward
def go_back(actual_x, actual_y, maze, come_from):
    if len(come_from) == 0:
        return actual_x, actual_y, maze, come_from
    else:
        maze[actual_y][actual_x] = 5
        if come_from[-1] == 'left':
            come_from.pop(-1)
            return actual_x + 1, actual_y, maze, come_from
        elif come_from[-1] == 'right':
            come_from.pop(-1)
            return actual_x - 1, actual_y, maze, come_from
        elif come_from[-1] == 'down':
            come_from.pop(-1)
            return actual_x, actual_y - 1, maze, come_from
        elif come_from[-1] == 'up':
            come_from.pop(-1)
            return actual_x, actual_y + 1, maze, come_from
        else:
            return actual_x, actual_y, maze, come_from
    
#test if the arrival flag is found
def flag_found(actual_x, actual_y, pacman_x, pacman_y):
    if actual_x == pacman_x and actual_y == pacman_y:
            return True
    else:
        return False

#find the position of the arrival flag
def find_arrival(maze):
    for i in range(len(maze[0])):
        for o in range(len(maze)):
            if maze[o][i] == 3:
                return i, o

#find the most oficient position to try
def test_priority(arrival_x, arrival_y, actual_x, actual_y):
    priority = []

    difference_x = arrival_x - actual_x
    difference_y = arrival_y - actual_y
    if difference_x < difference_y:
        if difference_x >= 0:
            priority.append("right")
        else:
            priority.append("left")
        if difference_y >= 0:
            priority.append("down")
        else: 
            priority.append("up")
    else:
        if difference_y >= 0:
            priority.append("down")
        else: 
            priority.append("up")
        if difference_x >= 0:
            priority.append("right")
        else:
            priority.append("left")

    
    return priority

#clear the maze
def clear_the_maze(maze):
    for y in range(len(maze)):
        for x in  range(len(maze[0])):
            if maze[y][x] == 4 or maze[y][x] == 5:
                maze[y][x] = 0
            if maze[y][x] == 4 or maze[y][x] == 5:
                maze[y][x] = 0
    return maze

def test_next_direction(maze, pacman_x, pacman_y, next_direction, direction):
    if next_direction == "left":
        if maze[pacman_y][pacman_x - 1] != 1:
            return "left", "none"
        else:
            return direction, next_direction
    elif next_direction == "right":
        if maze[pacman_y][pacman_x + 1] != 1:
            return "rights", "none"
        else:
            return direction, next_direction
    elif next_direction == "up":
        if maze[pacman_y + 1][pacman_x] != 1:
            return "up", "none"
        else:
            return direction, "none"
    elif next_direction == "down":
        if maze[pacman_y - 1][pacman_x] != 1:
            return "down", "none"
        else:
            return direction, next_direction
    else:
        return direction, next_direction

def print_maze(maze):
    print(maze)
    for i in range(len(maze[0])):
        for o in range(len(maze)):
            print(maze[o])
        print()

def find_fantom_way(maze, fantom_x, fantom_y, pacman_x, pacman_y):
    come_from = []
    maze = clear_the_maze(maze)
    priority = test_priority(pacman_x, pacman_y, fantom_x, fantom_y)
    actual_x, actual_y, maze, come_from = find_next_step(fantom_x, fantom_y, maze, come_from, priority)
    while True:
        if flag_found(actual_x, actual_y, pacman_x, pacman_y):
            return maze
        else: 
            priority = test_priority(pacman_x, pacman_y, actual_x, actual_y)
            actual_x, actual_y, maze, come_from = find_next_step(actual_x, actual_y, maze, come_from, priority)
#main code
def main(maze):
    #create colors
    white = (33, 32, 32)

    #get the size of the window we create 
    root = Tk()
    width = root.winfo_screenwidth()
    root.destroy()
    window_width = int(40/100*width)
    window_height = window_width * len(maze) / len(maze[0])
    
    #create the window 
    
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption('pacman')
    screen.fill(white)
    pygame.display.flip()

    #set position for the searching
    come_from = []
    fantom_x, fantom_y, wall_size = draw_starting_ending_points(maze, screen, window_width)
    pacman_x, pacman_y = find_arrival(maze)
    priority = test_priority(pacman_x, pacman_y, fantom_x, fantom_y)
    actual_x, actual_y, maze, come_from = find_next_step(fantom_x, fantom_y + 1, maze, come_from, priority)
    maze = find_fantom_way(maze, fantom_x, fantom_y, pacman_x, pacman_y)
    rushing = True
    direction = 'none'
    next_direction = "none"
    while rushing:        
        
        direction, next_direction = test_next_direction(maze, pacman_x, pacman_y, next_direction, direction)
        if fantom_x == pacman_x and fantom_y == pacman_y:
            print("FOUND YOU !!!")
            rushing = False
            running = False

        else: 
            draw_the_maze(maze, screen, wall_size)
            fantom_x, fantom_y, maze = move_fantom(fantom_x, fantom_y, wall_size, screen, maze)
            pacman_x, pacman_y, maze = move_pacman(direction, pacman_x, pacman_y, wall_size, screen, maze, fantom_x, fantom_y)
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    next_direction = "none"
                    if pygame.key.name(event.key) == "left":
                        if maze[pacman_y][pacman_x - 1] != 1:
                            direction = "left"
                        elif next_direction == "none":
                            next_direction = "left"
                    elif pygame.key.name(event.key) == "right":
                        if maze[pacman_y][pacman_x + 1] != 1:
                            direction = "right"
                        elif next_direction == "none":
                            next_direction = "right"
                    elif pygame.key.name(event.key) == "down":
                        if maze[pacman_y+1][pacman_x] != 1:
                            direction = "down"
                        elif next_direction == "none":
                            next_direction = "down"
                    elif pygame.key.name(event.key) == "up":
                        if maze[pacman_y-1][pacman_x] != 1:
                            direction = "up"
                        elif next_direction == "none":
                            next_direction = "up"
                        
                elif event.type == pygame.QUIT:
                    running = False
                    rushing = False   
        time.sleep(0.1) 
main(maze)