# Emphasise the Words
# todo The challenge is to recreate the functionality of the title() method into a function called emphasise(). 
#  todo The title() method capitalises the first letter of every word and lowercases all of the other letters in the word.

# ? Examples
# * emphasise("hello world") ➞ "Hello World"

# * emphasise("GOOD MORNING") ➞ "Good Morning"

# * emphasise("99 red balloons!") ➞ "99 Red Balloons!"
# ! Notes
# ! You won't run into any issues when dealing with numbers in strings.
# !  Please don't use the title() method directly :(



def emphasise(txt):
    words = txt.split()  
    emphasised_words = []
    
    for word in words:
        if len(word) > 0:
            
            emphasised_word = word[0].upper() + word[1:].lower()
            emphasised_words.append(emphasised_word)
    
    return ' '.join(emphasised_words)  

# * Test cases
print(emphasise("hello world")) 
print(emphasise("GOOD MORNING"))  
print(emphasise("99 red balloons!")) 
