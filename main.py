import os
import random
import numpy
import cv2
from PIL import Image,ImageDraw,ImageFont
import torch
from torch.utils.data import Dataset
import torchvision.transforms as transforms
import torch.nn as nn
import torch.optim as optim
from torch.nn.utils.rnn import pad_sequence
from torchvision.utils import save_image
from IPython.display import clear_output,display,html
import matplot.pyplot as plt
import base64

#we create a directiory
os.makedirs('training_dataset',exist_ok=True)

#we define the number of videos to genrate for the dateset
num_videos = 1000

#we define the number of frames per video
frames_per_video = 10

#we define the size of eaxh image in the dataset
image_size = (64,64)

#define the size of the shape
shape_size=10

#we define text prompts and corresponding movements for circles
prompts_and_movements = [("circle moving down", "circle", "down"),  # Move circle downward
("circle moving left", "circle", "left"),  # Move circle leftward
("circle moving right", "circle", "right"),  # Move circle rightward
("circle moving diagonally up-right", "circle", "diagonal_up_right"),  # Move circle diagonally up-right
("circle moving diagonally down-left", "circle", "diagonal_down_left"),  # Move circle diagonally down-left
("circle moving diagonally up-left", "circle", "diagonal_up_left"),  # Move circle diagonally up-left
("circle moving diagonally down-right", "circle", "diagonal_down_right"),  # Move circle diagonally down-right
("circle rotating clockwise", "circle", "rotate_clockwise"),  # Rotate circle clockwise
("circle rotating counter-clockwise", "circle", "rotate_counter_clockwise"),  # Rotate circle counter-clockwise
("circle shrinking", "circle", "shrink"),  # Shrink circle
("circle expanding", "circle", "expand"),  # Expand circle
("circle bouncing vertically", "circle", "bounce_vertical"),  # Bounce circle vertically
("circle bouncing horizontally", "circle", "bounce_horizontal"),  # Bounce circle horizontally
("circle zigzagging vertically", "circle", "zigzag_vertical"),  # Zigzag circle vertically
("circle zigzagging horizontally", "circle", "zigzag_horizontal"),  # Zigzag circle horizontally
("circle moving up-left", "circle", "up_left"),  # Move circle up-left
("circle moving down-right", "circle", "down_right"),  # Move circle down-right
("circle moving down-left", "circle", "down_left"),  # Move circle down-left
                        ]
#define function with parameters
def create_image_with_moving_shape(size,frame_num,shape,direction):
  #create a new RGB image with the specified size and  white backgeound
  img=Image.new('RGB',size,color=(255,255,255))

#creaet a drawing object
  draw=ImageDraw.Draw(img) 
#