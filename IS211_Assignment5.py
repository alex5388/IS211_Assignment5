import csv
import urllib
import argparse


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()


class Server:

    def __init__(self, host_name=None):
        self.host_name = host_name
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
        self.time_remaining = new_task.get_req()

class Request:

    def __init__(self, time, seconds):
        self.timestamp = time
        self.seconds = seconds

    def get_req(self):
        return self.seconds

    def wait_time(self, current_time):
        return current_time - self.timestamp

def simulateOneServer(filename):
    taskQ = Queue()
    wait_time = []
    server_req = Server()

    for i in range(filename):

        if server_req.tick():
            taskQ.enqueue()

        if (not server_req.busy()) and (not taskQ.is_empty()):
            next_task = taskQ.dequeue()
            wait_time.append(next_task.wait_time(i))







def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file')
    parser.add_argument('--servers', default=1)
    args = parser.parse_args()

    if args.file:



if __name__=="__main__":
    main()