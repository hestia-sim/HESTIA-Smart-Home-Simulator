import json
import sys

import simpy
import os

from data_generator import generate_data
from data_transformer import transform
from join_routines import routines_join
from menu import menu

stop = False
while not stop:
    options = ['Data generator', 'Routines join', 'Data transformer', 'Exit']
    max_size = max(len(option) for option in options)
    title = '*' * (max_size // 2) + ' MAIN MENU ' + '*' * (max_size // 2)
    option = menu(options, title)
    back = False
    if option == 0:
        while not back:
            back = generate_data()
    elif option == 1:
        while not back:
            back = routines_join()
    elif option == 2:
        while not back:
            back = transform()
    else:
        stop = True



