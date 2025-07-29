# 2) დაწერეთ პროგრამა, სადაც თავდაპირველად მომხმარებელს შემოატანინებთ ანგარიშის პაროლს,
# შემდეგ შეეკითხეთ რომ გაიმეოროს იქამდე, სანამ არ დაემთხვევა შეყვანილი პაროლი.
# user_pass = input("enter your password: ")
# while True:
#     confirm_pass = input("Please re-enter your password: ")
#     if confirm_pass == user_pass:
#         print("Password confirmed successfully!")
#         break
#     else:
#         print("Passwords do not match. Please try again.")
# 3) შექმენით Number guess game:

# ცვლადში შეინახეთ სასურველი რიცხვი. მომხმარებელს Input-ის მეშვეობით შეეკითხეთ ეცადოს რიცხვის გამოცნობა, 
# ვერ გამოცნობის შემთხვევა გამოუტანეთ "Try again" და იქამდე გამოუტანეთ Input ველი სანამ არ გამოიცნობს რიცხვს. 
# წარმატებით გამოცნობის შემთხვევაში გამოუტანეთ "You guessed the number sucessfully!".
# num1 = 2
# guess_the_num = int(input("Try to guess the number: "))
# while guess_the_num != num1:
#     print("Try again")
#     guess_the_num = int(input("Try to guess the number: "))
# print("You guessed the number successfully!")

# 4) შექმენით სია, სადაც შეინახავთ თქვენს საყვარელ ცხოველებს. გამოიტანეთ სიიდან პირველი და ბოლო ელემენტი და ერთ ხაზზე დაბეჭდეთ.
# animals = ["ძაღლი", "მეგელი", "კატა"]
# print(f"i love {animals[0]} and {animals[2]}") 

# 5) შექმენით სია და მასში შეინახეთ თქვენი საყვარელი ფერები (მინიმუმ 5).
# გამოიყენეთ უარყოფითი ინდექსინგი (Negative Indexing) იმისთვის, რომ გამოიტანოთ სიის მესამე ელემენტი.
# colors = ["black", "white", "red", "blue", "green"]
# print(colors[-3])  

# HARD LEVEL:

# შექმენით სახელების სია და მასში დაამატეთ 3 სახელი, თუმცა სამივე სახელი უნდა იყოს მომხმარებლის მიერ შემოტანილი. დაბეჭდეთ სიის მნიშვნელობა.
# names = []
# names.append(input("Enter names: "))
# names.append(input("Enter names: "))
# names.append(input("Enter names: "))
# print(names)

