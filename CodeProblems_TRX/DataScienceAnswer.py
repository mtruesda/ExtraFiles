import random, matplotlib.pyplot as plt

# operation not important
def rand8():
    return random.randint(1, 8)

# given rand8, write rand11 that it returns a uniform random integer from 1 to 11
# using rand8
def rand11():
    # use rejection sampling
    while True:
        num1 = rand8()
        num2 = rand8()

        value = (num1 - 1) * 8 + num2

        if value <= 55:
            return (value % 11) + 1

def main():
    sampleSize = 10000000
    samples = [rand11() for _ in range(sampleSize)]

    plt.hist(samples, bins=range(1,13), align='left', rwidth=.8, alpha=.75) # rwidth necessary for visibility
    plt.title("Distribution of 10000000 samples from rand11") # trying to see uniform distribution
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.xticks(range(1,12))
    plt.grid(axis='y',alpha=.75) # grid lines

    plt.show()

# So I'm not sure if this actually works--the 2 seems to be above the rest of the
# distribution every time. I did have to look up rejection sampling and how that works though

main()