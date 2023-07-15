letter=input('Enter any letter:')
letter1=letter.lower()
vowels=list('aeiou')   # ['a','e','i','o','u']
if letter1.isdigit():
    print('Invalid Input')
elif letter1 in vowels:
    print('Vowel')
else:
    print('Consonant')



