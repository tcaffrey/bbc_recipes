from src.utils import *
import unittest
import pickle
import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in

url_list = ["https://www.bbc.co.uk/food/recipes/warmpotatosaladwithh_88228",
    "https://www.bbc.co.uk/food/recipes/tex-mex_brick_chicken_47381",
    "",
    None,
    "test",
    "https://www.bbc.co.uk/food/recipes/our_special_cassoulet_05208"]

class TestGetBBCRecipes(unittest.TestCase):
    def test_url_request(self):
        
        rel_path = "input_files/expected_parsed_data"
        abs_file_path = os.path.join(script_dir, rel_path)

        with open (abs_file_path, 'rb') as fp:
            expected_parsed_data = pickle.load(fp)
        
        actual_parsed_data = []

        for i in range(0, len(url_list)):
            recipe_url = RecipeBBC(url_list[i])
            recipe_url.url_request()
            actual_parsed_data.append(recipe_url.recipe_json)

        with open ('expected_parsed_data', 'rb') as fp:
            expected_parsed_data = pickle.load(fp)

        self.assertEqual(actual_parsed_data, expected_parsed_data)

    def test_chef_name(self):
        
        expected_chef_name = ['-', '-', '-', '-', '-', 'The Hairy Bikers']
        
        actual_chef_name = []

        for i in range(0, len(url_list)):
            recipe_url = RecipeBBC(url_list[i])
            recipe_url.url_request()
            actual_chef_name.append(recipe_url.chef_name())

        self.assertEqual(expected_chef_name, actual_chef_name)

    def test_recipe_name(self):
        
        expected_recipe_name = ['-', '-', '-', '-', '-', 'Our special cassoulet']

        actual_recipe_name = []

        for i in range(0, len(url_list)):
            recipe_url = RecipeBBC(url_list[i])
            recipe_url.url_request()
            actual_recipe_name.append(recipe_url.recipe_name())

        self.assertEqual(expected_recipe_name, actual_recipe_name)

    def test_recipe_name(self):
        
        expected_recipe_name = ['-', '-', '-', '-', '-', 'Our special cassoulet']

        actual_recipe_name = []

        for i in range(0, len(url_list)):
            recipe_url = RecipeBBC(url_list[i])
            recipe_url.url_request()
            actual_recipe_name.append(recipe_url.recipe_name())

        self.assertEqual(expected_recipe_name, actual_recipe_name)

    def test_unique_value(self):
        
        expected_values = ['-', 'test', None, 'less than 30 mins', 10]

        actual_inputs = [["-"],
                         ["test", "test", "test"],
                         [None, None, None],
                         ["less than 30 mins", "less than 30 mins"],
                         [10, "str", 4.0, 4.0]                         
                        ]

        recipe_url = RecipeBBC("https://www.bbc.co.uk/food/recipes/our_special_cassoulet_05208")
        actual_values = [recipe_url.unique_value(i) for i in actual_inputs]

        self.assertEqual(expected_values, actual_values)


if __name__ == '__main__':
    unittest.main()