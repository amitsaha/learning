import random
import matplotlib.pyplot as plt

# return a random index based on the percentages
def get_index(r, percentages):
    c_percentage = 0
    sum_percentages = []
    for p in percentages:
        c_percentage += p
        sum_percentages.append(c_percentage)
    for item, sp in enumerate(sum_percentages):
        if r <= sp:
            return item
    # if we are here, it means we are somewhere between
    # sum(percentages) and 1.0, so, we assume it falls into the
    # last category
    return len(percentages)-1

indices = []
percentages = [1/6] * 6
for i in range(10000):
    r = random.random()
    idx = get_index(r, percentages)
    indices.append(idx)

# plot a histogram to make the random choices apparent
plt.hist(indices, bins=len(percentages))
plt.show()
