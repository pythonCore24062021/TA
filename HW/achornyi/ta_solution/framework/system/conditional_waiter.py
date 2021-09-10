import time

from framework.system._system_settings import DEFAULT_WAITER_TIMEOUT
from framework.system._system_settings import DEFAULT_WAITER_INTERVAL


def wait_while(predicate, wait_while_description="",
               timeout=DEFAULT_WAITER_TIMEOUT,
               interval=DEFAULT_WAITER_INTERVAL):
    deadline = time.time() + timeout
    while time.time() < deadline:
        if predicate():
            time.sleep(interval)
        else:
            return
        raise TimeoutError(f"{wait_while_description} has timed out after {timeout} seconds");


def wait_until(predicate, wait_until_description="",
               timeout=DEFAULT_WAITER_TIMEOUT,
               interval=DEFAULT_WAITER_INTERVAL):
    wait_while(not predicate, wait_until_description, timeout, interval)
