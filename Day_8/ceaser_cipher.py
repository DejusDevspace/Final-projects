alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
import art

def ceaser(start_text, shift_number, cipher_decision):
    end_text = ""
    if cipher_decision == "decode":
        shift_number *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_number
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"The {cipher_decision}d text is {end_text}")

print(art.logo)

continue_cipher = True
while continue_cipher:
    decision = input("Type 'encode' or 'decode':  ").lower()
    text = input("Type your message: ").lower()
    shift = int(input("shift number you want to use: "))
    shift = shift % 26
    ceaser(start_text= text, shift_number= shift, cipher_decision= decision)

    responce = input("Do you want to continue? 'yes' or 'no'?\n").lower()
    if responce == "no":
        continue_cipher = False
        print("Goodbye!!!")


