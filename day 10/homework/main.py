# კომენტარის სახით დაწერეთ თუ რა დანიშნულება აქვს type() ფუნქციას და რატომაა მისი გამოყენება მოხერხებული.
#type() ფუნქციას გამოაქვს რა ტიპისაა კოდი მაგ: boolean, ინტეგერ ...
# ჩამოწერეთ ყველა ის ფუნქცია რომელიც “Data Conversion”-ს მოიცავს. გატესტეთ თითოეული ყველაჯ ნასწავლ მონაცემთა ტიპზე.

# bool
# str
# int
# float

# a = 20   boolean
# b = 4
# print(a > b)

# print("string")  string

# a = 1  integer
# print(a) 

# a = 1.1 float
# print(a)


# ცვლადებში შეინახეთ თქვენი სახელი,  გვარი და ასაკი (Integer) . ტერმინალში გამოიტანეთ წინადადება -
# რომელსაც კონკატინაციის შედეგად მიიღებთ. ვიცით რომ String-სა და Integer-ს შორის 
# მათემატიკურ ოპერაციას ვერ შევასრულებთ, შესაბამისად დაწერეთ ისეთი კოდი, რომ Error-ების გარეშე გაეშვას ტერმინალში.

# name = "iura"
# lastname = "imerlishvili"
# age = 15
# print(f"i am {name} {lastname} and i am {age} yeas old") 

#int-ის string-ად გადაქცევა
# string_number = "5"
# real_number = 3

# result = string_number + str(real_number)
# print(result)

# #int-ად გადაქცევა სტრინგის
# string_number = "5"
# real_number = 3
# result = int(string_number) + real_number
# print( result)
# მომხმარებელს შემოატანინეთ 5 რიცხვი. დაწერეთ პროგრამა, რომელიც გამოთვლის და დაბეჭდავს ამ რიცხვების საშუალო არითმეტიკულს. 
# a = float(input("enter any number: "))
# b = float(input("enter any number: "))
# c = float(input("enter any number: "))
# d = float(input("enter any number: "))
# e = float(input("enter any number: "))

# average = (a + b + c + d + e) / 5
# print(average)

# მომხმარებელს შემოატანინეთ ტემპერატურა ცელსიუსში. დაწერეთ პროგრამა, რომელიც 
# მომხმარებლის მიერ შემოტანილ ტემპერატურას გადაიყვანს ფარენგეიტში და დაბეჭდეთ საბოლოო შედეგი. (მოიძიეთ ფორმულა ინტერნეტში)

# celsius = float(input("enter temp in celsius: "))
# fahrenheit = (celsius * 9/5) + 32
# print(fahrenheit)

# მეხუთე დავალების მსგავსად, შემოატანინეთ მომხმარებელს ტემპერატურა, თუმცა ამჯერად - ფარენგეიტში. შემდეგ კი დაწერეთ პროგრამა, 
# რომელიც შემოტანილ ტემპერატურას ცელსიუსში გადაიყვანს და საბოლოოდ დაბეჭდეთ შედეგი.

# fahrenheit = float(input("enter temperature in farenheit: "))
# celsius = (fahrenheit - 32) * 5 / 9
# print(celsius)