def is_armstrong_number(number):
    s = str(number)
    exp_No = len(s)
    final_Num = sum(int(i)**exp_No for i in s)
    return final_Num == number
     
        
        
