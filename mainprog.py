

class rediqueue:
    def __init__(self):
        self.array = []

    def enqueue(self, value):
        self.array.append(value)

    def deqeueue(self):
        return self.array.pop(0)

        
# obj1 = rediqueue()
# obj1.enqueue('p1')
# obj1.enqueue('p2')
# obj1.enqueue('p3')

# print(obj1.deqeueue())
# print(obj1.array)


# self.job_manager.enqueue(['P2',3,0])
# self.job_manager.enqueue(['P3',3,0])
#  ['P2',3,0] , ['P3',3,0]

# def Sort_the_queue(list2sort: list):
#     list2sort.sort(key=lambda x: x[2])
#     return list2sort

# print(Sort_the_queue)
from sorting_algos import Sorting_Process


class CPU:
    functions = Sorting_Process() #fetching the sorting functions which will sort the function according
    # to scheduling algorithms

    def __init__(self):
        self.job_manager = rediqueue()  # redi queue manager

        self.CPU = "CPU"
        self.processes_executed = []
        self.arrivaltimes = []
        self.bursttimes = []
        self.completiontime = []
        self.turnaroundtime = []
        self.w8ingtime = []

        #nested list try karte hain
        self.nestlst = []
        """Completion time is sum of burst times of all prev processes
        """

    def execute_process(self):
        """Implementing FCFS, SJF, SJF Preemptive, Round Robin and Priority Scheduling algorithms
        printing process will be same for every algorithms, in the start we will first sort out the algorithms and
        then will send them to printing.
        """
        #_______ process name with it burst time, arrival time_________
        make_arrival_0 = 1
        # self.job_manager.enqueue(["P0", 6, 0 * make_arrival_0])
        self.job_manager.enqueue(["P1", 8, 0 * make_arrival_0])
        self.job_manager.enqueue(["P2", 4, 1 * make_arrival_0])
        self.job_manager.enqueue(["P3", 9, 2 * make_arrival_0])
        self.job_manager.enqueue(['P4', 5, 3 * make_arrival_0])
        # self.job_manager.enqueue(['P5', 8, 9 * make_arrival_0])
        # self.job_manager.enqueue(['P6',1,0])


        #______________ sort the queue according to the arrival times for FCFS
        # self.job_manager.array = self.functions.sort_FCFS(self.job_manager.array)

        #______________ sort the queue according to the burst times for SJF non preemptive
        self.job_manager.array = self.functions.sort_SJF_non_pe(self.job_manager.array)


        # print(self.job_manager.array)

        for i in range(len(self.job_manager.array)):

            process = (
                self.job_manager.deqeueue()
            )  # ['P1',24, 0] process and burst time and arrival time

            self.processes_executed.append(process[0]) # process[0] is string of process: e.g 'P1'
            self.arrivaltimes.append(process[2])

            bursttime_inst = process[1]
            self.bursttimes.append(bursttime_inst)

            completion_var = sum(self.bursttimes)
            self.completiontime.append(completion_var)

            turnaround_inst = ( completion_var - process[2] ) # process[2] is arrival time
            self.turnaroundtime.append(turnaround_inst)

            w8ing_inst = turnaround_inst - bursttime_inst
            self.w8ingtime.append(w8ing_inst)

            self.nestlst.append(
                [process[0], bursttime_inst, completion_var, process[2], turnaround_inst, w8ing_inst]
            )


        self.nestlst = self.functions.sort_the_processes(self.nestlst)




    def printdata(self):
        print("Processes times:", self.processes_executed)
        print("Arrivals times:", self.arrivaltimes)
        print("Bursts times:", self.bursttimes)
        print("Completion times:", self.completiontime)
        print("Turnaround times:", self.turnaroundtime)
        print("Waiting times:", self.w8ingtime)


        print("\nNEsted List:",self.nestlst)

    def average_waiting_time(self):
        return f"Average Waiting Time:{sum(self.w8ingtime)/len(self.w8ingtime)} units"

if __name__ == "__main__":
    obj = CPU()
    obj.execute_process()

    obj.printdata()
    print(obj.average_waiting_time())
