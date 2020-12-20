
#### FCFS first come first serve

class rediqueue():
    
    def __init__(self):
        self.array = []
        
        
    def enqueue(self, value):
        self.array.append(value)
    
    def deqeueue(self):
        return self.array.pop(0)
        
        
# job_manager = rediqueue()
# job_manager.enqueue(['P1',24]) # process name with it burst time
# job_manager.enqueue(['P2',3])
# job_manager.enqueue(['P3',3])
# print(job_manager.deqeueue())



class CPU():
    
    def __init__(self):
        self.job_manager = rediqueue() # redi queue manager
        
        self.CPU = 'CPU'
        self.processes_executed = []
        self.arrivaltimes = []
        self.arrivaltimes_flag = 0
        
        self.bursttimes = []
        self.completiontime = []
        self.turnaroundtime = []
        self.w8ingtime = []
        
        
        """Completion time is sum of burst times of all prev processes
        """
        
        
        
    def execute_process(self):
        
        self.job_manager.enqueue(['P1',24]) # process name with it burst time
        self.job_manager.enqueue(['P2',3])
        self.job_manager.enqueue(['P3',3])
        self.job_manager.enqueue(['P4',4])
        self.job_manager.enqueue(['P5',23])
        self.job_manager.enqueue(['P6',1])
        
        self.arrivaltimes = [0 for i in range(len(self.job_manager.array))]
        
        for i in range(len(self.job_manager.array)):
                
            self.process = self.job_manager.deqeueue() # ['P1',24] process and burst time
            
            self.processes_executed.append(self.process[0])
            self.bursttime_inst = self.process[1]
            self.bursttimes.append(self.bursttime_inst)
            
            self.completion_var = sum(self.bursttimes)
            self.completiontime.append(self.completion_var)
            # Turn Around Time = Completion Time - Arrival Time   
            # self.turnaround_inst = self.completion_var - self.arrivaltimes[self.arrivaltimes_flag]
            self.turnaround_inst = self.completion_var - 0
            
            # self.arrivaltimes_flag += 1
            
            self.turnaroundtime.append(self.turnaround_inst)
            
            self.w8ingtime.append(self.turnaround_inst-self.bursttime_inst)
            
        
        
    def printdata(self):
        print('Processes times:',self.processes_executed)
        print('Arrivals times:',self.arrivaltimes)
        print('Bursts times:',self.bursttimes)
        print('Completion times:',self.completiontime)
        print('Turnaround times:',self.turnaroundtime)
        print('Waiting times:',self.w8ingtime)
        
    def average_waiting_time(self):
        return f"Average Waiting Time:{sum(self.w8ingtime)//len(self.w8ingtime)} units"

obj = CPU()
obj.execute_process()

obj.printdata()
print(obj.average_waiting_time())