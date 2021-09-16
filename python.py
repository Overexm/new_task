
def func(input_l, ind=''):
 
    if len(input_l) == 0:
        print(ind)
 
    for i in range(len(input_l)):
 
        input_L = ind + input_l[i]
        index_s = input_l[0:i] + input_l[i+1:]
 
        func(index_s, input_L)
 
 
if __name__ == '__main__':
 
    s = 'abs'
    func(s)