import time


def wait_until(predicate, error_message, timeout=10, frequency=0.1):
    start = time.time()
    while True:
        try:
            result = predicate()
            if result:
                return result
        except:
            time.sleep(frequency)
        if time.time() - start > timeout:
            raise TimeoutError(error_message)
        time.sleep(frequency)
