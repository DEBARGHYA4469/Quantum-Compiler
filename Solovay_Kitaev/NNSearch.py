# ...................................NEAREST NEIGHBOUR SEARCH FOR KD-TREE---------------------------------------------------

import pickle 
import math,cmath 
import numpy as np 
import kdtree 
from random import randint 
import dill as pickle # dill is important for dumping lambda functions....

pin = open("kdtree.pickle","rb") 
pin = pickle.load(pin) # pickle_in

def matrix_unroll(Gate):
	r1 = Gate[0][0].real
	c1 = Gate[0][0].imag
	r2 = Gate[0][1].real
	c2 = Gate[0][1].imag	
	return [r1,c1,r2,c2]

def basic_approx(U,e0):
	unroll = matrix_unroll(U) 
	R=pin.search_nn(unroll)
	coords = R[0].__dict__['data'].__dict__['coords']
	R_sequence = R[0].__dict__['data'].__dict__['payload']
	return R_sequence 
	

