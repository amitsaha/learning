'''
Implement a disk based external sorting

'''
import tempfile
import heapq

def read_file_incrementally(file):
    numbers = []
    with open(file) as f:
        for number in f:
            numbers.append(float(number))
            if len(numbers) >= 100:
                # sort and store temporarily on disk
                yield numbers
                del numbers[:]
        # in case there are any remaining
        if not f.read() and numbers:
            yield numbers

tmp_files = []
def sort_and_save(numbers):
    f = tempfile.NamedTemporaryFile(delete=False)
    with f:
        for num in sorted(numbers):
            f.write(str(num)+'\n')
    tmp_files.append(f.name)

# incremental sort and write to external files
for numbers in read_file_incrementally('numbers.dat'):
    sort_and_save(numbers)

# merge them back
def read_sorted():
    for temp_file in tmp_files:
        with open(temp_file) as f:
            numbers = [float(line.strip('\n')) for line in f.readlines()]
            yield iter(numbers)

sorted_iterators = []
for iterator in read_sorted():
    sorted_iterators.append(iterator)
# merge and print
for n in heapq.merge(*sorted_iterators):
    print(n)
