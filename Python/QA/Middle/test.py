import dis
def recursive_sum(n):
    """Function to return the sum of recursive numbers"""
    if n <= 1:
        return n
    else:
        return n + recursive_sum(n-1)

# change this value for a different result
number = 16
if number < 0:
    print("The sum is",recursive_sum(number))
# by using dis module ,the bytecode is loaded into machine code ,and a piece of code that reads each instruction in the bytecode and executes whatever operation is indicated.
dis.dis(recursive_sum)