import matplotlib.pyplot as plt

def graphSnowfall(t):
    """Graphs the snowfall data from a file t."""
    with open(t, 'r') as file:
        snowfall = [int(line.strip()) for line in file.readlines()]

    # Define ranges and count occurrences
    ranges = {f"{i}-{i+9}cms": 0 for i in range(0, max(snowfall)+1, 10)}
    for amount in snowfall:
        for range_start in range(0, max(snowfall)+1, 10):
            if range_start <= amount < range_start + 10:
                ranges[f"{range_start}-{range_start+9}cms"] += 1
                break

    # Plotting
    plt.bar(ranges.keys(), ranges.values())
    plt.xlabel('Snowfall ranges')
    plt.ylabel('Occurrences')
    plt.title('Snowfall Distribution')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Usage: graphSnowfall('path_to_your_file.txt')

