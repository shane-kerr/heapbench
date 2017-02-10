"""
# What To Benchmark

In order to benchmark the various heap implementations, we use the
published API in order to check the two fundamental operations:

* Adding something to the heap.
* Removing the smallest (or largest) item from the heap.

Additionally, we check the following operation:

* Convert an unordered list into a heap.

We do NOT check the operations:

* Remove an arbitrary item from the heap.
* Change the priority of an item on the heap.

On a basic heap, both of these require a linear search through the
heap and so are not the main strength of a heap implementation.

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

import perf
import random

import binaryheap
import fibonacci_heap_mod
import heapdict
import heapq
import heapqueue
import pyheapq


#
# Here we define our various insertion tests.
#

def insert_heapdict(items):
    """insert the items into a heapdict object"""
    h = heapdict.heapdict()
    for item in items:
        h[item] = item[0]


def insert_heapq(items):
    """insert the items into a list using the heapq module"""
    h = []
    for item in items:
        heapq.heappush(h, item)


def insert_binaryheap(items):
    """insert the items into a binaryheap object"""
    h = binaryheap.new_min_heap()
    for item in items:
        h.add(item)


def insert_heapqueue(items):
    """insert the items into a heapqueue object"""
    def list_cmp(a, b):
        if a < b:
            return -1
        if a > b:
            return 1
        return 0
    kwargs = {'cmp': list_cmp}
    h = heapqueue.HeapQueue(**kwargs)
    for item in items:
        h.push(item)


def insert_pyheapq(items):
    """insert the items into a list using a Python-only version of heapq"""
    h = []
    for item in items:
        pyheapq.heappush(h, item)


def insert_fibheap(items):
    """insert the items into a Fibonacci heap object"""
    h = fibonacci_heap_mod.Fibonacci_heap()
    for item in items:
        h.enqueue(item, item[0])

#
# Now do the actual benchmarking, using the perf module.
#

runner = perf.Runner()

# Build a small array in order, and insert each entry.
items = [(n,) for n in range(1000)]
runner.bench_func('heapdict[] ascending, N=1K',
                  insert_heapdict, items)
runner.bench_func('heapq.heappush() ascending, N=1K',
                  insert_heapq, items)
runner.bench_func('binaryheap.add() ascending, N=1K',
                  insert_binaryheap, items)
runner.bench_func('heapqueue.push() ascending, N=1K',
                  insert_heapqueue, items)
runner.bench_func('pyheapq.heappush() ascending, N=1K',
                  insert_pyheapq, items)
runner.bench_func('fibonacci_heap_mod.enqueue() ascending, N=1K',
                  insert_fibheap, items)

# Build a small array in reverse order, and insert each entry.
items = [(n,) for n in range(1000, 0, -1)]
runner.bench_func('heapdict[] descending, N=1K',
                  insert_heapdict, items)
runner.bench_func('heapq.heappush() descending, N=1K',
                  insert_heapq, items)
runner.bench_func('binaryheap.add() descending, N=1K',
                  insert_binaryheap, items)
runner.bench_func('heapqueue.push() descending, N=1K',
                  insert_heapqueue, items)
runner.bench_func('pyheapq.heappush() descending, N=1K',
                  insert_pyheapq, items)
runner.bench_func('fibonacci_heap_mod.enqueue() descending, N=1K',
                  insert_fibheap, items)

# Randomize the small array, and insert each entry.
random.shuffle(items)
runner.bench_func('heapdict[] random order, N=1K',
                  insert_heapdict, items)
runner.bench_func('heapq.heappush() random order, N=1K',
                  insert_heapq, items)
runner.bench_func('binaryheap.add() random order, N=1K',
                  insert_binaryheap, items)
runner.bench_func('heapqueue.push() random order, N=1K',
                  insert_heapqueue, items)
runner.bench_func('pyheapq.heappush() random order, N=1K',
                  insert_pyheapq, items)
runner.bench_func('fibonacci_heap_mod.enqueue() random order, N=1K',
                  insert_fibheap, items)

# Build a big array in order, and insert each entry.
items = [(n,) for n in range(1000000)]
runner.bench_func('heapdict[] ascending, N=1M',
                  insert_heapdict, items)
runner.bench_func('heapq.heappush() ascending, N=1M',
                  insert_heapq, items)
runner.bench_func('binaryheap.add() ascending, N=1M',
                  insert_binaryheap, items)
runner.bench_func('heapqueue.push() ascending, N=1M',
                  insert_heapqueue, items)
runner.bench_func('pyheapq.heappush() ascending, N=1M',
                  insert_pyheapq, items)
runner.bench_func('fibonacci_heap_mod.enqueue() ascending, N=1M',
                  insert_fibheap, items)

# Build a big array in reverse order, and insert each entry.
items = [(n,) for n in range(1000000, 0, -1)]
runner.bench_func('heapdict[] descending, N=1M',
                  insert_heapdict, items)
runner.bench_func('heapq.heappush() descending, N=1M',
                  insert_heapq, items)
runner.bench_func('binaryheap.add() descending, N=1M',
                  insert_binaryheap, items)
runner.bench_func('heapqueue.push() descending, N=1M',
                  insert_heapqueue, items)
runner.bench_func('pyheapq.heappush() descending, N=1M',
                  insert_pyheapq, items)
runner.bench_func('fibonacci_heap_mod.enqueue() descending, N=1M',
                  insert_fibheap, items)

# Randomize the big array, and insert each entry.
random.shuffle(items)
runner.bench_func('heapdict[] random order, N=1M',
                  insert_heapdict, items)
runner.bench_func('heapq.heappush() random order, N=1M',
                  insert_heapq, items)
runner.bench_func('binaryheap.add() random order, N=1M',
                  insert_binaryheap, items)
runner.bench_func('heapqueue.push() random order, N=1M',
                  insert_heapqueue, items)
runner.bench_func('pyheapq.heappush() random order, N=1M',
                  insert_pyheapq, items)
runner.bench_func('fibonacci_heap_mod.enqueue() random order, N=1M',
                  insert_fibheap, items)
