import unittest


def job_sched(s, e, max_jobs):
    """Python3 program to check if all jobs can be scheduled if two jobs are allowed at a time."""
    s.sort()
    e.sort()
    si, ej = 1, 0
    job_count, res = 1, 1
    n = len(s)
    while si < n and ej < n:
        if s[si] < e[ej]:
            job_count = job_count + 1
            si += 1
            if res < job_count:
                res = job_count
            if res > 2:
                return False
        else:
            job_count = job_count - 1
            ej += 1
    return res <= 2


class Test(unittest.TestCase):
    def test_job_sched(self):
        startin = [1, 2, 4]  # starting time of jobs
        endin = [2, 3, 5]  # ending times of jobs
        max_jobs = 2
        expected = True
        actual = job_sched(startin, endin, max_jobs)
        self.assertEqual(expected, actual)
