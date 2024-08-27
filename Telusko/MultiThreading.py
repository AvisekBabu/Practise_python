from threading import *
from time import sleep

#  Need to inherit Thread to run our threads in different different cores
#  Main thread will be bypassed and two more threads will start

class test1(Thread):
    # Need to use method run, which is a subclass of Thread
    def run(self):
        for i in range(10):
            print("Hello")
            sleep(1)


class test2(Thread):
    def run(self):
        for j in range(10):
            print("Hi")
            sleep(1)

t1 = test1()
t2 = test2()

# t1.run()
# t2.run()


t1.start()
sleep(0.2)
t2.start()

"""
#  Here Main thread will transfer the activity in other two threads
#  But same time when task transfer done, main thread will print "Bye"
#  Which can make collision inside other two thread
#  "Bye" is part of main thread, t1.start() and t2.start() each part of individual thread
#  Total 3 threads at same time
"""
# print("Bye")

#  We can introduce object.join() through will main thread will understand that other two thread need to join
#  first, then only print("Bye") will be print.

t1.join()
t2.join()
print("Bye")