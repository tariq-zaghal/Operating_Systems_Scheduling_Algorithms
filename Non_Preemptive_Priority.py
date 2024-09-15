import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from Plotter import Plotter
from Process import Process
from Process_Statistics import Process_Statistics

p1 = Process('P1', 0, 10, 2, 3)
p2 = Process('P2', 1, 8, 4, 2)
p3 = Process('P3', 3, 14, 6, 3)
p4 = Process('P4', 4, 7, 8, 1)
p5 = Process('P5', 6, 5, 3, 0)
p6 = Process('P6', 7, 4, 6, 1)
p7 = Process('P7', 8, 6, 9, 2)

processes = [p2, p3, p4, p5, p6, p7]
cpu_queue = []
waiting_list = []

processing = True
done = False
current_process = p1

start = 0
end = -1
n = 200

for i in range(1, n + 1):

    for p in cpu_queue:
        p.waiting_time_counter = p.waiting_time_counter + 1
        p.turnaround_time_counter = p.turnaround_time_counter + 1

    for process in processes:
        process.arrival_time = process.arrival_time - 1

    for process in waiting_list:
        process.comeback_time = process.comeback_time - 1
        process.turnaround_time_counter = process.turnaround_time_counter + 1

    for process in cpu_queue:
        process.update_time = process.update_time - 1
        if process.update_time == 0:
            if process.priority > 0:
                process.priority = process.priority - 1
            process.set_update_time()

    for process in waiting_list:
        if process.comeback_time <= 0:
            cpu_queue.append(process)
            process.comeback_time = process.get_comeback_time()
            waiting_list.remove(process)

    for process in processes:
        if process.arrival_time == 0:
            cpu_queue.append(process)
            processes.remove(process)

    if processing:
        current_process.burst_time = current_process.burst_time - 1
        current_process.turnaround_time_counter = current_process.turnaround_time_counter + 1

        if current_process.burst_time == 0:
            end = i - start

            current_process.turnaround_time = current_process.turnaround_time + current_process.turnaround_time_counter
            current_process.waiting_time = current_process.waiting_time + current_process.waiting_time_counter

            current_process.turnaround_time_counter = 0
            current_process.waiting_time_counter = 0

            current_process.add_start_end_pair(start, end)
            current_process.burst_time = current_process.get_burst_time()
            current_process.priority = current_process.get_priority()
            waiting_list.append(current_process)
            processing = False
            done = True

        elif i == n:
            current_process.start_end_pair.append((start, n - start))

            current_process.turnaround_time = current_process.turnaround_time + current_process.turnaround_time_counter
            current_process.waiting_time = current_process.waiting_time + current_process.waiting_time_counter

            current_process.turnaround_time_counter = 0
            current_process.waiting_time_counter = 0
            break

    if not processing:
        current_process = cpu_queue[0]
        for process in cpu_queue:
            if process.priority < current_process.priority:
                current_process = process

        cpu_queue.remove(current_process)
        processing = True
        done = False
        start = i

processes = [p1, p2, p3, p4, p5, p6, p7]

print("For Non Preemptive Priority Scheduling:\n")

print("Schedule (start time, time spent):")
for process in processes:
    print(f"{process.process_name} : {process.start_end_pair}")


print("Waiting time and turnaround time for each process:")
for process in processes:
    print(f'{process.process_name}: waiting: {process.waiting_time}, turnaround: {process.turnaround_time}')

avg_waiting_time = Process_Statistics.get_average_waiting(processes)
avg_turnaround_time = Process_Statistics.get_average_turnaround(processes)

print(f"Average waiting time: {avg_waiting_time}")
print(f"Average turnaround time: {avg_turnaround_time}")

Plotter.plot(processes, "Non Preemptive Priority Plot")

