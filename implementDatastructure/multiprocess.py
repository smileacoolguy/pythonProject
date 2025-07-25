import multiprocessing
import os

def worker_function(name):
    """
    A function to be executed by a separate process.
    """
    print(f"Hello, {name} from process ID: {os.getpid()}")

if __name__ == "__main__":
    # Create a Process object
    # target: the function to be executed by the process
    # args: a tuple of arguments to pass to the target function
    p = multiprocessing.Process(target=worker_function, args=("Alice",))
    p1 = multiprocessing.Process(target=worker_function, args=("Ismail",))
    # Start the process
    p.start()
    p1.start()
    # Wait for the process to complete
    p.join()

    print(f"Main process finished. Main process ID: {os.getpid()}")