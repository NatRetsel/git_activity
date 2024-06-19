def single_fib(n:int) -> int:
    if (n==0): return 0
    if (n==1): return 1
    return single_fib(n-1) + single_fib(n-2)

def print_fib_seq(n:int) -> None:
    prev1: int = 1
    prev2: int = 0 
    for i in range(0, n+1):
        if (i == 0):
            print(i, end=" ")
        elif (i==1):
            print(i, end=" ")
        else:
            fib = prev1 + prev2
            print(fib, end=" ")
            prev1, prev2 = fib, prev1
    print("\n")
    

def print_fib_seq_list(n:int) -> None:
    res = []
    prev1: int = 1
    prev2: int = 0 
    for i in range(0, n+1):
        if (i == 0):
            res.append(i)
        elif (i==1):
            res.append(i)
        else:
            fib = prev1 + prev2
            res.append(fib)
            prev1, prev2 = fib, prev1
    print(res)

if __name__ == "__main__":
    print_fib_seq(2)
    print_fib_seq(5)
    print_fib_seq(7)
    print(single_fib(7))
    print_fib_seq_list(7)
