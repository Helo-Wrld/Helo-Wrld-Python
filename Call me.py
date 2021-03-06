import sys

def num(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isalnum():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isalnum():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isalnum():
            return False
    return True


while True:
    print("Enter to see if you have an eligible phone number(or 'exit' to finish): ", end='')
    call = input()
    if call == 'exit':
        sys.exit()
    if len(call) != 12:
        print("Couldn't find phone number, try again")
    for t in range(len(call)):
        chunk = call[t:t+12]
        if num(chunk):
            print("Phone number found: " + chunk)
print("Done")
