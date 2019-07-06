def print_num(num):
    new_num=list(num)
    for i in range(len(num)):
        print('\n{}: '.format(new_num[i]),end='')
        for j in range(int(new_num[i])):
            print(new_num[i],end='')
    print('\n')

print_num(input('>>'))
    
