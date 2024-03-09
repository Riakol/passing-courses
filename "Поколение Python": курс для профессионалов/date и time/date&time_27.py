from datetime import timedelta

h, m, s = str(input()).split(":")

print(int(timedelta(hours=int(h), minutes=int(m), seconds=int(s)).total_seconds()))
