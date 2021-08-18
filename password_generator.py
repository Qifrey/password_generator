#!/usr/bin/env python
"""
Created on Mon Aug 16 21:06:25 2021

@author: Thi Vidal
"""

'''
Password generator
'''

import string
import random

    
def new_password(type_pw, how_many_char, name_key):
    '''
    Args:
        type_pw (integer): Types of passwords: 1- only integer numbers, 2- only letters, 3- only simbols, 4- numbers and letters, 5- numbers and simbols, 6- letters and simbols and 7- mixed types.
        how_many_char (integer): select how many chacters.
        name_key (TYPE): a str that is the key of a new password.
        
    Returns:
        new_pw (dic): A dic of a new password.
    '''
    new_pw = {}
    valid_numbers = '0123456789'
    valid_letters = string.ascii_lowercase
    valid_simbols = '!@#$%&*\/><][}{'
    
    # type_pw = 4
    # how_many_char = 18
    # name_key = 'test'
    
    if type_pw == 1:
        list_of_vn = []
        while how_many_char > 0:
            list_of_vn.append(random.randrange(0,10)) #(secrets.randbelow(10)) you can use the secrets module for more safety password.
            how_many_char -= 1
        new_pw[name_key] = list_of_vn
     
    if type_pw == 2:
        list_of_vl = []
        while how_many_char > 0:
            list_of_vl.append(random.choice(valid_letters))
            how_many_char -= 1
        new_pw[name_key] = list_of_vl
    
    if type_pw == 3:
        list_of_vs = []
        while how_many_char > 0:
            list_of_vs.append(random.choice(valid_simbols))
            how_many_char -= 1
        new_pw[name_key] = list_of_vs
        
    if type_pw == 4:
        list_of_vnl = [] 
        while how_many_char > 0:
            list_of_vnl.append(random.choice(valid_letters + valid_numbers))
            how_many_char -= 1
        new_pw[name_key] = list_of_vnl
        
    if type_pw == 5:
        list_of_vns = [] 
        while how_many_char > 0:
            list_of_vns.append(random.choice(valid_numbers + valid_simbols))
            how_many_char -= 1
        new_pw[name_key] = list_of_vns
        
    if type_pw == 6:
        list_of_vls = [] 
        while how_many_char > 0:
            list_of_vls.append(random.choice(valid_letters + valid_simbols))
            how_many_char -= 1
        new_pw[name_key] = list_of_vls
        
    if type_pw == 7:
        list_of_vmt = [] 
        while how_many_char > 0:
            list_of_vmt.append(random.choice(valid_letters + valid_simbols + valid_numbers))
            how_many_char -= 1
        new_pw[name_key] = list_of_vmt
    
    return new_pw

def call_new_password(x):
    '''
    Args:
        x (smt): call the function.
    Returns:
        call the new_password function.
    '''   
    type_pw = 0
    how_many_char = 0
    name_key = ''
    
    while type_pw != 1 and type_pw != 2 and type_pw != 3 and type_pw != 4 and type_pw != 5 and type_pw != 6 and type_pw != 7: #select the type of password
        try:
            print('Types of passwords: 1- only integer numbers, 2- only letters, 3- only simbols, 4- numbers and letters, 5- numbers and simbols, 6- letters and simbols and 7- mixed types.')
            type_pw = int(input('What is the type of your new password? '))
        except ValueError:
            print('Please select an valid option')

    while how_many_char == 0: #select how many chacters
        try:
            how_many_char = int(input('How many characters you need? '))
        except ValueError:
            print('Please select an valid option')
    
    while len(name_key) == 0: #select the name
            name_key = str(input('What is the name of your password? '))
    
    return new_password(type_pw, how_many_char, name_key)

#def list_of_pw(new_password):
    #list_of_pw = []
    #list_of_pw.append(new_password)
    #return list_of_pw

while True:
    start = str(input('Hi, what do you need? n: new password, l: list your saved passwords '))
    if start == 'n':
        print(call_new_password(start))
    