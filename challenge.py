import copy

DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Mentor',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Mariandrea',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():

    all_python_devs =  list(filter(lambda x: x['language'] == 'python', DATA)) # Using filter, generate a list with all the python devs
    all_Platzi_workers = list(filter(lambda x: x['organization'] == 'Platzi', DATA))   # Using filter, generate a list with all the Platzi workers
    adults = list(filter(lambda x: x['age'] > 18, DATA )) # Using filter, generate a list with all people over 18 years old
    
    data_2 = copy.deepcopy(DATA)

    def homeless(test):
        if test['organization'] == '':
            test['homeless'] = True           
        else:
            test['homeless'] = False

        return test
    
    def age_test(test):
        if test['age'] > 30:
            test['old'] = True
        else: 
            test['old'] = False

        return test    
    
 
    workers = list(map(homeless, data_2)) # Using map, generate a new list of people with a key 'homeless' with True or False values, if 'organization' have something or not
    old_people = list(map(age_test, DATA)) # Using map, generate a new list of people with a key 'old' with True or False values, if 'age' is greater than 30 or not

    print('Python devs: ')
    for dev in all_python_devs:
        print(dev['name'])
    print('\n\n')

    print('Platzi workers: ')
    for worker in all_Platzi_workers:
        print(worker['name'])
    print('\n\n')

    print('Adults: ')
    for adult in adults:
        print(adult['name'])
    print('\n\n')

    print('List including homeless: ')
    for worker in workers:
        print(worker)
        print('\n\n')

       
    print('List including old people: ')
    for old in old_people:
        print(old)
        print('\n\n')

    
   

    # Remember: when possible, use lambdas


if __name__ == '__main__':
   
    run()
