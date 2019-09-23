# Benchmarking Python Heaps

There are several heap implementations on PyPI. This simple benchmark
can help choose between them.

We use the `pyperf` module, which was seen presented at FOSDEM 2017
(called `perf` at that time):

    https://pypi.python.org/pypi/pyperf

# Installation

I tend to use Python's virtual environments for everything:

    $ python3 -m venv venv
    $ . venv/bin/activate

Then install both `pyperf` and the heaps that we are going to
measure:

    $ pip install -r requirements.txt

# Running

After installation just run it:

    $ python3 heapbench.py

The benchmarks take some time.
