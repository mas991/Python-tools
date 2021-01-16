# -*- using:utf-8 -*-
import time

"""
This is a library for measuring the execution time of a process.
"""

if __name__ == '__main__':
    start = time.time()
    # Run the process of measuring time.

    end = time.time()
    process_time = end - start
    print("process_time:{:.9f}".format(process_time) + "[sec]")
