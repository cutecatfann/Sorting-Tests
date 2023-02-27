import random
import time
import plotly.graph_objs as go


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left_half, right_half):
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            result.append(left_half[left_index])
            left_index += 1
        else:
            result.append(right_half[right_index])
            right_index += 1

    result += left_half[left_index:]
    result += right_half[right_index:]

    return result


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def measure_runtime(sort_fn, arr):
    start_time = time.time()
    sort_fn(arr)
    end_time = time.time()
    return end_time - start_time


def generate_data(num_samples):
    data = []
    for i in range(num_samples):
        arr = random.sample(range(1, num_samples * 10), i * 10)
        data.append((i * 10, arr))
    return data


def graph_runtimes(data):
    merge_sort_times = []
    insertion_sort_times = []
    sizes = []

    for size, arr in data:
        sizes.append(size)
        merge_sort_time = measure_runtime(merge_sort, arr)
        merge_sort_times.append(merge_sort_time)
        insertion_sort_time = measure_runtime(insertion_sort, arr)
        insertion_sort_times.append(insertion_sort_time)

    trace1 = go.Scatter(x=sizes, y=merge_sort_times, name="Merge Sort")
    trace2 = go.Scatter(x=sizes, y=insertion_sort_times, name="Insertion Sort")
    layout = go.Layout(title="Sort Runtimes", xaxis=dict(
        title="Array Size"), yaxis=dict(title="Time (s)"))
    fig = go.Figure(data=[trace1, trace2], layout=layout)
    fig.show()


if __name__ == "__main__":
    num_samples = 1000
    data = generate_data(num_samples)
    graph_runtimes(data)
