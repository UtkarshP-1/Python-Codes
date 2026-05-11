# Write a version of a palindrome recognizer that also accepts phrase palindromes such as 
# "Go hanga salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil", 
# "Satan,oscillate my metallic sonatas", "I roamed under it as a tired nude Maori","Rise to vote sir", or the exclamation "Dammit, I'm mad!".
# Note that punctuation, capitalization, and spacing are usually ignored.

import re

def palindrome_recongnizer(line: str) -> bool:
    line = re.sub(r"[^a-zA-Z0-9]",'',line).lower()
    if line[::1] == line[::-1]:
        return True

lines = [
"Go hanga salami I'm a lasagna hog.",
"Was it a rat I saw?",
"Step on no pets",
"Sit on a potato pan, Otis",
"Lisa Bonet ate no basil",
"Satan,oscillate my metallic sonatas",
"I roamed under it as a tired nude Maori",
"Rise to vote sir",
"Dammit, I'm mad!"
]

results = map(palindrome_recongnizer, lines)

for line in lines:
    if palindrome_recongnizer(line):
        print(f'The given line "{line}" is palindrome.')
