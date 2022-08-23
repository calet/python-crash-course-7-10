def create_animal_dict(filename, animal_dict = {}):
    
    try:
        with open(filename, encoding='utf-8') as f:
            names = f.readlines()
    except FileNotFoundError:
        #print(f"{filename} not found!")
        pass
    else:
        if filename == 'catNames.txt':
            animal_dict['cats'] = []
            animal_dict['cats'].extend(names)
        
        if filename == 'dogNames.txt':
            animal_dict['dogs'] = []
            animal_dict['dogs'].extend(names)
        
        return animal_dict
files = ['catNames.txt', 'dog names/dogNames.txt']

for file in files:
    save_dict = create_animal_dict(file)

for species, name in save_dict.items():
    print(f"{species}:\n- {'- '.join(name)}\n")


