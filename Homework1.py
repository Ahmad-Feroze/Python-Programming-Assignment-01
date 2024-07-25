#Task 1:
Anton = 21
Beth = 21 + 6
Chen = Beth + 20
Drew = Chen + Anton
Ethan = Chen
print("Anton is ", Anton)
print("Beth is ", Beth)
print("Chen is", Chen)
print("Drew is", Drew)
print("Ethan is", Ethan)     

#Task 2:
Name = "Ahmad"
Age = 30
city = "Lahore"
sentence = f"{Name} is {Age} years old and lives in {city}."
print(sentence)

#Task 3:
string = "Hello World"
print(string.capitalize())
print(string.upper())
print(string.lower())

#Task 4:
string = "the quick brown fox jumps over the lazy dog"
print (f"index of 'fox' is {string.find("fox")}")
print(f"'the' appears {string.count("the")} times.")

#Task 5:
string = "I love programming in Python"
print(f"{string.replace("Python", "Java")}")

#Task 6:
string = "apple,banana,cherry,dates"
seprater = " "
print(f"{seprater.join(string.split(","))}")

#Task 7:
string = "    Python is fun!     "
justified = string.strip()
print(f"{justified}")
print(f"{justified.ljust(20, "*")}")
print(f"{justified.rjust(20, "*")}")

#Task 8:
num = int(45)
print(f"Binary represenation: {bin(num)}")

#Task 9:
base = 3
exponent = 4
print(f"Power result {base**exponent}")

#Task 10:
value:float = 12.34567
print(f"Rounded to nearest integer{int(value)}")
print(f"Rounded to 2 decimal place {round(value, 2)}")