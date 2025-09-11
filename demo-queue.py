import multiprocessing
import time
import random


def producer(queue):
    """
    This function simulates a producer process.
    It generates numbers and puts them into a queue.
    """
    print("Producer process: Starting to generate data...")
    for i in range(5):
        # Simulate some work
        time.sleep(random.uniform(0.1, 0.5))
        data = f"data item {i}"
        print(f"Producer process: Putting '{data}' on the queue.")
        queue.put(data)
    # Put a "stop" signal on the queue to tell the consumer to stop
    queue.put(None)
    print("Producer process: Finished.")


def consumer(queue):
    """
    This function simulates a consumer process.
    It gets data from a queue and processes it.
    """
    print("Consumer process: Waiting for data...")
    while True:
        # Get data from the queue
        data = queue.get()
        # If we get the "stop" signal, exit the loop
        if data is None:
            break
        print(f"Consumer process: Received '{data}'. Processing...")
        # Simulate some work
        time.sleep(random.uniform(0.1, 0.5))
    print("Consumer process: Finished.")


if __name__ == "__main__":
    # Create a multiprocessing Queue
    queue = multiprocessing.Queue()

    # Create the producer and consumer processes
    p1 = multiprocessing.Process(target=producer, args=(queue,))
    p2 = multiprocessing.Process(target=consumer, args=(queue,))

    # Start the processes
    p1.start()
    p2.start()

    # Wait for both processes to complete
    p1.join()
    p2.join()

    print("\nMain process: All subprocesses have completed.")
