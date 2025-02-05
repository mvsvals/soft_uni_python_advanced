
jobs = [int(x) for x in input().split(', ')]

desired_job_value = jobs[int(input())]

cycles = 0
while desired_job_value in jobs:
    value = min(jobs)
    jobs.remove(value)
    cycles += value

print(cycles)