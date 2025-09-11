import multiprocessing
import time
import math


def worker():
    """A worker function that performs a CPU-intensive task."""
    try:
        print(f"Worker process {multiprocessing.current_process().name} started.")
        while True:
            _ = [math.sqrt(i) for i in range(1_000_000)]
    except KeyboardInterrupt:
        pass  # Child processes can be interrupted, but we'll let the main process handle the cleanup.
    finally:
        print(f"Worker process {multiprocessing.current_process().name} terminating.")


if __name__ == "__main__":
    num_cores = multiprocessing.cpu_count()
    print(f"Detected {num_cores} CPU cores.")

    processes = []
    for i in range(num_cores):
        p = multiprocessing.Process(target=worker)
        processes.append(p)
        p.start()

    print("Press Ctrl+C to stop the script and the container.")

    try:
        while any(p.is_alive() for p in processes):
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping processes...")
        for p in processes:
            p.terminate()

        # Give processes a moment to terminate
        time.sleep(1)

        for p in processes:
            if p.is_alive():
                p.join(timeout=1)
                if p.is_alive():
                    print(f"Warning: Process {p.name} did not terminate cleanly.")
    finally:
        print("All processes terminated.")
