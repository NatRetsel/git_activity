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

# added comment "ngeeann" as a code change - e5
# What a cool Fib Sequence! - Mickey

#npbranch2 hahha

def add(num1, num2):
  return num1 + num2

def subtract(num1, num2):
  return num1 - num2

def multiply(num1, num2):
  return num1 * num2

def divide(num1, num2):
  try:
    return (num1 / num2)
  except ZeroDivisionError:
     return "Cannot divide by 0"

def get_num(text):
  try:
     return int(input(f"\n{text}"))
  except ValueError:
     return "Please enter a valid integer"

def get_selection():
  selection = int(input("\nSelect your calculator operations: \
                      \n1.Addition\
                      \n2.Subtraction\
                      \n3.Multiplication\
                      \n4.Division\n\n"))
  if selection not in (1, 2, 3, 4):
    raise ValueError
  return selection