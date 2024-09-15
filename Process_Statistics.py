class Process_Statistics:
    @staticmethod
    def get_average_waiting(process_list):
        process_counter = 0
        waiting_sum = 0

        for p in process_list:
            if p.turnaround_time > 0:
                process_counter += 1
                waiting_sum += p.waiting_time

        return waiting_sum / process_counter

    @staticmethod
    def get_average_turnaround(process_list):
        process_counter = 0
        turnaround_sum = 0

        for p in process_list:
            if p.turnaround_time > 0:
                process_counter += 1
                turnaround_sum += p.turnaround_time

        return turnaround_sum / process_counter