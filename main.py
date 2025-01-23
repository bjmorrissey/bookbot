import re

with open("books/frankenstein.txt") as f:
    file_contents = f.read().lower()
    # print(file_contents)
    words = len(file_contents.split())

    def letterCount(text):
        
        dict = {}
        for letter in text: 
            if (letter in dict):
                dict[letter] += 1
            else: 
                dict[letter] = 1

        return dict

    

    def report(text):
        only_letters = re.findall('[a-z]', text)
        letters = letterCount(only_letters)
        output_string = f'--Begin report of books/frankenstein.txt\n{words} words found in the document\n\n'

        for letter in letters: 
            output_string += f"The '{letter}' character was found {letters[letter]} times\n" 
    
        print(output_string)    
        return output_string      
     
    report(file_contents)

