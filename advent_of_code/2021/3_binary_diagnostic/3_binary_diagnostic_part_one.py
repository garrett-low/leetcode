def diag(filename):
    with open(filename, 'rt', encoding = 'utf-8') as file:
        first_line = file.readline().strip()
        file.seek(0)
        
        zero_bit = [0] * len(first_line)
        one_bit = [0] * len(first_line)
        print(zero_bit)
        print(one_bit)
        for line in file:
            line = line.strip()
            for bit_idx in range(len(line)):
                if line[bit_idx] == '0':
                    zero_bit[bit_idx] += 1
                else:
                    one_bit[bit_idx] += 1
        
        print(zero_bit)
        print(one_bit)
        gamma_list = []
        epsilon_list = []
        for bit_idx in range(len(zero_bit)):
            if zero_bit[bit_idx] > one_bit[bit_idx]:
                gamma_list.append(0)
                epsilon_list.append(1)
            else:
                gamma_list.append(1)
                epsilon_list.append(0)
        
        print(gamma_list)
        print(epsilon_list)
        
        gamma = 0
        epsilon = 0
        for i in range(len(gamma_list) - 1, -1, -1):
            if gamma_list[i] == 1:
                gamma += 1 << (len(gamma_list) - i - 1)
            else:
                epsilon += 1 << (len(gamma_list) - i - 1)
            
        print(gamma)
        print(epsilon)
        print(gamma * epsilon)

diag('sample.txt')
diag('input.txt')