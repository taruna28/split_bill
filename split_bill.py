import random
print("Enter the number of friends joining (including you): ")
try:
    all_person = int(input())
    print("")
    if all_person> 0:
        dictionary = {}

        print("Enter the name of every friend (including you), each on a new line:")
        for i in range(all_person):
            # dictionary[i]=input()
            person= input()
            dictionary[person]=0
        # print(dictionary)
        print("Enter the total bill value:")
        total = int(input())
        split = total/all_person
        split_dict = dict.fromkeys(dictionary, round(split,2))
        # print(split_dict)
        print('''Do you want to use the "Who is lucky?" feature? Write Yes/No:''')
        feature = input()
        if feature=="Yes":
            list_name = [key for key in split_dict]
            Name = random.choice(list_name)
            print(f"{Name} is the lucky one!")
            split = total/(all_person-1)
            split_dict = dict.fromkeys(dictionary, round(split, 2))
            split_dict[Name]=0
            print(split_dict)
        else:
            print("No one is going to be lucky")
            print(split_dict)
    else :
        print("No one is joining for the party")

except Exception:
    print("No one is joining for the party")
