def is_armstrong_number(number):
    s = str(number)
    expNo = len(s)
    finalNum = sum(int(i)**expNo for i in s)
    return finalNum == number
     
        
        
