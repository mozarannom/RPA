import pandas as pd
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


data = {'이름' : ['Kim', 'Park', 'Lee', 'Ho'],
        '국어' : [90, 58, 88, 100],
        '영어' : [100, 60, 80, 70],
        '수학' : [55, 65, 76, 88] }

print("1> --------------------------------------------------")
df = pd.DataFrame(data)
print(df, end="\n\n")

print("2> --------------------------------------------------")
df = pd.DataFrame(data)
print(df, end="\n\n")

print("3> --------------------------------------------------")
df = pd.DataFrame(data)
print(df, end="\n\n")

print("4> --------------------------------------------------")
df = pd.DataFrame(data)
print(df, end="\n\n")

print("5> --------------------------------------------------")
df = pd.DataFrame(data)
print(df, end="\n\n")

print("6> --------------------------------------------------")
df = pd.DataFrame(data)
print(df, end="\n\n")

print("7> --------------------------------------------------")
df = pd.DataFrame(data)
print(df, end="\n\n")