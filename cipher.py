import string
"""
def caesar(text, shift=1):
    alpha = string.ascii_lowercase
    mask = alpha[shift:] + alpha[:shift]
    table = str.maketrans(alpha, mask)
    return text.translate(table)
"""
def shift_n(text, shift):
    if text not in string.ascii_lowercase:
        return text
    new_text = ord(text) + shift
    while new_text > ord("z"):
        new_text -= 26
    while new_text < ord("a"):
        new_text += 26
    return chr(new_text)

def caesar2(msg, shift):
    enc_list = [shift_n(text, shift) for text in msg]
    return "".join(enc_list)

text=input("Enter Text --->  ")
shift=int(input("Enter Spaces To Shift ---> "))
cipher=caesar2(text,shift)
print(cipher)