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


def is_insertion_sort_faster(arr):
    start_time = time.time()
    insertion_sort(arr)
    insertion_sort_time = time.time() - start_time

    start_time = time.time()
    merge_sort(arr)
    merge_sort_time = time.time() - start_time

    return insertion_sort_time < merge_sort_time


# Test the function for various array sizes and degrees of disorder
results = []
for n in [10, 100, 1000]:
    print("IN For Loop" , n)
    start_time = time.time()
    for disorder in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
        arr = list(range(n))
        for i in range(int(n*disorder/100)):
            j = random.randint(0, n-1)
            k = random.randint(0, n-1)
            arr[j], arr[k] = arr[k], arr[j]

        if is_insertion_sort_faster(arr):
            results.append((n, disorder, "Insertion sort",
                           time.time() - start_time))
        else:
            results.append((n, disorder, "Merge sort",
                           time.time() - start_time))


# Create a scatter plot of the results
fig = go.Figure(data=go.Scatter(x=[x[1] for x in results], y=[x[3] for x in results],
                                mode='markers',
                                marker=dict(symbol='circle',
                                            size=5,
                                            color=[
                                                1 if x[2] == "Insertion sort" else 0 for x in results],
                                            colorscale='Viridis',
                                            opacity=0.8),
                                hovertemplate='<b>n=10<sup> %{x:.0f}</sup></b><br>Disorder=%{y}%<br>%{text}<br>Time=%{y:.3f} seconds'))

fig.update_layout(xaxis=dict(title='Degree of disorder'),
                  yaxis=dict(title='Time (seconds)', type='log'),
                  title='Insertion sort vs Merge sort')

fig.add_shape(
    dict(
        type="line",
        x0=50,
        y0=0,
        x1=50,
        y1=10,
        line=dict(color="red", width=2, dash="dot")))

fig.show()
