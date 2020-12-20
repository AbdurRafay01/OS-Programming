
class Sorting_Process:
    """This class contains the functions whic will sort the processes
    according to the CPU scheduling algo's: FCFS, SJF, etc.
    """
    def __init__(self):
        self.psa = None

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

    def sort_SJF_non_pe(self, array):
        """Sorts according to the SJF non-preemptive algorithm
            will sort the BURST times
        Returns:
            [list]: [A nested list of which contains processes, burst times and arrival time]
        """
        arr = array
        arr.sort(key=lambda x: x[1]) # x[1] here we are selecting the third index which is burst time
        return arr


if __name__=="main":
    arr = [['P1', 2, 0], ['P2', 1, 0], ['P3', 8, 0], ['P4', 4, 0], ['P5', 5, 0]]

    test1 = Sorting_Process()

    print(test1.sort_the_processes(arr))