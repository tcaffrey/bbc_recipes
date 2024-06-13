import pandas as pd
#This will not run on online IDE 
import requests 
from bs4 import BeautifulSoup 
import random
import time
import os
import json

class RecipeBBC():
    
    def __init__(self, url):
        self.url = url
    
    def url_request(self):
        try:
            r = requests.get(self.url) 
            self.parsed_data = BeautifulSoup(r.content, "html.parser")
            recipe_items = self.parsed_data.select_one('script[type="application/ld+json"]').text
            self.recipe_json = json.loads(recipe_items)
        except:
            self.parsed_data = []
            self.recipe_json = {}
      
    def chef_name(self):
        try:
            return self.recipe_json['author']['name']
        except:
            return '-'
    
    def recipe_name(self):
        try:
            return self.recipe_json['name']
        except:
            return '-'

    def return_tags(self, html_type, html_class):
        try:
            tagList = []
            tags = self.parsed_data.find_all(html_type, class_=html_class)
            for tag in tags:
                tagList.append(tag.text)
            return tagList
        except:
            return []
    
    def programme_name(self):
        html_type, html_class = ['div', 'chef__programme-name']
        programme_name = self.return_tags(html_type, html_class)
        try:
            unique_name = list(set(programme_name))[0]
            if 'From ' in unique_name:
                unique_name = unique_name.replace('From ', '')
        except:
            unique_name = "-"
        return unique_name
        
    def prep_time(self):
        html_type, html_class = ['p', 'recipe-metadata__prep-time']
        prepTime = self.return_tags(html_type, html_class)
        
        try:
            return unique_value(prepTime)
        except:
            return "-"
    
    def cook_time(self):
        html_type, html_class = ['p', 'recipe-metadata__cook-time']
        cookTime = self.return_tags(html_type, html_class)
        try:
            return unique_value(cookTime)
        except:
            return "-"
    
    def serving(self):
        try:
            return self.recipe_json['recipeYield']
        except:
            return "-"
    
    def recipe_description(self):
        try:
            return self.recipe_json['description']
        except:
            return "-"
    
    def list_ingredients(self):
        html_type, html_class = ['a', 'recipe-ingredients__link']
        ingredients_list = self.return_tags(html_type, html_class)
        try:
            return list(dict.fromkeys(ingredients_list))
        except:
            return "-"
    
    def list_ingredients_amounts(self):
        html_type, html_class = ['li', 'recipe-ingredients__list-item']
        ingredients_list = self.return_tags(html_type, html_class)
        try:
            return list(dict.fromkeys(ingredients_list))
        except:
            return "-"
    
    def recipe_instructions(self):
        try:
            return self.recipe_json['recipeInstructions']
        except:
            return "-"
    
    def rating_count(self):
        try:
            return self.recipe_json['aggregateRating']['ratingCount']
        except:
            return "-"
    
    def rating(self):
        try:
            return round(self.recipe_json['aggregateRating']['ratingValue'], 2)
        except:
            return "-"
    
    def recipe_category(self):
        try:
            return self.recipe_json['recipeCategory']
        except:
            return "-"
        
    def recipe_keywords(self):
        try:
            return self.recipe_json['keywords']
        except:
            return "-"
        
    def recipe_diets(self):
        try:
            return self.recipe_json['suitableForDiet']
        except:
            return "-"
        
def unique_value(duplicate_list):
    try:
        return list(dict.fromkeys(duplicate_list))[0]
    except:
        return "-"