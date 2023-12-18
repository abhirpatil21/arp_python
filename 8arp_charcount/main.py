print("Count chars in words")
word1 = input("Enter first word : ")
word2 = input("Enter second word : ")

all_word = word1 + " " + word2

lower_word = all_word.lower()
upper_word = all_word.upper()
print(f"Lower case : {lower_word} \n Upper case : {upper_word}")

#search for patil in name

s = lower_word.count("s")
h = lower_word.count("h")
r = lower_word.count("r")
e = lower_word.count("e")
y = lower_word.count("y")
a = lower_word.count("a")

shreya_count = s + h + r + e + y + a

s = lower_word.count("s")
w = lower_word.count("w")
a = lower_word.count("a")
r = lower_word.count("r")
a = lower_word.count("a")

swara_count = s + w + a + r + a

print(f"shreya count : {shreya_count} \n swara count : {swara_count}")


