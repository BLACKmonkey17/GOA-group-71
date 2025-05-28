# # 2) გაიხსენეთ და დაწერეთ თუ რა შედეგს ვიღებთ შედარების და ლოგიკური ოპერაციების გამოყენებისას.
# # Boolean მნიშვნელობები (True და False)

# # 3) ჩამოწერეთ ყველა შესაძლო ლოგიკური გამოსახულება (and და or ოპერატორების გამოყენებით)

# # and - და
# print(True and True) # Ouput: True
# print(True and False) # Ouput: False
# print(False and True) # Ouput: False
# print(False and False) # Ouput: False

# # or - ან
# print(True or True) # Ouput: True
# print(True or False) # Ouput: True
# print(False or True) # Ouput: True
# print(False or False) # Ouput: False

# # 4)  რას გამოიტანს მოცემული კოდები?

# # • False or True and True and False
# print(False or True and True and False)

# # • True and False or False or True
# print(True and False or False or True)

# # • True or True and False or True or False and True or False
# print(True or True and False or True or False and True or False)

# # 5) დაწერეთ სახლის გაგრილების სისტემის პროგრამა.
# # ვთქვათ, როდესაც სახლში ტემპერატურა 30 გრადუსს ასცდება - ავტომატურად უნდა ჩაირთოს გაგრილების სისტემა. იმის გასაგებად თუ რა ტემპერატურაა სახლში, მომხმარებელს იგი შემოატანინეთ input() ფუნქციის მეშვეობით. (გამოიყენეთ მხოლოდ ლოგიკური ოპერატორები)

# house_temp = float(input("What's the temperature?: "))
# print(house_temp > 30)

# # HARD LVL:
# # 6) დაწერეთ ოთახის გაგრილების სისტემის პროგრამა, but there’s a twist:

# # ჩათვალეთ, რომ პროგრამა მხოლოდ იმ შემთხვევაში აღიქვამს ოთახის ტემპერატურას, თუ იგი ფარენგეიტშია გადმოცემული. (სისტემა ჩაირთვება მაშინ, როდესაც ტემპერატურა 89.6 ფარენგეიტს ასცდება). 
# # ერთადერთი გასათვალისწინებელი ფაქტი ის არის, რომ მომხმარებელს ოთახის ტემპერატურა გრადუსებში შემოაქვს. 


# temp = float(input("Enter temperature in celcius: "))
# farenheit = (temp * 9/5) + 32
# print(farenheit > 89.6)

# ეცადეთ დაწეროთ პირობის მიხედვით ისეთი ოთახის გაგრილების სისტემის პროგრამა, რომელიც სწორად იმუშავებს 