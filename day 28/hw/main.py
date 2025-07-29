# 2) კომენტარის სახით ახსენით რატომ ვიყენებთ Slicing-ს Python-ში.
# Slicing-ს ვიყენებთ Python-ში იმისთვის, რომ მივიღოთ სიის ან სტრინგის ნაწილები. ეს საშუალებას გვაძლევს მარტივად მივაწვდოთ კონკრეტული ელემენტები ან სიმბოლოები, რაც განსაკუთრებით სასარგებლოა, როდესაც გვჭირდება მხოლოდ გარკვეული ნაწილი მონაცემებისგან.
# 3) შექმენით რიცხვების სია, სადაც შენახული გექნებათ 10 რიცხვი. Slicing-ის მეშვეობით გამოიტანეთ ამ სიის პირველი ხუთი რიცხვი და გამოიტანეთ ტერმინალში.

# 4) ცვლადში შეინახეთ სიტყვა "Goal-Oriented Academy".
# გამოიყენეთ Slicing რათა აქედან დაბეჭდოთ მხოლოდ სიტყვა "Academy".

# 5) ცვლადში შეინახეთ სიტყვა "Goal-Oriented Academy".
# გამოიყენეთ Slicing რათა აქედან დაბეჭდოთ მხოლოდ სიტყვა "Oriented".

# 6) ცვლადში შეინახეთ თქვენი გვარი. ინდექსინგის საშუალებით გამოიტანეთ თქვენი გვარის პირველი, ბოლო და შუა ასოები.

# 7) შექმენით სია colors = ["Black", "Yellow", "Blue", "Purple", "Orange"]

# სიიდან გამოიტანეთ მხოლოდ Yellow და Black.

# 8) შეინახეთ ცვლადში "Hello, World!". Slicing-ის საშუალებით ამ სტრინგიდან  ამოიღეთ ცალკე სიტყვა "Hello" და ცალკე სიტყვა "World!". შეინახეთ ისინი ცვლადებში და გამოიტანეთ ეკრანზე.
# 1) Slicing-ს ვიყენებთ Python-ში იმისთვის, რომ მივიღოთ სიის ან სტრინგის ნაწილები. ეს საშუალებას გვაძლევს მარტივად მივაწვდოთ კონკრეტული ელემენტები ან სიმბოლოები, რაც განსაკუთრებით სასარგებლოა, როდესაც გვჭირდება მხოლოდ გარკვეული ნაწილი მონაცემებისგან.
# 3) რიცხვების სია
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# პირველი ხუთი რიცხვი
first_five_numbers = numbers[:5]
print(first_five_numbers)
# 4) ცვლადში სიტყვა "Goal-Oriented Academy"
phrase = "Goal-Oriented Academy"
# სიტყვა "Academy"
academy = phrase[16:]
print(academy)
# 5) ცვლადში სიტყვა "Goal-Oriented Academy"
phrase = "Goal-Oriented Academy"
# სიტყვა "Oriented"
oriented = phrase[5:14]
print(oriented)
# 6) ცვლადში თქვენი გვარი
surname = "imerlishvili"
# პირველი ასო
first_letter = surname[0]
# ბოლო ასო
last_letter = surname[-1]
# შუა ასო
middle_letter = surname[len(surname) // 2]
print(f"First letter: {first_letter}, Last letter: {last_letter}, Middle letter: {middle_letter}")
# 7) სია colors
colors = ["Black", "Yellow", "Blue", "Purple", "Orange"]
# Yellow და Black
selected_colors = colors[0:2]
print(selected_colors)  
# 8) ცვლადში "Hello, World!"
greeting = "Hello, World!"
# სიტყვა "Hello"
hello = greeting[:5]
# სიტყვა "World"
world = greeting[7:12]
print(f"Hello: {hello}, World: {world}")
