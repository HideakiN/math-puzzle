num = 11

while True:
    
    dec_list = []
    bin_list = []
    oct_list = []
    bin_list = list(bin(num))[::-1]
    bin_list.pop(), bin_list.pop()
    oct_list = list(oct(num))[::-1]
    oct_list.pop(), oct_list.pop()
    dec_list = list(str(num))
    if bin_list == bin_list[::-1]:
        if oct_list == oct_list[::-1]:
            if dec_list == dec_list[::-1]:
                print("10進数：{}".format(num))
                print("2進数 ：{}".format(bin_list))
                print("8進数 ：{}".format(oct_list))
                break

    num = num + 2
