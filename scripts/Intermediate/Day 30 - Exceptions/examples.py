
# with open("text.txt") as file: # Will fail if file does not exist
#     file.read()

# Try/Catch/Else/Finally
try: # try attempts to do the thing
    file = open("scripts\\Intermediate\\Day 30 - Exceptions\\text.txt", "r")
    dict = {"key":"val"}
    print(dict["key"])
except FileNotFoundError: # except handles an exception
    file = open("scripts\\Intermediate\\Day 30 - Exceptions\\text.txt", "w")
except KeyError as key: # except handles an exception
    print(f"Key {key} does not exist.")
else: # what to do if there are no exceptions
    text = file.read()
    print(f"Text: {text}")
finally: # Do this regardless of what worked or didn't work up above. 
    file.close()
    print("Program terminating")
    # Define a new exception using the raise keyword
    # raise KeyError("False Flag")