import os 
         
all_files = os.listdir("10-10/books")   

files = []
for file in all_files:
    files.append(file)

for file in files:
    with open(f"10-10/books/{file}", encoding='utf-8') as book:
        my_book = book.read()

    read = my_book.split()
    print(f"book file: {file}")
    print(f"about {len(read)} words")
    print(f"how many 'the': {str(read).lower().count('the')}\n")
    
        
    