str1 = input ("Enter a string: ")
count = 0

for s in str1:
    if s.lower() not in 'aeiouAEIOU':
        count+=1

        print("Non-vowel charecter:", count)