#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Define function to find word counter
def word_counter(x):
    return len(tweet.split())
#Define function to find average number 
def average_num(x):
    average = round(sum(len(i) for i in tweet.split())/len(tweet.split()),2)
    return average
#Define function to find upper case
def upper_case(x):
    upper = 0
    for i in tweet: 
        if i.isupper(): #check if i is an upper case letter
            upper = upper + 1                  
    return upper
#Define function to find lower case    
def lower_case(x):
    lower = 0
    for i in tweet: 
         if i.islower(): #check if i is an lower case letter
            lower = lower + 1
    return lower                 
#Define function to reverse the string
def reverse(x): 
  return x[::-1]
#Define function to find string stats
def string_stats(x): 
    alphabet, digit, special = 0, 0, 0
    for i in range(len(x)): 
        if x[i].isalpha(): #check if i is an alphabet
            alphabet += 1
        elif x[i].isdigit(): #check if i is a digit
            digit += 1
        elif x[i] != ' ': #check if i is a special char but not white space
            special += 1
    print("Number of alphabets:", alphabet) 
    print("Number of digits:", digit) 
    print("Number of special characters:", special) 

#Ask for input   
tweet = input("What would you like to tweet?: ")
#Display outputs
print("Number of words:", word_counter(tweet))
print("Average number of characters:", average_num(tweet))
print("Number of upper case letters:", upper_case(tweet))
print("Number of lower case letters:", lower_case(tweet))  
print("Your tweet reversed:\n", reverse(tweet))
string_stats(tweet) 
