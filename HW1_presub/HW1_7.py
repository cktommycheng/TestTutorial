#Problem7

filename = input("Enter filename: ")
file = open(filename)

line = file.read()

text = line
text = text.lower() 
wordcount = 0

print(text)

#for i in range(len(text)):
#        if (ord(text[i]) > 96 and ord(text[i])<123 ) or (ord(text[i]) > 47 and ord(text[i])<58):
#            wordcount = wordcount +1     

for i in range(len(text)):
    if text[i] != ' ':
        wordcount = wordcount + 1            

            
print(wordcount)

words = float( len(text.split()) * 1.0)

print ('The average word length of this text is: ', "%.1f"%(wordcount/words),'words' )