"""
# What To Benchmark

In order to benchmark the various heap implementations, we use the
published API in order to check the two fundamental operations:

* Adding something to the heap.
* Removing the smallest (or largest) item from the heap.

We do NOT check the operations:

* Convert an unordered list into a heap.
* Remove an arbitrary item from the heap.
* Change the priority of an item on the heap.

Converting an unordered list into a heap may be interesting, but
not so much for implementing a cache.

On a basic heap, both remove/change require a linear search through
the heap and so are not the main strength of a heap implementation.

# How To Benchmark

Heaps provide O(lgN) insertion and O(lgN) removal of the smallest (or
largest) element. However, they are sometimes inefficient when
processing sorted data. To check for this, we use 3 different data
sets when benchmarking:

1. Items added in ascending order (smallest to largest).
2. Items added in descending order (largest to smallest).
3. Items added in random order.

Many real-world situations provide mostly-sorted data, so these tests
are meaningful. (For example, a priority queue operating on items that
have the same interval will tend to be roughly sorted.)

We will also benchmark on small, medium, and large heap sizes.
Implementations may make decisions that optimize for small heaps, for
example.
"""

import pyperf
import random

import binaryheap
import fibonacci_heap_mod
import heapdict
import heapq
import pyheapq
import libheap
import fibheap
import heapy

try:
    import bhpq
    have_bhpq = True
except SyntaxError:
    have_bhpq = False


#
# Here we define our various insertion tests.
#

def insert_heapdict(items):
    """insert the items into a heapdict object"""
    h = heapdict.heapdict()
    for item in items:
        h[item] = item[0]
    return h


def bench_remove_heapdict(loops, items):
    """insert the items into a heapdict object, then time removing them"""
    range_it = range(loops)
    time_total = 0
    for loops in range_it:
        h = insert_heapdict(items)
        t0 = pyperf.perf_counter()
        while len(h) > 0:
            h.popitem()
        t1 = pyperf.perf_counter()
        time_total += t1 - t0
    return time_total


def insert_heapq(items):
    """insert the items into a list using the heapq module"""
    h = []
    for item in items:
        heapq.heappush(h, item)
    return h


def bench_remove_heapq(loops, items):
    """insert the items into a heap list, then time removing them"""
    range_it = range(loops)
    time_total = 0
    for loops in range_it:
        h = insert_heapq(items)
        t0 = pyperf.perf_counter()
        while h:
            heapq.heappop(h)
        t1 = pyperf.perf_counter()
        time_total += t1 - t0
    return time_total


def insert_pyheapq(items):
    """insert the items into a list using a Python-only version of heapq"""
    h = []
    for item in items:
        pyheapq.heappush(h, item)
    return h


def bench_remove_pyheapq(loops, items):
    """insert the items into a heap list with Python-only version of heapq,
       then time removing them"""
    range_it = range(loops)
    time_total = 0
    for loops in range_it:
        h = insert_pyheapq(items)
        t0 = pyperf.perf_counter()
        while h:
            pyheapq.heappop(h)
        t1 = pyperf.perf_counter()
        time_total += t1 - t0
    return time_total


def insert_binaryheap(items):
    """insert the items into a binaryheap object"""
    h = binaryheap.new_min_heap()
    for item in items:
        h.add(item)
    return h


def bench_remove_binaryheap(loops, items):
    """insert the items into a binaryheap, then time removing them"""
    range_it = range(loops)
    time_total = 0
    for loops in range_it:
        h = insert_binaryheap(items)
        t0 = pyperf.perf_counter()
        while h:
            h.extract_one()
        t1 = pyperf.perf_counter()
        time_total += t1 - t0
    return time_total


def insert_fibonacci_heap_mod(items):
    """insert the items into a Fibonacci heap object"""
    h = fibonacci_heap_mod.Fibonacci_heap()
    for item in items:
        h.enqueue(item, item[0])
    return h


def bench_remove_fibonacci_heap_mod(loops, items):
    """insert the items into a Fibonacci heap, then time removing them"""
    range_it = range(loops)
    time_total = 0
    for loops in range_it:
        h = insert_fibonacci_heap_mod(items)
        t0 = pyperf.perf_counter()
        while h:
            h.dequeue_min()
        t1 = pyperf.perf_counter()
        time_total += t1 - t0
    return time_total


def insert_libheap(items):
    """insert the items into a libheap object"""
    h = libheap.Heap()
    for item in items:
        h.insert(item)
    return h


def bench_remove_libheap(loops, items):
    """insert the items into a libheap object, then time removing them"""
    range_it = range(loops)
    time_total = 0
    for loops in range_it:
        h = insert_libheap(items)
        t0 = pyperf.perf_counter()
        while not h.empty():
            h.pop()
        t1 = pyperf.perf_counter()
        time_total += t1 - t0
    return time_total


def insert_fibheap(items):
    """insert the items into a fibheap object"""
    h = fibheap.makefheap()
    for item in items:
        fibheap.fheappush(h, item)
    return h


def bench_remove_fibheap(loops, items):
    """insert the items into a fibheap object, then time removing them"""
    range_it = range(loops)
    time_total = 0
    for loops in range_it:
        h = insert_fibheap(items)
        t0 = pyperf.perf_counter()
        while h.num_nodes > 0:
            fibheap.fheappop(h)
        t1 = pyperf.perf_counter()
        time_total += t1 - t0
    return time_total

def insert_bhpq(items):
    """insert the items into a bhpq"""
    h = bhpq.BinaryHeapPriorityQueue(prefer=max)
    for item in items:
        h.add(item)
    return h


def bench_remove_bhpq(loops, items):
    """insert the items into a bhpq, then time removing them"""
    range_it = range(loops)
    time_total = 0
    for loops in range_it:
        h = insert_bhpq(items)
        t0 = pyperf.perf_counter()
        while h.size() > 0:
            h.pop()
        t1 = pyperf.perf_counter()
        time_total += t1 - t0
    return time_total


def insert_heapy(items):
    """insert the items into a heapy object"""
    h = heapy.pqueue()
    for item in items:
        h.push((item[0], item))
    return h


def bench_remove_heapy(loops, items):
    """insert the items into a heapy object, then time removing them"""
    range_it = range(loops)
    time_total = 0
    for loops in range_it:
        h = insert_heapy(items)
        t0 = pyperf.perf_counter()
        while len(h) > 0:
            h.pop()
        t1 = pyperf.perf_counter()
        time_total += t1 - t0
    return time_total

#
# Create a table of tests to run.
#

TESTS = [
    { "name_insert": 'heapdict[]',
      "insert": insert_heapdict,
      "name_remove": 'heapdict.popitem()',
      "remove": bench_remove_heapdict, },
    { "name_insert": 'heapq.heappush()',
      "insert": insert_heapq,
      "name_remove": 'heapq.heappop()',
      "remove": bench_remove_heapq, },
    { "name_insert": 'pyheapq.heappush()',
      "insert": insert_pyheapq,
      "name_remove": 'pyheapq.heappop()',
      "remove": bench_remove_pyheapq, },
    { "name_insert": 'binaryheap.add()',
      "insert": insert_binaryheap,
      "name_remove": 'binaryheap.extract_one()',
      "remove": bench_remove_binaryheap, },
    { "name_insert": 'libheap.insert()',
      "insert": insert_libheap,
      "name_remove": 'libheap.pop()',
      "remove": bench_remove_libheap, },
    { "name_insert": 'fibonacci_heap_mod.enqueue()',
      "insert": insert_fibonacci_heap_mod,
      "name_remove": 'fibonacci_heap_mod.dequeue_min()',
      "remove": bench_remove_fibonacci_heap_mod, },
    { "name_insert": 'fibheap.fheappush()',
      "insert": insert_fibheap,
      "name_remove": 'fibheap.fheappop()',
      "remove": bench_remove_fibheap, },
    { "name_insert": 'heapy.push()',
      "insert": insert_heapy,
      "name_remove": 'heapy.pop()',
      "remove": bench_remove_heapy, },
]

if have_bhpq:
    TESTS.append(
        { "name_insert": 'bhpq.add()',
          "insert": insert_bhpq,
          "name_remove": 'bhpq.pop()',
          "remove": bench_remove_bhpq, },
    )

#
# Now do the actual benchmarking, using the perf module.
#

runner = pyperf.Runner()

# Build a small array in order, and insert each entry.
items = [(n,) for n in range(1000)]
for test in TESTS:
    runner.bench_func(f'{test["name_insert"]} ascending, N=1K',
                      test["insert"], items)

# Build a small array in reverse order, and insert each entry.
items = [(n,) for n in range(1000, 0, -1)]
for test in TESTS:
    runner.bench_func(f'{test["name_insert"]} descending, N=1K',
                      test["insert"], items)

# Randomize the small array, and insert each entry.
random.shuffle(items)
for test in TESTS:
    runner.bench_func(f'{test["name_insert"]} random order, N=1K',
                      test["insert"], items)

# Build a big array in order, and insert each entry.
items = [(n,) for n in range(1000000)]
for test in TESTS:
    runner.bench_func(f'{test["name_insert"]} ascending order, N=1M',
                      test["insert"], items)

# Build a big array in reverse order, and insert each entry.
items = [(n,) for n in range(1000000, 0, -1)]
for test in TESTS:
    runner.bench_func(f'{test["name_insert"]} descending order, N=1M',
                      test["insert"], items)

# Randomize the big array, and insert each entry.
random.shuffle(items)
for test in TESTS:
    runner.bench_func(f'{test["name_insert"]} random order, N=1M',
                      test["insert"], items)

# Build a small array, see how long it takes to remove this.
items = [(n,) for n in range(1000)]
for test in TESTS:
    runner.bench_time_func(f'{test["name_remove"]}, N=1K',
                           test["remove"], items, inner_loops=10)

# Build a big array, see how long it takes to remove this.
items = [(n,) for n in range(1000000)]
for test in TESTS:
    runner.bench_time_func(f'{test["name_remove"]}, N=1M',
                           test["remove"], items, inner_loops=10)
