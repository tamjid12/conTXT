# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 12:05:21 2023

@author: Charlotte

<categories> is a list that contains strings which represent article types 
which can be selected by the user.

To view the currently existing categories at any time, pass function cats(),
which will print an indexed list.

The suggest_urls() function takes up to one argument, which specifies the 
category of resource the user wants to scan for. If no argument is passed, 
the default category is "Scholarly Articles."

Categories can be added by user by passing the add_cat() function and 
following the prompts.
"""

#default categories
#will probably change to a dict later so i can add keys
#multiple categories?
categories = ["scholarly articles for ", 
              "definition of ", 
              "news about ", 
              "image of ", 
              "video of "]

def cats():
    for number, letter in enumerate(categories):
        print(number, letter)
    
def add_cat():
    newcat = input("Enter new category here: ")
    if newcat not in categories:
        categories.append(newcat + " ")
        print("\'" + newcat + "\'" + " has been added as a category!")
    else:
        print(newcat + " is already exists as a category.")


def suggest_urls(cat: int = 0): # use cat to choose mode  
    # 0 <= cat < len(categories)   
    if cat >= len(categories):
        return("Please enter a new category")
    else:
        # Get the user's input
        search_terms = input("Enter notes here: ")
        # Split the input into a list of words
        search_list = search_terms.split()
        # Take the last 5 words of the list
        recent_search = search_list[-5:]
        # Join the last 5 words back into a string
        recent_search = " ".join(recent_search)
        
        
        try:
            from googlesearch import search
        except ImportError:
             print("No module named 'google' found") 
        # to search
        query = categories[cat] + recent_search
        for j in search(query, tld="co.in", num=1, stop=1, pause=2):
            print(j)
    
            suggest_urls(cat)