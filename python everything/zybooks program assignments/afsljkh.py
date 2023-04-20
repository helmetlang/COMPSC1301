if __name__ == '__main__':
    
    #initializing variables
    text = input()
    new_text = text

    print ("Enter a text, which may contain BFF, IDK, etc.('stop' to end the program):",'You entered:', text)

def expand(new_text):
    if 'BFF' in new_text:
        new_text = new_text.replace('BFF', 'best friend forever')
        print ('Replaced "BFF" with "best friend forever"')
    if 'IDK' in new_text:
        new_text = new_text.replace("IDK", "I don't know")
        print ('Replaced "IDK" with "I don\'t know"')
    if 'JK' in new_text:
        new_text = new_text.replace('JK', 'just kidding')
        print ('Replaced "JK" with "just kidding"')
    if 'TMI' in new_text:
        new_text = new_text.replace('TMI', 'too much information')
        print ('Replaced "TMI" with "too much information"')
    if 'TTYL' in new_text:
        new_text = new_text.replace('TTYL', 'talk to you later')
        print ('Replaced "TTYL" with "talk to you later"')
    print ('Expanded:', new_text)
    return new_text

new_text = expand(text)


#lengths of original and expanded text
print( 'The length of the user input is', len(text))
print( 'The length of the changed input is', len(new_text))
