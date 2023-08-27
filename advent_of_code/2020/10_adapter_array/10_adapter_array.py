from collections import defaultdict

def adapter_array(filename):
    adapters = set()
    max_adapter = 0
    with open(filename, 'rt', encoding = 'utf-8') as file:
        for line in file:
            adapter = int(line.strip())
            adapters.add(adapter)
            if adapter > max_adapter:
                max_adapter = adapter
    # built-in adapter
    built_in_adapter = max_adapter + 3
    adapters.add(built_in_adapter)
    # print(adapters)
    
    # outlet is 0
    prev = 0
    curr = 1
    diff_dict = defaultdict(int)
    while curr < built_in_adapter + 1 and prev < curr <= prev + 3:
        if curr in adapters:
            diff = curr - prev
            diff_dict[diff] += 1
            prev = curr
            
        curr += 1
    
    # print(diff_dict)
    p1_answer = diff_dict[1] * diff_dict[3]
    print(f"P1:\t{p1_answer}")

adapter_array('sample.txt')
adapter_array('sample2.txt')
adapter_array('input.txt')