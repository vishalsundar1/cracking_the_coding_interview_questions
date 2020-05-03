#Word frequency: a method to find the frequency of occurences of any given word in a book.

#we use a dictionary to map all the words. we then iterate over the dictionary and increment
#count whenever a key exists.

def word_count(elements):
    #check for '.', ignore if its there
    if elements[-1] == '.': 
        elements = elements[0, len(elements)-1]

    if elements in word_Dict:
        word_Dict[elements] +=1
    else:
        word_Dict.update({elements: 1})
Sentence = "Apple Mango Orange Mango Guava Guava Mango"

#create a dictionary
word_Dict = {}

wordList = Sentence.split()

for elements in wordList:
    word_count(elements)

for allKeys in word_Dict: 
    print ("Frequency of ", allKeys, end = " ") 
    print (":", end = " ") 
    print (word_Dict[allKeys], end = " ") 
    print()  
