with open('catNames.txt') as cN:
    c_names = cN.readlines()

with open('dogNames.txt') as dN:
    d_names = dN.readlines()

animal_dict = {'cats': [], 'dogs': []}

animal_dict['cats'].extend(c_names)

animal_dict['dogs'].extend(d_names)

for species, name in animal_dict.items():
    print(f"{species}:\n- {'- '.join(name)}\n")