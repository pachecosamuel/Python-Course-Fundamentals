import statistics as stats

data = [1.2, 3.4, 1.7, 4.5, 3.2, 2.3, 5.6, 2.4, 1.6]
average = stats.mean(data)

above_average = filter(lambda value: value > average, data)

print(f"Average -> {average:.3f}")
print(f"Filter average -> {list(above_average)}")