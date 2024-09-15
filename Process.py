class Process:
    def __init__(self, process_name, arrival_time, burst_time, comeback_time, priority):
        self.process_name = process_name

        self.__arrival_time = arrival_time
        self.arrival_time = self.__arrival_time

        self.__burst_time = burst_time
        self.burst_time = self.__burst_time

        self.__comeback_time = comeback_time
        self.comeback_time = self.__comeback_time

        self.__priority = priority
        self.priority = self.__priority

        self.start_end_pair = []

        self.in_queue = False

        self.update_time = 5

        self.waiting_time_counter = 0
        self.waiting_time = 0

        self.turnaround_time_counter = 0
        self.turnaround_time = 0

    def __lt__(self, other):
        return self.burst_time < other.burst_time

    def get_arrival_time(self):
        return self.__arrival_time

    def get_burst_time(self):
        return self.__burst_time

    def get_comeback_time(self):
        return self.__comeback_time

    def get_priority(self):
        return self.__priority

    def set_update_time(self):
        self.update_time = 5

    def add_start_end_pair(self, start, end):
        self.start_end_pair.append((start, end))