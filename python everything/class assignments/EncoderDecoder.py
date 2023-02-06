message = input("Enter a message to encode or decode: ") # Get a message
message = message.lower()           # Make it all UPPERCASE :) ## Edit: Makes them lowercase now
output = ""                         # Create an empty string to hold output
for letter in message:              # Loop through each letter of the message
    if letter.islower():            # If the letter is in the alphabet (A-Z), ## Edit: Now checking in lowercase letters
        value = ord(letter) + 13    # shift the letter value up by 13,
        letter = chr(value)         # turn the value back into a letter,
        if not letter.islower():    # and check to see if we shifted too far ## Edit: Checking lowercase now
            value -= 26             # If we did, wrap it back around Z->A
            letter = chr(value)     # by subtracting 26 from the letter value
    output += letter                # Add the letter to our output string
output = output.capitalize()        # Adds a string method to allow for Capitalization of the first word
print("Output message: ", output)   # Output our coded/decoded message
