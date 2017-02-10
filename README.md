# Benchmarking Python Heaps

There are several heap implementations on PyPI. This simple benchmark
can help choose between them.

We use the `perf` module, which was seen presented at FOSDEM 2017.

    https://pypi.python.org/pypi/perf

# Installation

I tend to use Python's virtual environments for everything:

    $ python3 -m venv venv
    $ . venv/bin/activate

Next install the `perf` module:

    $ python3 -m pip install perf

We also need a to install the various heaps that we are going to
measure:

    $ python3 -m pip install binaryheap
    $ python3 -m pip install fibonacci-heap-mod
    $ python3 -m pip install heapdict
    $ python3 -m pip install heapqueue

# Running

After installation just run it:

    $ python3 heapbench.py

The benchmarks take some time.
