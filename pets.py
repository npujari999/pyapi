from pprint import pprint

pets_dict = {'dogs': [{'name':'Odie', 'age': 1, 'color':'tri-color'}, {'name':'Sparky', 'age': 2, 'color': 'white'}], 'cats':[{'name':
    'garfied', 'age': 3, 'color': 'orange'}, {'name':'Tom', 'age': 5, 'color': 'blue'}]}

pprint(pets_dict)

print(f"My dog\'s name is {pets_dict['dogs'][0]['name']},  age {pets_dict['dogs'][0]['age']} and his color is  {pets_dict['dogs'][0]['color']}")
print(f"My cat\'s name is {pets_dict['cats'][1]['name']},  age {pets_dict['cats'][1]['age']} and his color is  {pets_dict['cats'][1]['color']}")
