from lab03 import integerDivision
from lab03 import collectEvenInts
from lab03 import countVowels
from lab03 import reverseString
from lab03 import removeSubString

def test_integerdivision():
    
    assert integerDivision(27,6) == 4
    assert integerDivision(15,4) == 3
    assert integerDivision(39,8) == 4
    assert integerDivision(10,3) == 3

    
def test_collectints():

    assert collectEvenInts([1,2,3,4,5]) == [2,4]
    assert collectEvenInts([5,3,7,8,9]) == [8]
    assert collectEvenInts([2,6,5,7,18,11]) == [2,6,18]
    assert collectEvenInts([5,7,9])==[]

def test_countvowels():

    assert countVowels('Bet')==1
    assert countVowels('legume')==3
    assert countVowels('')==0

def test_stringreverse():

    assert reverseString('Yodel')=='ledoY'
    assert reverseString('CMPSC8')=='8CSPMC'
    assert reverseString('banter')=='retnab'
    assert reverseString('')==''

def test_removesubstring():

    assert removeSubString('alphabetagammabeta','beta')=='alphagamma'
    assert removeSubString('Poppopoppopoppopoopopopp','pop')=='Popopopooopp'
    assert removeSubString('iototaoiotosoiot','iot')=='otaooso'
    

    
