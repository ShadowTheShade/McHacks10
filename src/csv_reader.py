import csv

with open('questions.txt', mode='r+') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    
    for q_dict in csv_reader:

        for key in q_dict:
            if q_dict[key][0] == "0":
                ans = q_dict[key][1:]
                q_dict[key] = q_dict[key][1:]

        print(f'\nkeys are:{",".join(q_dict)}\n')
        print(f'Category --> {q_dict["category"]}\n\nQuestion --> {q_dict["question"]}\n\nOption 1 --> {q_dict["a1"]}\nOption 2 --> {q_dict["a2"]}\nOption 3 --> {q_dict["a3"]}\nOption 4 --> {q_dict["a4"]}')
        
        
        response = input("ans")
        if response == ans:
            print("Yeah")
        else:
            print("Bruh")
    
    