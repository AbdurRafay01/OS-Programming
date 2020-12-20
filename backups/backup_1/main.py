from sorting_algos import Sorting_Process


class rediqueue:
    def __init__(self):
        self.array = []

    def enqueue(self, value):
        self.array.append(value)

    def deqeueue(self):
        return self.array.pop(0)

# self.job_manager.enqueue(['P2',3,0])
# self.job_manager.enqueue(['P3',3,0])
#  ['P2',3,0] , ['P3',3,0]

# def Sort_the_queue(list2sort: list):
#     list2sort.sort(key=lambda x: x[2])
#     return list2sort

# print(Sort_the_queue)


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
        make_arrival_0 = 0
        # self.job_manager.enqueue(["P0", 6, 0 * make_arrival_0])  
        self.job_manager.enqueue(["P1", 2, 2 * make_arrival_0])
        self.job_manager.enqueue(["P2", 1, 5 * make_arrival_0])
        self.job_manager.enqueue(["P3", 8, 1 * make_arrival_0])
        self.job_manager.enqueue(['P4', 4, 0 * make_arrival_0])
        self.job_manager.enqueue(['P5', 5, 4 * make_arrival_0])
        # self.job_manager.enqueue(['P6',1,0])


        # sort the queue according to the arrival times for FCFS
        # self.functions.sort_FCFS(self.job_manager.array)
        # sort the queue according to the burst times for SJF non preemptive
        self.functions.sort_FCFS(self.job_manager.array)
        print(self.job_manager.array)

        for i in range(len(self.job_manager.array)):

            process = (
                self.job_manager.deqeueue()
            )  # ['P1',24, 0] process and burst time and arrival time
            bursttime_inst = process[1]

            self.processes_executed.append(process[0])
            self.bursttimes.append(bursttime_inst)
            
            completion_var = sum(self.bursttimes)
            turnaround_inst = ( completion_var - process[2] )
            w8ing_inst = turnaround_inst - bursttime_inst

            self.completiontime.append(completion_var)
            self.arrivaltimes.append(process[2])
            self.turnaroundtime.append(turnaround_inst)
            self.w8ingtime.append(w8ing_inst)


            self.nestlst.append(
                [process[0], bursttime_inst, completion_var, process[2], turnaround_inst, w8ing_inst]
            )




    def printdata(self):
        print("Processes times:", self.processes_executed)
        print("Arrivals times:", self.arrivaltimes)
        print("Bursts times:", self.bursttimes)
        print("Completion times:", self.completiontime)
        print("Turnaround times:", self.turnaroundtime)
        print("Waiting times:", self.w8ingtime)

        print("\nNEsted List:",self.nestlst)

    def average_waiting_time(self):
        return f"Average Waiting Time:{sum(self.w8ingtime)//len(self.w8ingtime)} units"


obj = CPU()
obj.execute_process()

obj.printdata()
print(obj.average_waiting_time())
