# Common-sense guide to DSA: Chapter 10 - Exercise 4
# Input an array containing numbers or arrays of numbers (nested to any depth)

def print_nested_arr(arr):
    print(unwrap(arr))

def unwrap(arr):
    sum = 0
    for i in range(len(arr)):
        if type(arr[i]) is int:
            sum += arr[i]
        else:
            sum += unwrap(arr[i])
    return sum

print_nested_arr([1, 2, 3, 4])
print_nested_arr([1,
                    2,
                    3,
                    [4, 5, 6]
                    ])

book_arr = [1,
            2,
            3,
            [4, 5, 6],
            7,
            [8,
                [9, 10, 11,
                    [12, 13, 14]
                ]
            ],
            [15, 16, 17, 18, 19,
                [20, 21, 22,
                    [23, 24, 25,
                        [26, 27, 28, 29]
                    ], 30, 31
                ], 32
            ], 33
            ]
print_nested_arr(book_arr)