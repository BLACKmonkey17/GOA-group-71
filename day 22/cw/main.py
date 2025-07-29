
# 1) დაწერეთ თუ რა დანიშნულება აქვს if, elif და else-ს.

# 2) ცვლადში შეინახეთ თქვენი გვარი. შემდეგ მომხმარებელს შემოატანინეთ თავისი გვარი. თუ თქვენი გვარები დაემთხვევა გამოიტანეთ "Our surnames are similar", სხვა შემთხვევაში "Our surnames are not similar"

# 3) ცვლადში შეინახეთ თქვენი სიმაღლე. მომხმარებელსაც შეეკითხეთ მისი სიმაღლე.

# • თუ შენ უფრო მაღალი ხარ გამოიტანე: "I'm taller than you."

# • თუ მომხმარებელი უფრო მაღალია გამოიტანე: "You're taller than me"

# • თუ ტოლი სიმაღლეების ხართ, მაშინ დაბეჭდეთ "We have equal heights".

# 1) if elif და else გამოიყენება პირობითი გამოთქმების შესასრულებლად if გამოიყენება პირველ რიგში, შემდეგ 
# შეიძლება იყოს რამდენიმე elif რომელიც შემოწმებს დამატებით პირობებს და ბოლოს else რომელიც შესრულდება,
#  თუ არცერთი პირობა არ შესრულდა.
# 2)
# surname = "imerlishvili"  გვარი
# user_surname = input("Enter your surname: ")  გვარი 2
# if user_surname == surname: 
#     print("Our surnames are similar")
# else:
#     print("Our surnames are not similar")
# 3)
# height = 175   სიმაღლე
# user_height = int(input("Enter your height: "))  სიმაღლე 2
# if user_height > height:
#     print("You are-- taller than me")
# elif user_height < height:
#     print("Im taller than you")
# else:
#     print("We have equal heights")
# HARD LVL
# --------

# 5) დაწერეთ პროგრამა, რომელიც მომხმარებლს მოსთხოვს, რომ შემოიტანოს დადებითი რიცხვი. 
# თუ მომხმარებელი შემოიტანს უარყოფით რიცხვს ან ნულს, პროგრამამ უნდა მოსთხოვოს რიცხვის თავიდან შემოტანა

# useris_ricxviii = int(input("Please enter a positive number: "))
# while useris_ricxviii <= 0:
#     print("axlidan.")
#     useris_ricxviii= int(input("Please enter a positive number: "))
# print(f"You entered a positive number: {useris_ricxviii}")
