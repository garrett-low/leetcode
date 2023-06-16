# I didn't reset inspect_count between my testing, so the final result was wrong.
# I was reusing the same monkeys across my tests...........................

import inspect

class Monkey:
    def __init__(self, ident, items, inspect_fn, test_fn, test_mod):
        self.ident = ident
        self.items = items
        self.inspect_fn = inspect_fn
        self.test_fn = test_fn
        self.test_mod = test_mod
        self.inspect_count = 0
    def __str__(self):
        retval = f"Monkey {self.ident}:\t {self.inspect_count}"
#         retval = f"Monkey {self.ident}:\t{self.items}, inspect count: {self.inspect_count}"
#         retval += f"\t\t{inspect.getsource(self.inspect_fn).strip()}\n"
#         retval += f"\t\t{inspect.getsource(self.test_fn).strip()}"
        return retval

# I'm not going to bother with reading in from the input file...
def monkey_business(monkeys, is_part_two = False):
    if is_part_two:
        total_rounds = 10000
        test_mod = 1
        for monk in monkeys:
            test_mod *= monk.test_mod
        print(test_mod)
    else:
        total_rounds = 20
#     print(f"Starting: ")
#     for monkey in monkeys:
#             print(monkey)
    for round_num in range(total_rounds): # 20 rounds
        for monk in monkeys:
            for item in monk.items:
                # inspect op
                item = monk.inspect_fn(item)
                monk.inspect_count += 1
#                 print(item)
                # post-inspect worry safe
                if not is_part_two:
                    item = item // 3
                else:
                    item = item % test_mod
#                 print(item)
                # test op
                to_monk_num = monk.test_fn(item)
#                 print(to_monk_num)
                # throw
                to_monk = monkeys[to_monk_num]
                to_monk.items.append(item)
#                 print(to_monk)
            # clear after list iteration
            monk.items.clear()
#         print(f"After round {round_num + 1}: ")
#         for monkey in monkeys:
#             print(monkey)
    
    # scoring
    first_hi = 0
    second_hi = 0
    for monkey in monkeys:
        print(monkey)
        if monkey.inspect_count >= first_hi:
            second_hi = first_hi
            first_hi = monkey.inspect_count
        elif monkey.inspect_count > second_hi and monkey.inspect_count < first_hi:
            second_hi = monkey.inspect_count
    
    print(f"{first_hi} * {second_hi}: {first_hi * second_hi}")
    

input_monkeys = []
input_monkeys.append(Monkey(0, [99, 67, 92, 61, 83, 64, 98],
                            lambda old : old * 17,
                            lambda worry : 4 if worry % 3 == 0 else 2,
                            3))
input_monkeys.append(Monkey(1, [78, 74, 88, 89, 50],
                            lambda old : old * 11,
                            lambda worry : 3 if worry % 5 == 0 else 5,
                            5))
input_monkeys.append(Monkey(2, [98, 91],
                            lambda old : old + 4,
                            lambda worry : 6 if worry % 2 == 0 else 4,
                            2))
input_monkeys.append(Monkey(3, [59, 72, 94, 91, 79, 88, 94, 51],
                            lambda old : old * old,
                            lambda worry : 0 if worry % 13 == 0 else 5,
                            13))
input_monkeys.append(Monkey(4, [95, 72, 78],
                            lambda old : old + 7,
                            lambda worry : 7 if worry % 11 == 0 else 6,
                            11))
input_monkeys.append(Monkey(5, [76],
                            lambda old : old + 8,
                            lambda worry : 0 if worry % 17 == 0 else 2,
                            17))
input_monkeys.append(Monkey(6, [69, 60, 53, 89, 71, 88],
                            lambda old : old + 5,
                            lambda worry : 7 if worry % 19 == 0 else 1,
                            19))
input_monkeys.append(Monkey(7, [72, 54, 63, 80],
                            lambda old : old + 3,
                            lambda worry : 1 if worry % 7 == 0 else 3,
                            7))

sample_monkeys = []
sample_monkeys.append(Monkey(0, [79, 98],
                             lambda old : old * 19,
                             lambda worry : 2 if worry % 23 == 0 else 3,
                             23))
sample_monkeys.append(Monkey(1, [54, 65, 75, 74],
                             lambda old : old + 6,
                             lambda worry : 2 if worry % 19 == 0 else 0,
                             19))
sample_monkeys.append(Monkey(2, [79, 60, 97],
                             lambda old : old * old,
                             lambda worry : 1 if worry % 13 == 0 else 3,
                             13))
sample_monkeys.append(Monkey(3, [74],
                             lambda old : old + 3,
                             lambda worry : 0 if worry % 17 == 0 else 1,
                             17))

# monkey_business(sample_monkeys)
# monkey_business(input_monkeys)
# monkey_business(sample_monkeys, True)
monkey_business(input_monkeys, True)