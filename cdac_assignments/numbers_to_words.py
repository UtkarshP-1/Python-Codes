# Print the given number in words.(eg.1234 => one two three four)

int_to_char = {
    '1':'one',
    '2':'two',
    '3':'three',
    '4':'four',
    '5':'five',
    '6':'six',
    '7':'seven',
    '8':'eight',
    '9':'nine',
    '0':'zero'
}

nums = list(input("Enter a number : "))

for i in nums:
    print(int_to_char.get(i), end=' ')
