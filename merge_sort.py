import random
import time
import plotly.graph_objs as go
from plotly.subplots import make_subplots


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def time_merge_sort(arr):
    start_time = time.time()
    merge_sort(arr)
    end_time = time.time()
    return end_time - start_time


def generate_arrays(n):
    ordered_arr = list(range(n))
    reverse_arr = list(range(n))[::-1]
    random_arr = [random.randint(0, n) for _ in range(n)]
    return ordered_arr, reverse_arr, random_arr


sizes = [10, 100, 1000, 10000]  # sizes of arrays to test
colors = ['red', 'green', 'blue']  # colors to use for the different orderings

fig = make_subplots(rows=1, cols=1, x_title='Input size',
                    y_title='Time taken (seconds)')

for i, size in enumerate(sizes):
    ordered_arr, reverse_arr, random_arr = generate_arrays(size)
    arrays = [ordered_arr, reverse_arr, random_arr]

    for j, arr in enumerate(arrays):
        time_taken = time_merge_sort(arr)
        fig.add_trace(go.Scatter(x=[size], y=[
                      time_taken], name=f'{size} {j}', mode='markers', marker_color=colors[j]))
        if i > 0:
            prev_size = sizes[i - 1]
            prev_times = [fig.data[k].y[-1]
                          for k in range(j + 3 * (i - 1), j + 3 * i)]
            curr_times = [time_taken]
            fig.add_trace(go.Scatter(
                x=[prev_size, size], y=prev_times + curr_times, mode='lines', line_color=colors[j]))

fig.update_layout(showlegend=True)
fig.show()
