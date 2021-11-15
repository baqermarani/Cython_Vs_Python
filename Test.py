import Main
import time
import time
import functools
import pandas as pd
from functools import partial
import timeit
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot
from random import randint

def timefunc(func):
    @functools.wraps(func)
    def time_closure(*args, **kwargs):
        start = time.process_time()
        result = func(*args, **kwargs)
        time_elapsed = time.process_time() - start
        print(f"Function: {func.__name__} , Time: {time_elapsed}")
        return result

    return time_closure


def plot_time(func, inputs,  repeats, n_tests):
    x, y, yerr = [], [], []
    for i in inputs:
        timer = timeit.Timer(partial(func, i))
        t = timer.repeat(repeat=repeats, number=n_tests)
        x.append(len(i))
        y.append(np.mean(t))
        yerr.append(np.std(t) / np.sqrt(len(t)))
    pyplot.errorbar(x, y, yerr=yerr, fmt='-o', label=func.__name__)

@timefunc
def Plot_times(functions, inputs,repeats=3, n_tests=1, file_name=""):
    for func in functions:
        plot_time(func, inputs, repeats, n_tests)
    pyplot.legend()
    pyplot.xlabel("Numbers of Input")
    pyplot.ylabel("Time [s]")
    if not file_name:
        pyplot.show()
    else:
        pyplot.savefig(file_name)

if __name__ == "__main__":
    data = []
    Number = []
    with open('Numbers' , 'r') as File :
        for line in File:
            line = line.strip()
            data.append(int(line))
    for _ in range(1000):
        value = randint(0 , 5000)
        Number.append(value)
    inputs = [Number , Number*2 , Number*4 , Number*6 , Number*8 , Number*10 , Number*15 , Number*30]
    Plot_times([Main.selection_sort, Main.selection_sort_optimized], inputs, repeats=1)
