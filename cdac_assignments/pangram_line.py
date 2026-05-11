# A pangram is a sentence that contains all the letters of the English alphabet at least once, for example: The quick brown fox jumps over the lazy dog. Your task here is to write a function to check a sentence to see if it is a pangram or not.

# Solution 1
string1 = "The quick brown fox jumps over the lazy dog"
string2 = "Just another line to check" 

def is_pangram(s: str) -> bool:
    alphabet = (' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    if set(alphabet) == set(s.lower().strip()):
        print("The given sentence is pangram")
    else:
        print("The given sentence is NOT pangram")
    
is_pangram(string1)
is_pangram(string2)

# Solution 2
def check_pangram(line: str) -> bool:
    line = set(line.lower())
    # The ord() function returns the number representing the unicode code of a specified character
    dist_list = [char for char in line if ord(char) in range(ord('a'), ord('z') + 1)]
    if len(dist_list) == 26:
        return 'Line is a Pangram'
    else:
        return 'Line is not a Pangram'


line1 = "The quick brown fox jumps over the lazy dog"
line2 = "Just another line to check"

print(check_pangram(line1))
print(check_pangram(line2))
