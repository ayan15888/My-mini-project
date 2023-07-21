import random
import string
Word=int(input("Enter the length of the password: "))
character=string.ascii_letters+string.digits+string.punctuation
pasgen=''.join(random.choice(character) for i in range(Word))
print(pasgen)
