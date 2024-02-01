def stats_decorator(func):
    def wrapper(*args, **kwargs):
        numbers = func(*args, **kwargs)
        print(f"Numbers: {numbers}")
        print(f"Count: {len(numbers)}")
        print(f"Average: {sum(numbers) / len(numbers)}")
        print(f"Max: {max(numbers)}")
    return wrapper

@stats_decorator
def printStats(t):
    with open(t, 'r') as file:
        for line in file:
            numbers = [int(num) for num in line.split()]
            yield numbers

for numbers in printStats('your_file.txt'):
    pass  # Numbers are processed in the decorator

