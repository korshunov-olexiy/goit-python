# num = 123
# print(num % 10)
# print(num % 100//10)
# print(num//100)

# print(str(num)[::-1])

# result = ''
# n = None
# while num != 0:
#     n = str(num % 10)
#     num = num // 10
#     result += n

times_to_sec = 5000
hour = times_to_sec // 3600
times_to_sec = times_to_sec % 3600
minutes = times_to_sec // 60
times_to_sec = times_to_sec % 60
print(f"{hour}h {minutes}m {times_to_sec}s")
