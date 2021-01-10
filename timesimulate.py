#-*- using:utf-8 -*-
import time

if __name__ == '__main__':
    start = time.time()
    print(pow(10, 10000000) % 3)
    end = time.time()
    process_time = end - start
    print ("process_time:{0}".format(process_time) + "[sec]")
