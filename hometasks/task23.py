alphabet = "abcdefghijklmnopqrstuvwxyz"

def decode_char(letter, offset):
    
    if letter in alphabet and offset <= len(alphabet):
        return alphabet[alphabet.index(letter)-int(offset)]
    else:
        return letter
     

encode_str = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."
count = 1

while count <= len(alphabet):
    decode_str = ''
    for i in encode_str:
        decode_str += decode_char(i,count)
    print("Вариант расшифровки:",decode_str)
    count += 1
        
    
    


