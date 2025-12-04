#Day 12: 30 Days of python programming

import random
import string

def random_user_id():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=6))  
print(random_user_id())

def user_id_gen_by_user():
    num_chars = int(input('Number of characters: '))
    num_ids = int(input('Number of IDs characters: '))
    characters = string.ascii_letters + string.digits
    user_ids = []
    for _ in range(num_ids):  
        user_id = ''
        for _ in range(num_chars):  
            user_id += random.choice(characters)
        user_ids.append(user_id)
    return user_ids
print(user_id_gen_by_user())

def rgb_color_gen():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r, g, b
print(rgb_color_gen())

#Exercises 2
def list_of_hexa_colors(n):
    hex_colors = []
    for _ in range(n):
        hex_color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
        hex_colors.append(hex_color)
    return hex_colors
print(list_of_hexa_colors(1))

def list_of_rgb_colors(n):
    rgb_list = []
    for _ in range(n):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        rgb_list.append(f'{r}, {g}, {b}')
    return rgb_list
print(list_of_rgb_colors(2))

def generate_colors(gen, n):
    if gen == 'hexa':
        return list_of_hexa_colors(n)
    elif gen == 'rgb':
        return list_of_rgb_colors(n)
    else: return ('Error, first parameter should be: "hexa" or "rgb"')
print(generate_colors('hexa',5))

#Exercises 3
def shuffle_list(inp_list):
    random.shuffle(inp_list)
    return inp_list
print(shuffle_list([1,4,5]))

def seven_numbers():
    list_random = []
    while len(list_random) <7:
     x =random.randint(0,9)
     if x not in list_random:
         list_random.append(x)
    return list_random
print(seven_numbers())