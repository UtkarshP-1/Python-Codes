# Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's language"). 
# That is, double every consonant and place an occurrence of "o" in between. 
# For example, translate("this is fun") should return the string "tothohisos isos fofunon".

def translate(input_str: str) -> str :
    blank_lst = []
    for i in list(input_str):
        if i not in ('a','e','i','o','u',' '):
            blank_lst.append(i+'o'+i)
        else:
            blank_lst.append(i)
    return ''.join(blank_lst)

input_str = 'this is fun'

output_str = translate(input_str)

print(output_str)
