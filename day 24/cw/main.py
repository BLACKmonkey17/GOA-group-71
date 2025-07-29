# შექმენით ხილის სია, სადაც შეინახავთ მინიმუმ 5 ელემენტს. ჯერ ტერმინალში დაბეჭდეთ 
# მთლიანი სია, შემდეგ სიიდან გამოიტანეთ პირველ ინდექსზე მდგომი ელემენტი.
fruits = ["apple", "banana", "cherry", "alucha", "elderberry"]
print("Full list of fruits:", fruits)
print("First fruit:", fruits[0])

# შექმენით სახელების სია. სიიდან დაბეჭდეთ პირველი და ბოლო ელემენტები დადებითი Indexing-ის გამოყენებით.
names = ["lasha", "gio", "ani", "elene", "lika", "saba"]
a = names[0]
b = names[5]
print("First name:", a)
print("Last name:", b)
# შექმენით პროდუქტების სია. სიიდან დაბეჭდეთ პირველი და ბოლო ელემენტები უარყოფითი Indexing-ის გამოყენებით.
products = ["milk", "bread", "cheese", "eggs", "butter"]
first_product = products[-5]  # First element
last_product = products[-1]  # Last element
print("First product:", first_product)
print("Last product:", last_product)