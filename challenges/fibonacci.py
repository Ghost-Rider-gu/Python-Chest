from typing import Dict

dictionary: Dict[int, int] = { 0:0, 1:1 }

def fibonacci_memoization(num: int) -> int:
    if num not in dictionary:
        dictionary[num] = fibonacci_memoization(num - 2) + fibonacci_memoization(num - 1)
    return dictionary[num]

def fibonacci_recursion(num: int) -> int:
    if num < 2:
        return num
    return fibonacci_recursion(num - 2) + fibonacci_recursion(num - 1)

if __name__ == '__main__':
    print(fibonacci_memoization(50))
    print(fibonacci_recursion(8))
