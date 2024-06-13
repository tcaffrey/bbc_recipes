from src.bbc_recipes.utils import *
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

        # recipe_url = RecipeBBC("https://www.bbc.co.uk/food/recipes/our_special_cassoulet_05208")
        actual_values = [unique_value(i) for i in actual_inputs]

        self.assertEqual(expected_values, actual_values)

    def test_return_tags(self):

        expected_tags = [[], [], [], [], [], ['From Hairy Dieters: How to Love Food and Lose Weight']]
        actual_tags = []
        html_type, html_class = ['div', 'chef__programme-name']

        for i in range(0, len(url_list)):
            recipe_url = RecipeBBC(url_list[i])
            recipe_url.url_request()
            actual_tags.append(recipe_url.return_tags(html_type, html_class))

        self.assertEqual(expected_tags, actual_tags)


    def test_programme_name(self):
        
        expected_programme_name = ['-', '-', '-', '-', '-', 'Hairy Dieters: How to Love Food and Lose Weight']

        actual_programme_name = []

        for i in range(0, len(url_list)):
            recipe_url = RecipeBBC(url_list[i])
            recipe_url.url_request()
            actual_programme_name.append(recipe_url.programme_name())

        self.assertEqual(expected_programme_name, actual_programme_name)

    def test_prep_time(self):

        expected_prep_time = ['-', '-', '-', '-', '-', 'less than 30 mins']

        actual_prep_time = []

        for i in range(0, len(url_list)):
            recipe_url = RecipeBBC(url_list[i])
            recipe_url.url_request()
            actual_prep_time.append(recipe_url.prep_time())

        self.assertEqual(expected_prep_time, actual_prep_time)

    def test_cook_time(self):

        expected_cook_time = ['-', '-', '-', '-', '-', '1 to 2 hours']

        actual_cook_time = []

        for i in range(0, len(url_list)):
            recipe_url = RecipeBBC(url_list[i])
            recipe_url.url_request()
            actual_cook_time.append(recipe_url.cook_time())

        self.assertEqual(expected_cook_time, actual_cook_time)

    def test_serving(self):

        expected_serving = ['-', '-', '-', '-', '-', 'Serves 6']

        actual_serving = []

        for i in range(0, len(url_list)):
            recipe_url = RecipeBBC(url_list[i])
            recipe_url.url_request()
            actual_serving.append(recipe_url.serving())

        self.assertEqual(expected_serving, actual_serving)

    def test_recipe_description(self):

        expected_recipe_description = ['-', '-', '-', '-', '-', 
                                    ('Cassoulet is a hearty dish but with a few little tweaks we’ve reduced the '
                                    'calorie count while keeping the big flavours. Choose really meaty sausages '
                                    'and gammon, take the skin off the chicken and use a very small amount of oil '
                                    '– it all helps. \r\n'
                                    '464 calories per portion.\r\n')]

        actual_recipe_description = []

        for i in range(0, len(url_list)):
            recipe_url = RecipeBBC(url_list[i])
            recipe_url.url_request()
            actual_recipe_description.append(recipe_url.recipe_description())

        self.assertEqual(expected_recipe_description, actual_recipe_description)

    def test_list_ingredients(self):

        expected_ingredients = [[], [], [], [], [],
                                 ['sunflower oil', 'sausages', 'celery', 'carrots', 'onions', 'chicken thighs', 'garlic',\
                                  'gammon', 'chopped tomatoes', 'red wine', 'caster sugar', 'dried chilli', 'bay leaf',\
                                  'thyme', 'cannellini beans', 'butter beans', 'parsley', 'orange']]

        actual_ingredients = []

        for i in range(0, len(url_list)):
            recipe_url = RecipeBBC(url_list[i])
            recipe_url.url_request()
            actual_ingredients.append(recipe_url.list_ingredients())

        self.assertEqual(expected_ingredients, actual_ingredients)

    def test_list_ingredients_amounts(self):

        expected_ingredients = [[], [], [], [], [],
                                ['½ tsp sunflower oil', '6 sausages, at least 85% meat', '4 celery sticks',
                                 '3 carrots', '2 onions, halved and sliced', '6 boneless, skinless chicken thighs (about 450g/1lb)',
                                 '2 garlic cloves, crushed', '200g/7oz piece smoked lean gammon, trimmed and cut into 2cm/1in cubes',
                                 '2 x 400g/14oz cans chopped tomatoes', '150ml/5fl oz red wine (or water)', '1 tsp caster sugar',
                                 '1 tsp dried chilli flakes', '1 bay leaf', '4-5 bushy sprigs fresh thyme',
                                 '400g/14oz can cannellini beans in water, drained and rinsed',
                                 '400g/14oz can butter beans in water, drained and rinsed', 'freshly ground black pepper',
                                 'handful fresh flatleaf parsley', '½ large orange, zest only, finely grated']]

        actual_ingredients = []

        for i in range(0, len(url_list)):
            recipe_url = RecipeBBC(url_list[i])
            recipe_url.url_request()
            actual_ingredients.append(recipe_url.list_ingredients_amounts())

        self.assertEqual(expected_ingredients, actual_ingredients)  

    def test_recipe_instructions(self):

        expected_recipe_instructions = ['-', '-', '-', '-', '-', ['Brush a large non-stick frying pan with the sunflower oil, using the tip of a pastry brush. Add the sausages to the pan and cook over a medium heat for 10 minutes, turning every now and then until nicely browned on all sides. ',
 'Meanwhile, trim the celery and peel the carrots and cut them into diagonal slices about 1.5cm/½in thick.',
 'Preheat the oven to 180C/350F/Gas 4. ',
 'Add the onions to the frying pan and cook with the sausages for 6-8 minutes, stirring regularly until softened and lightly browned.',
 'Trim the chicken thighs of any visible fat - we find a good pair of kitchen scissors does the job well - then cut the thighs in half. ',
 'Add the garlic and chicken pieces to the pan with the sausages and onions and cook for 3-4 minutes, turning the chicken twice until coloured all over. ',
 'Transfer everything to a large flameproof casserole dish. ',
 'Stir in the gammon, celery, carrots, tomatoes, red wine and 300ml/½ pint cold water, then sprinkle over the caster sugar and chilli flakes. Stir in the bay leaf and thyme and season with lots of ground black pepper. ',
 'Bring the cassoulet to a simmer on the hob, then cover with a lid and transfer to the oven. Cook for 45 minutes.',
 'Take the casserole out of the oven and stir in all the beans. Cover with the lid again and put the dish back in the oven for another 30 minutes. ',
 'Just before the cassoulet is ready, prepare the garnish. Chop the parsley roughly and toss with the orange zest in a small bowl. ',
 'Serve large portions of the cassoulet in deep plates or wide bowls with a good sprinkling of the zesty parsley garnish on each one.']]

        actual_recipe_instructions = []

        for i in range(0, len(url_list)):
            recipe_url = RecipeBBC(url_list[i])
            recipe_url.url_request()
            actual_recipe_instructions.append(recipe_url.recipe_instructions())

        self.assertEqual(expected_recipe_instructions, actual_recipe_instructions)

    def test_rating_count(self):

        # Rating count will increase overtime for the page that returns results. 
        # Therefore the test needs to check that a number is returned for that result? 

        expected_rating_count = ['-', '-', '-', '-', '-', 28]
        expected_rating_types = [type(i) for i in expected_rating_count]

        actual_rating_count = []

        for i in range(0, len(url_list)):
            recipe_url = RecipeBBC(url_list[i])
            recipe_url.url_request()
            actual_rating_count.append(recipe_url.rating_count())

        actual_rating_types = [type(i) for i in actual_rating_count]

        self.assertEqual(expected_rating_types, actual_rating_types)

    def test_rating(self):

        # Rating count will increase overtime for the page that returns results. 
        # Therefore the test needs to check that a number is returned for that result? 

        expected_rating = ['-', '-', '-', '-', '-', 4.82]
        expected_rating_types = [type(i) for i in expected_rating]

        actual_rating = []

        for i in range(0, len(url_list)):
            recipe_url = RecipeBBC(url_list[i])
            recipe_url.url_request()
            actual_rating.append(recipe_url.rating())

        actual_rating_types = [type(i) for i in actual_rating]

        self.assertEqual(expected_rating_types, actual_rating_types)

    def test_recipe_category(self):

        expected_recipe_category = ['-', '-', '-', '-', '-', 'Main course']

        actual_recipe_category = []

        for i in range(0, len(url_list)):
            recipe_url = RecipeBBC(url_list[i])
            recipe_url.url_request()
            actual_recipe_category.append(recipe_url.recipe_category())

        self.assertEqual(expected_recipe_category, actual_recipe_category)

    def test_recipe_keywords(self):

        expected_recipe_keywords = ['-', '-', '-', '-', '-', 'continental classics, easy sausage suppers , \
french comfort food, healthy pub grub, autumn, winter, cassoulet, sausage, \
chicken thigh, gammon, cannellini beans, butter beans, dairy free, egg free, \
nut free, Hairy Dieters: How to Love Food and Lose Weight']

        actual_recipe_keywords = []

        for i in range(0, len(url_list)):
            recipe_url = RecipeBBC(url_list[i])
            recipe_url.url_request()
            actual_recipe_keywords.append(recipe_url.recipe_keywords())

        self.assertEqual(expected_recipe_keywords, actual_recipe_keywords) 


    def test_recipe_diets(self):

        expected_recipe_diets = ['-', '-', '-', '-', '-', ['http://schema.org/LowLactoseDiet']]

        actual_recipe_diets = []

        for i in range(0, len(url_list)):
            recipe_url = RecipeBBC(url_list[i])
            recipe_url.url_request()
            actual_recipe_diets.append(recipe_url.recipe_diets())

        self.assertEqual(expected_recipe_diets, actual_recipe_diets) 

if __name__ == '__main__':
    unittest.main()