import math

#import pandas_datareader as web

def progress_bar(progress, total):
    percent = 100 * (progress / float(total))
    bar = '█' * int(percent) + '-' * (100 - int(percent))
    print(f"\r|{bar}| {percent:.2f}%", end="\r")

number = [x * 2 for x in range(2000, 3000)]    
results = []

progress_bar(0, len(number))
for i, x in enumerate(number):
    results.append(math.factorial(x))
    progress_bar(i + 1,len(number))
    
