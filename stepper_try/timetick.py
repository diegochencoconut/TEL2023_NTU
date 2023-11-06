import time

time_interval = 4000

start_time = time.clock_gettime_ns(time.CLOCK_BOOTTIME)
print(start_time)

end_time = time.clock_gettime_ns(time.CLOCK_BOOTTIME)

while (end_time - start_time) < time_interval * 1000000:
    end_time = time.clock_gettime_ns(time.CLOCK_BOOTTIME)

print(end_time)
