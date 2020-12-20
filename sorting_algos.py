from mainprog import rediqueue

class Sorting_Process:
    """This class contains the functions whic will sort the processes
    according to the CPU scheduling algo's: FCFS, SJF, etc.
    """
    def __init__(self):
        self.psa = None
        self.arrdupliforsjfpreem = None

    def sort_the_processes(self,array):
        """This will sort the processes in alphabetical order, applies to all algorithms
        """
        arr = array
        arr.sort(key=lambda x : x[0])
        return arr

    def sort_FCFS(self, array):
        """Sorts according to the FCFS algorithm

        Returns:
            [list]: [A nested list of which contains processes, burst times and arrival time]
            will sort the ARRIVAL times
        """
        arr = array
        arr.sort(key=lambda x: x[2]) # x[2] here we are selecting the third index which is arrival time
        return arr

    def sort_SJF_non_pe(self, process_data):
        print("SJF NON Running")

        """Sorts according to the SJF non-preemptive algorithm
            will sort the BURST times

        sjf mein aesi denge
        [['P1', 8, 6], ['P2', 4, 1], ['P3', 9, 2], ['P4', 5, 3]]
        ani aese chahye:
        [['P1', 8, 0], ['P2', 4, 1], ['P4', 5, 3], ['P3', 9, 4]]

        [['P1', 8, 0], ['P2', 4, 1], ['P4', 5, 0], ['P3', 9, 9]]
        Returns:
            [list]: [A nested list of which contains processes, burst times and arrival time]
        """
        start_time = []
        exit_time = []
        s_time = 0
        process_data.sort(key=lambda x: x[1])
        '''
        Sort processes according to the Arrival Time
        '''
        for i in range(len(process_data)):
            ready_queue = []
            temp = []
            normal_queue = []

            for j in range(len(process_data)):
                if (process_data[j][1] <= s_time) and (process_data[j][3] == 0):
                    temp.extend([process_data[j][0], process_data[j][1], process_data[j][2]])
                    ready_queue.append(temp)
                    temp = []
                elif process_data[j][3] == 0:
                    temp.extend([process_data[j][0], process_data[j][1], process_data[j][2]])
                    normal_queue.append(temp)
                    temp = []

            if len(ready_queue) != 0:
                ready_queue.sort(key=lambda x: x[2])
                '''
                Sort the processes according to the Burst Time
                '''
                start_time.append(s_time)
                s_time = s_time + ready_queue[0][2]
                e_time = s_time
                exit_time.append(e_time)
                for k in range(len(process_data)):
                    if process_data[k][0] == ready_queue[0][0]:
                        break
                process_data[k][3] = 1
                process_data[k].append(e_time)

            elif len(ready_queue) == 0:
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                start_time.append(s_time)
                s_time = s_time + normal_queue[0][2]
                e_time = s_time
                exit_time.append(e_time)
                for k in range(len(process_data)):
                    if process_data[k][0] == normal_queue[0][0]:
                        break
                process_data[k][3] = 1
                process_data[k].append(e_time)

        print(process_data)

    def sort_SJF_pe(self, array):
        print("SJF Running")

        """Sorts according to the SJF non-preemptive algorithm
            will sort the BURST times

        sjf mein aesi denge
        [['P1', 8, 0], ['P2', 4, 1], ['P3', 9, 2], ['P4', 5, 3]]

        ['P4', 5 (bt), 3 (at)]
        Returns:
            [list]: [A nested list of which contains processes, burst times and arrival time]
        """
        import copy
        arraydup11 = copy.deepcopy(array)
        #print( len(arraydup11), arraydup11)
        time = 0
        processes_series = []
        f_arr = [] # final array
        
        while True:
            
            readyque = []
            
            for i in range(len(array)):
                # jitne bhi process arrived hogye hain woh readyque mein daldo
                if array[i][2] <= time:
                    readyque.append(array[i]) # .... + burst_time
            
            if len(readyque) == 0:
                time += 1
                continue

            readyque.sort(key=lambda x: x[1])
            
            readyque[0][1] -= 1 # readyque ke first process ke bt ko reduce kardia
            time += 1
            processes_series.append(readyque[0][0])
            
            # agr process executed ho tu usko nikaldo array se aur kisi or mein daldo

            if readyque[0][1] == 0:
                f_arr.append( [readyque[0][0] , readyque[0][2] , time ] )
                array.remove(readyque[0])
            
            if len(f_arr) == 4:
                break
        
        f_arr.sort(key=lambda x: x[0])
        #print(len(f_arr) , len(arraydup11), arraydup11)
        for i in range(len(f_arr)):
            f_arr[i].append(arraydup11[i][1])

        print("turn around time",self.cal_turnaround_time(f_arr))
        print("waiting time",self.cal_w8ing_time(f_arr))
        return f_arr

    def cal_turnaround_time(self, process_list:list): # for SJF-preemptive
        # [['P1', 0, 17, 8], ['P2', 1, 5, 4], ['P3', 2, 26, 9], ['P4', 3, 10, 5]]
        turn_around_time = []
        total_ta_time = 0
        for i in range(len(process_list)):
            
            turn_around_time_inst = process_list[i][2] - process_list[i][1] # completion - arrival
            total_ta_time += turn_around_time_inst
            turn_around_time.append(turn_around_time_inst)

        return turn_around_time

    def cal_w8ing_time(self, process_list:list):  # for SJF-preemptive
        # [['P1', 0, 17, 8], ['P2', 1, 5, 4], ['P3', 2, 26, 9], ['P4', 3, 10, 5]]
        w8ing_time = []
        total_wa_time = 0
        for i in range(len(process_list)):
            
            w8ing_time_inst = process_list[i][2] - process_list[i][1] - process_list[i][3] # completion - arrival
            total_wa_time += w8ing_time_inst
            w8ing_time.append(w8ing_time_inst)

        return w8ing_time

    def priority_nonpe(self,process_list):
        return process_list.sort(key=lambda x: x[2])


if __name__ == "__main__":
    # arr = [['P1', 0, 4, 0], ['P2', 1, 2, 0], ['P3', 2, 6, 0], ['P4', 3, 2, 0]]
    # arr = [[1, 0, 4, 0], [2, 1, 2, 0], [3, 2, 6, 0], [4, 3, 2, 0]]
    for_priority_algo = [['P1', 10, 3], ['P2', 1, 1], ['P3', 2, 4], ['P4', 1, 5], ['P5', 5 , 2]]
    test1 = Sorting_Process()
    print(test1.sort_SJF_non_pe(for_priority_algo))

