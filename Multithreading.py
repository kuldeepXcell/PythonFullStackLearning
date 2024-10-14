# ****************************************************
# Python threading tutorial
# ****************************************************
# thread =  a flow of execution. Like a separate order of instructions.
#                  However each thread takes a turn running to achieve concurrency
#                  GIL = (global interpreter lock),
#                  allows only one thread to hold the control of the Python interpreter at any one time

# cpu bound = program/task spends most of it's time waiting for internal events (CPU intensive)
#             use multiprocessing

# io bound = program/task spends most of it's time waiting for external events (user input, web scraping)
#            use multithreading

import threading
import time

######################################################################################################################

# def print_cube(*lst):
#     for num in lst:
#         print(f"Cube of {num}: {num*num*num}\n")
#
#
# def print_square(*lst):
#     for num in lst:
#         print(f"Square of {num}: {num*num}\n")
#
#
# if __name__ =="__main__":
#     t1 = threading.Thread(target=print_square, args=(list(range(100))))
#     t2 = threading.Thread(target=print_cube, args=(list(range(100))))
#
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()
#     print("Done!")


#####################################################################################################################

def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")


def drink_coffee():
    time.sleep(4)
    print("You drank coffee")


def study():
    time.sleep(5)
    print("You finish studying")

start = time.perf_counter()
x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

x.join()
y.join()
z.join()

finish = time.perf_counter()
print(threading.active_count())
print(threading.enumerate())
print(f"Execution Time : {finish-start :.3f} S")

# ****************************************************
