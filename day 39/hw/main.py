# 2) კომენტარის სახით ჩამოწერეთ ყველა სტრინგის მეთოდი, რომელიც ისწავლეთ. თითოეულს მიუწერეთ დეტალური განმარტება და მათზე მოიყვანეთ თითო-თითო მაგალითი.
# .find() - გამოაქვს string-ში არსებული ინდექსის ციფრი. თუ იგი არ არსებობს მაშინ ტერმინალში გამოიტანს "-1"-ს
# .lower() - string-ის ასოები გამოაქვს პატარა ასოებით
# .upper() - string-ის ასოები გამოაქვს დიდი ასოებით
# .capitalize() - string-ის პირველ ასოს ადიდებს ხოლო დანარჩენს წერს პატარა ასოებით

# 3) მომხმარებელს შემოატანინეთ სიტყვა. ტერმინალში კი დაბეჭდეთ ეს სიტყვა ისე რომ იყოს:

# ყველა პატარა ასო;
# ყველა დიდი ასო;
# პირველი ასო დიდი, ხოლო ყველა დანარჩენი პატარა.
# word = input("Enter your word: ")

# print(word.lower())
# print(word.upper())
# print(word.capitalize())

# 4) მომხმარებელს შემოატანინეთ სამი წინადადება და თითოეულზე გამოიყენეთ სხვადასხვა სტრინგის მეთოდი:
# პირველ წინადადებაზე — .lower()
# მეორე წინადადებაზე — .upper()
# მესამე წინადადებაზე — .capitalize()
# sentence1 = input("Enter your sentence: ")
# sentence2 = input("Enter your sentence: ")
# sentence3 = input("Enter your sentence: ")


# print(sentence1.lower())
# print(sentence2.upper())
# print(sentence3.capitalize())
# 4) ცვლადში შეინახე შენი სახელი. მომხმარებელს შეეკითხე თავისი სახელი, იმ შემთხვევაში თუ თქვენი სახელები ემთხვევა დაბეჭდეთ "Our names are similar!", თუ არ ემთხვევა დაბეჭდეთ "We have different names". გაითვალისწინეთ, რომ მომხმარებელმა შეიძლება თქვენნაირი სახელი შემოიტანოს, თუმცა სახელის ასოები შესაძლოა იყოს სხვადასხვა შრიფტის ზომით, ამიტომ ამან თქვენ პროგრამაში შეფერხება არ უნდა გამოიწვიოს (გამოიყენეთ ნასწავლი სტრინგის მეთოდები)
# my_name = "NIGERIAN"

# name = input("Enter your name: ")

# if my_name.lower() == name.lower():
#     print("Our names are similar!")

# elif my_name.upper() == name.upper():
#     print("Our names are similar!")

# elif my_name.capitalize == name.capitalize():
#     print("Our names are similar!")

# else:
#     print("We have different names")

# 6) ცვლადში შეინახეთ წინადადება, დაწერეთ ისეთი პროგრამა რომ მხოლოდ წინადადების პირველი ასო იყოს დიდი ასოთი, დანარჩენი კი იყოს პატარა.
# sentence = "i love art and music"
# print(sentence.capitalize())

# 7) ცვლადში შეინახეთ რაიმე სტრინგი, შემდეგ .find() ფუნქციის მეშვეობით იპოვეთ რომელ ინდექსზეა კონკრეტული ასო.
# word = "NIGERIANperson"

# print(word.find("y"))

# 8) შექმენით სია, სადაც დაამატებთ რანდენიმე სტრინგს. სიაში დამატებული თითოეული სტრინგი გადაიყვანეთ დიდ ასოებად for ციკლის მეშვეობით.
# list = ["apple", "water melon", "grape", "strawberry"]
# for i in list:
#     print(i.upper())