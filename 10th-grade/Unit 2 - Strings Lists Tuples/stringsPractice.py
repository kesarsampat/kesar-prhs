'''
Kesar Sampat 
HCP Period 3 
Unit 2 - Strings/Lists/Tuples
Strings practice program uses the given words to form the following sentence:

He is Never On The Outside Looking In

'''

word1 = "insideout"
word2 = "nevertheless"
word3 = "upsidedown"
word4 = "looking"

heis = word2[6:8] + " " + word1[3:1:-1]
never = word2[:5]
on = word4[1] + word4[5]
the = word2[5:8]
outside = word1[6:] + word3[2:6]
inWord = word1[0:2]


sentence = heis + " " + never + " " + on + " " + the + " " + outside + " " + word4 + " " + inWord + "."

sentence = sentence.title() #convert to title case (first letters caps)
print(sentence)

print(heis)
