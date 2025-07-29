# 2) მოიყვანეთ მაგალითები და ახსენით თუ რატომ არის სტრინგი - Immutable და სია - Mutable.
# ამასთანავე ახსენით ტუ რას ეწოდება Mutable და Immutable.

# Mutable არის მონაცემის ტიპი, რომლის ელემენტების შეცვლა შესაძლებელია, ხოლო Immutable არის მონაცემის ტიპი, რომლის ელემენტების შეცვლა შეუძლებელია.
# მაგალითად, სტრინგი არის Immutable, რადგან მასში არსებული სიმბოლოების შეცვლა შეუძლებელია. თუ გვინდა სტრინგში არსებული სიმბოლოების შეცვლა, უნდა შევქმნათ ახალი სტრინგი. ხოლო სია არის Mutable, რადგან მასში არსებული ელემენტების შეცვლა შესაძლებელია, მაგალითად, შეგვიძლია დავამატოთ ახალი ელემენტი ან შევცვალოთ არსებული ელემენტი.

# 3) მომხმარებელს შემოატანინეთ თავისი სახელი, გვარი, ID ნომერი და ეროვნება.
# ეს ყოველივე შეინახეთ User_info ცვლადში. ჯერ მთლიანი სია დაბეჭდეთ, შემდეგ კი ინდექსინგის საშუალებით 
# გამოიტანეთ სიის თითოეული ელემენტი ტერმინალში.
# user_info = []
# name = input("name: ")
# surname = input("last name: ")
# id_number = input("ID: ")
# user_info.append(name)
# user_info.append(surname)
# user_info.append(id_number)
# print(user_info)  # დაბეჭდავს მთელ სიას
# print("Name:", user_info[0])  # დაბეჭდავს სახელს
# print("Surname:", user_info[1])  # დაბეჭდავს გვარს
# print("ID:", user_info[2])  # დაბეჭდავს ID ნომერს
# 4) შექმენით Vending Machine პროგრამა.

# შექმენით Vending Machine სია სადაც მინიმუმ 10 ცალ პროდუქტს დაამატებთ. მომხმარებელი უნდა ირჩევდეს პროდუქტის ინდექსს და შემდეგ თქვენ პროდუქტის დასახელება უნდა გამოუტანოთ ტერმინალში. (პირობაში დეტალები არ მიწერია, ასერომ ეცადეთ რაც შეიძლება დახვეწილი და მომხმარებლისთვის მოსახერხებელი პროგრამა შექმნათ)4) შექმენით Vending Machine პროგრამა.

# შექმენით Vending Machine სია სადაც მინიმუმ 10 ცალ პროდუქტს დაამატებთ. მომხმარებელი უნდა ირჩევდეს პროდუქტის ინდექსს და შემდეგ თქვენ პროდუქტის დასახელება უნდა გამოუტანოთ ტერმინალში. (პირობაში დეტალები არ მიწერია, ასერომ ეცადეთ რაც შეიძლება დახვეწილი და მომხმარებლისთვის მოსახერხებელი პროგრამა შექმნათ)
# vending_machine = ["Water", "Cola", "Chips", "Chocolate", "Cookies", "Juice", "Gum", "Candy", "Sandwich", "Ice Cream"]
# choice = int(input("Enter the product number (0-9): "))

# if choice == 0:
#     print("You chose:", vending_machine[0])
# elif choice == 1:
#     print("You chose:", vending_machine[1])
# elif choice == 2:
#     print("You chose:", vending_machine[2])
# elif choice == 3:
#     print("You chose:", vending_machine[3])
# elif choice == 4:
#     print("You chose:", vending_machine[4])
# elif choice == 5:
#     print("You chose:", vending_machine[5])
# elif choice == 6:
#     print("You chose:", vending_machine[6])
# elif choice == 7:
#     print("You chose:", vending_machine[7])
# elif choice == 8:
#     print("You chose:", vending_machine[8])
# elif choice == 9:
#     print("You chose:", vending_machine[9])
# else:
#     print("Invalid number!")
# 5) შექმენით Fruits სია: 
# Fruits = ["Strawberry", "Mango", "Melon", "Cherry"]
# სიის მეოთხე ელემეტი ჩაანაცვლეთ "Watermelon"-ით, მეორე ელემენტი კი "Pear"-ით. ტერმინალში დაბეჭდეთ სიის თავდაპირველი და საბოლოო სახე.
# Fruits = ["Strawberry", "Mango", "Melon", "Cherry"]
# print(Fruits)
# Fruits[3] = "Watermelon"  # მეოთხე ელემენტის შეცვლა
# Fruits[1] = "Pear"  # მეორე ელემენტის შეცვლა
# print(Fruits) 

# 6) რამდენიმე ცვლადში შინახეთ სხვადასხვა სიტყვა. ამ სიტყვების გამოყენებით ააწყვეთ ერთი მთლიანი სიტყვა. მაგ.
# ("Moon", "light" -- "Moonlight")
# word1 = "eddy"
# word2 = "X"
# word3 = "oblock"
# combined_word = word1 + word2 + word3 
# print(combined_word) 







