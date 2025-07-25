#multithread
import threading
import time

def print_message(message, delay):
    """
    A simple function to be executed by a thread.
    Prints a message multiple times with a delay.
    """
    for i in range(3):
        print(f"Thread: {threading.current_thread().name} - {message} ({i+1}/3)")
        time.sleep(delay)

if __name__ == "__main__":
    print("Main program started.")

    # Create two threads
    thread1 = threading.Thread(target=print_message, args=("Hello from Thread 1", 0.5), name="Thread-A")
    thread2 = threading.Thread(target=print_message, args=("Greetings from Thread 2", 0.7), name="Thread-B")

    # Start the threads
    thread1.start()
    thread2.start()

    # Wait for the threads to complete
    thread1.join()
    thread2.join()

    print("Main program finished.")