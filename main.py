import json
from difflib import get_close_matches

data = json.load(open("json_data_extract/dictionary.json"))

def translate(w):
    w = w.lower()

    if w in data:
        return data[w]

    #for getting close matches of a word
    elif len (get_close_matches(w, data.keys())) > 0:
        yn = input ("Did you mean % s insted ? Enter Y if yes, or N if no: " %get_close_matches(w, data.keys())[0])

        yn = yn.lower()
    
        if yn == "y":
            return data[get_close_matches(w, data.keys())[0]]
        
        elif yn =="n":
            return "This word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "This word doesn't exist. Please double check it." 

#driver
word = input("Enter word: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
    input('Press Enter to exit...')
