from operator import itemgetter

def score_by_diff(weight, length):
	return weight - length

def score_by_ratio(weight, length):
	return weight/length

def load_jobs(fname, score_ftn):
	f = open(fname)
	f.readline()
	jobs = []
	for line in f:
		weight, length = [int(x) for x in line.split()]
		score = score_ftn(weight, length)
		jobs.append([weight, length, score])
	f.close()
	jobs = sorted(jobs, key=itemgetter(2,0), reverse=True)
	return jobs

def calculate_sum(jobs):
	time = 0
	total = 0
	for job in jobs:
		time += job[1]
		total += job[0]*time
	return total

