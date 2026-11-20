"""Source code for Task 3 – Mathematical Functions and Vectorization."""

import numpy as np
import timeit

rng = np.random.default_rng(42)
latency_ms = rng.uniform(5, 250, 1_000_000)

def loop_version():
    result = []
    for value in latency_ms:
        seconds = value / 1000
        result.append(seconds ** 2)
    return result

def vector_version():
    seconds = latency_ms / 1000
    return seconds ** 2

loop_time = timeit.timeit(loop_version, number=1)
vector_time = timeit.timeit(vector_version, number=3) / 3
result = vector_version()

print("First five:", result[:5])
print("Loop time:", loop_time)
print("Vectorized time:", vector_time)
print("Approximate speed-up:", loop_time / vector_time)
