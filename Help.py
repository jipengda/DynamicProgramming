from docplex.mp.model import Model
import numpy as np
import math
import matplotlib.pyplot as plt

depot = 1
A = 4
N = 10

C = 20
lamda = 0.1164
garma = 0.0173
r_to_degree = 180/(math.pi)
grama_new = garma*(r_to_degree)
lamda = round(lamda, 1)
garma_new = round(garma_new, 1)
