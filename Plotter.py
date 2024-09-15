import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from Process import Process

class Plotter:
    @staticmethod
    def plot(process_list, label):
        processes = process_list

        fig, ax = plt.subplots()

        ax.broken_barh(process_list[0].start_end_pair, (10, 9), facecolor='tab:blue')
        ax.broken_barh(process_list[1].start_end_pair, (20, 9), facecolor='red')
        ax.broken_barh(process_list[2].start_end_pair, (30, 9), facecolor='blue')
        ax.broken_barh(process_list[3].start_end_pair, (40, 9), facecolor='green')
        ax.broken_barh(process_list[4].start_end_pair, (50, 9), facecolor='pink')
        ax.broken_barh(process_list[5].start_end_pair, (60, 9), facecolor='orange')
        ax.broken_barh(process_list[6].start_end_pair, (70, 9), facecolor='black')

        x_axis_values = []
        for p in processes:
            for tup in p.start_end_pair:
                x_axis_values.append(tup[0])

        x_axis_values.append(200)

        x_axis_values.sort()

        x_ticks = x_axis_values
        x_labels = x_axis_values

        ax.set_title(label, fontsize=25)
        ax.set_ylabel('Process', fontsize=20)
        ax.set_xlabel('Time', fontsize=20)

        ax.set_yticks([15, 25, 35, 45, 55, 65, 75])
        ax.set_yticklabels(['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7'], fontsize=15)

        plt.xticks(ticks=x_ticks, labels=x_labels, fontsize=10)
        plt.figure(figsize=(20, 10))

        fig.set_size_inches(25, 10, forward=True)

        xs = np.linspace(1, 21, 200)

        ax.vlines(x=x_axis_values, ymin=0, ymax=len(xs), ls='--', lw=1, label='vline_multiple - full height')

        ax.set_ylim(5, 85)
        ax.set_xlim(0, 200)

        plt.show()