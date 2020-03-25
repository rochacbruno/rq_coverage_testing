"""Enqueue jobs and test it."""
import time

from redis import Redis
from rq import Queue

from tasks import count_words_at_url

# Tell RQ what Redis connection to use
q = Queue(connection=Redis())  # no args implies the default queue


def produce_task(url):
    """Enqueue a task."""
    # Delay execution of count_words_at_url('http://nvie.com')
    return q.enqueue(count_words_at_url, url)


def test_produce_task():
    """Ensure task is enqued and resolved, also produces coverage."""
    # Enqueue a job
    job = produce_task("http://www.example.com")
    assert job.result is None
    # Now, wait a while, until the worker is finished
    time.sleep(2)
    assert job.result == 120
