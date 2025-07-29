# 2) მოცემულია სტრინგი: "Programming"
string = "Programming"
print(string[:5])  # დაბეჭდეთ მხოლოდ პირველი 5 სიმბოლო.
# დაბეჭდეთ მხოლოდ პირველი 5 სიმბოლო.


# • დაბეჭდეთ ბოლო 3 სიმბოლო.
print(string[-3:])  # დაბეჭდეთ ბოლო 3 სიმბოლო.

# • დაბეჭდეთ სტრინგი შებრუნებულად.
print(string[::-1])  # დაბეჭდეთ სტრინგი შებრუნებულად.


# 3) მოცემულია სია: fruits = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']
# ჯერ სიიდან ამოიღეთ შუა სამი ელემენტი, შემდეგ დაბეჭდეთ სიის ყოველი მეორე ელემენტი.
fruits = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']
# შუა სამი ელემენტი: 'banana', 'cherry', 'date'
# del fruits[1:4]  # ამოიღეთ შუა სამი ელემენტი
# print(fruits)  # დაბეჭდეთ განახლებული სია
# ყოველი მეორე ელემენტი: 'apple', 'fig'
# print(fruits[::2])  # დაბეჭდეთ სიის ყოველი მეორე ელემენტი

# 4)  ცვლადში შეინახეთ სტრინგი, სადაც Alphabet-ის ყველა ასოს ჩაწერთ. 
# alphabet = "abcdefghijklmnopqrstuvwxyz"

# • ამოიღეთ სტრინდიდან ყველა მესამე სიმბოლო Slicing-ის გამოყენებით.

# sliced_alphabet = alphabet[::3]  # ამოიღეთ ყველა მესამე სიმბოლო
# print(sliced_alphabet)  

# • შებრუნებული სტრინგიდან ამოღეთ მხოლოდ ყოველი მეორე სიმბოლო.
# reversed_alphabet = alphabet[::-1]  # შებრუნებული სტრინგი
# every_second_reversed = reversed_alphabet[::2]  # ყოველი მეორე სიმბოლო
# print(every_second_reversed)

# 5) მოცემულია სტრინგი: text = "IndexingAndSlicingIsPowerful"
text = "IndexingAndSlicingIsPowerful"

# ამოიღეთ text ცვლადიდან სიტყვა "Slicing". შემდეგ შეაბრუნეთ და გამოიტანეთ შედეგის სახით ეკრანზე.
slicing_word = text[10:17]  # ამოიღეთ სიტყვა "Slicing"
reversed_slicing = slicing_word[::-1]  # შებრუნებული სიტყვა
print(reversed_slicing)  

# 6) მოცემულია სტრინგი: word = "Programming"
word = "Programming"

# • დაბეჭდეთ სტრინგი უკუღმა ისე, რომ გამოტოვებული იყოს ყოველი მეორე ასო.
reversed_word = word[::-1]  # სტრინგი უკუღმა
every_second_reversed_word = reversed_word[::2]  # გამოტოვებული ყოველი მეორე ასო
print(every_second_reversed_word)  

# • ამოჭერით სტრინგი შუა სამი ასო.

# • შეაერთეთ მხოლოდ ლუწ ინდექსებზე მყოფი ასოები.
