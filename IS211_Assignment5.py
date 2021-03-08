import csv
import urllib
import argparse
import os

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Server:

    def __init__(self, ppm):
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task != None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate

class Request:

    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.timestamp

def simulateOneServer(filename):
    wait_time = []
    request_dict = {}

    for request in filename:
        n_time = int(request[0])
        Queue().enqueue(request)

        if n_time in request_dict:
            request_dict[n_time].append(request)
        else:
            request_dict[n_time] = [request]

    for time_in_second in request_dict:
        for req in request_dict[time_in_second]:
            Request(req)
            Queue().dequeue()

        if (not Server().busy()) and (not Queue().isEmpty()):
            nextreq = Request(Queue().dequeue())
            wait_time.append(nextreq.wait_Time(nextreq))
            #breaks after this line
            Server().startNext(nextreq)

        Server().tick()





def main():
    q = Queue()
    q.enqueue('cat')
    print(q.size())
    q.enqueue('dogs')
    print(q.size())
    print(q.items)
    q.dequeue()
    print('dequeue removes the first item entered in the stack')
    print(q.items)


if __name__=="__main__":
    main()