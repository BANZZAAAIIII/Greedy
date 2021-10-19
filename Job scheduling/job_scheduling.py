
from random import randint
from typing import List
from job import Job

def generate_jobs(nr_jobs, max_deadline) -> List:
    '''Generate a number of jobs with random profit and deadline'''
    jobs = []
    for _ in range(nr_jobs):
        jobs.append(Job(randint(1,1000), randint(1,max_deadline)))
    return jobs

def job_scheduling(jobs) -> List:
    ''' 1. Sorts the jobs based on the decreasing profit for the job
        2. Loops through the jobs list, this will select jobs with the most profit first
        3. If there is a slot available on the jobs deadline or before the given deadline the job is added to the schedule
        4. Finished once there are no more slots or no more jobs can be added to the schedule
    '''

    schedule = [None] * len(jobs)   # Initialize all the positions

    def sort():
        '''Sort jobs based on profit in decreasing value'''
        jobs.sort(key=lambda x: x.profit, reverse=True)


    def check_feasibility(job: Job):
        ''' Check the feasibility of the selected job
            Checks if there is a slot available on the deadline 
            or before the given deadline
        '''
        for i in range(min(job.deadline - 1, len(jobs) - 1), -1, -1):
            if schedule[i] is None:
                schedule[i] = job
                break

    def scheduling():
        for i in range(len(jobs)):
            check_feasibility(jobs[i])
            if None not in schedule:    # Check if there are slots available
                break

    sort()  # Sort jobs decreasing profit 
    scheduling()    # Schedules jobs
    # Removes slots that could not be filled and returns schedule
    return [i for i in schedule if i]


def main():
    jobs = generate_jobs(50, 40)
    jobs = job_scheduling(jobs)
    print(*jobs, sep='\n')

if __name__ == "__main__":
    main()
