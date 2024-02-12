from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
  cipher_text = ""
  if shift > len(alphabet):
    shift %= len(alphabet)
  if direction == "encode" or direction == "decode":
    for letter in text:
      if letter not in alphabet:
        cipher_text += letter
      else:
        find = alphabet.index(letter)
        if direction == "encode":
          push = find + shift
          if push >= len(alphabet):
            push -= len(alphabet)
        elif direction == "decode":
          push = find - shift
          if push <= 0:
            push -= 0
        push_find = alphabet[push]
        cipher_text += push_find
    print(f"The {direction}d text is {cipher_text}")
  else:
    print("I am sorry. I could not understand. Please try again.")

print(logo)
restart_def = "yes"
while restart_def == "yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(text, shift, direction)
  restart_def = str(input("Type 'yes' if you want to go again or type 'no' to quit.\n")).lower()
  if restart_def == "no":
    print("Goodbye")
  elif restart_def != "yes":
    print("I am sorry. I could not understand. Please try again.")
    restart_def = str(input("Type 'yes' if you want to go again or type 'no' to quit.\n")).lower()