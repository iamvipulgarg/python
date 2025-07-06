s1 = "this is s1ing,checking s1ing functions"
sub = 'H'
s1='Hello'
print(s1.upper()) #Into Upper Case
print(s1.lower()) #Into Lower Case
print(s1.swapcase()) #Swap upper into lower & vice versa
print(s1.title()) #Capitlize every first charcter or word
print(s1.capitalize()) # Capitlize first charcter of every line

print(s1.isalpha())	 # True if all characters are alphabets
print(s1.isdigit())	 # True if all characters are digits
print(s1.isalnum())	 # True if all characters are alphanumeric
print(s1.isspace())	 # True if all characters are whitespace
print(s1.islower())	 # True if all characters are lowercase
print(s1.isupper())	 # True if all characters are uppercase
print(s1.startswith(sub))	 # Checks if s1ing starts with subs1ing
print(s1.endswith(sub)) #Checks if s1ing ends with subs1ing
s1="a5c6d3"
# aaaaaccccccddd 
# ord('A')
# chr(65)

# ch = ''
# s2=''
# for i in s1:
    # if i.isalpha():
        # ch=i
    # else:
        # s2=s2+chr(ord(ch) + int(i))
# print(s2)

s3 = "aaabbc"
s4=''
check=[]
for i in s3:
    count  = s3.count(i)
    if i not in check:
        check.append(i)
        s4=s4+i + str(count)
print(s4)


# for i in s1:
    # if i.isalpha():
        # ch=i
    # else:
        # s2=s2+ch * int(i)
# print(s2)