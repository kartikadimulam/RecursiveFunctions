
def integerDivision(n, k):
    
    if n<k:
        return 0

    else:
        return 1 + integerDivision(n-k, k)


def collectEvenInts(listofInt):

    if listofInt != []:
        if listofInt[0] % 2 == 0:
            return [listofInt[0]] + collectEvenInts(listofInt[1:])
        else:
            return [] + collectEvenInts(listofInt[1:])
        
    else:
        return []

def countVowels(someString):
    
    vowellist = ["a",'e','i','o','u']

    if someString != '':
        if someString[0].lower() in vowellist:
            return 1 + countVowels(someString[1:])
        else:
            return 0 + countVowels(someString[1:])
    else:
        return 0

def reverseString(s):
    
    if s != '':
        return s[-1]+reverseString(s[:-1])

    else:
        return ''

def removeSubString(s,sub):
    if sub in s:
        index = s.find(sub)
        return s[:index] + removeSubString(s[index+len(sub):],sub)
    else:
        return s

