age = 100
age_is_greater_than_50 = age >50;
print(age_is_greater_than_50)
if age_is_greater_than_50:
    print("Eletkor nagyobb mint 50")
    print("Sajnos")
    if age < 100:
        print("De kisebb, mint 100")
else:
    print("Eletkor kisebb, mint 50")
print("Program vege")