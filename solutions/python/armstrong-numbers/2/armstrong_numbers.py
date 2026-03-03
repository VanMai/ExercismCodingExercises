def is_armstrong_number(number):
    s = str(number)
    exp_No = len(s)
    finalNum = sum(int(i)**exp_No for i in s)
    return finalNum == number
     
        
        
