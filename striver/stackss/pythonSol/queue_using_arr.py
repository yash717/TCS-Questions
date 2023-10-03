from typing import List


class Queue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.arr = [0] * 100001  # Initialize an array to simulate the queue.

    # Enqueue (add) element 'e' at the end of the queue.
    def enqueue(self, e: int) -> None:
        self.arr[self.rear] = e  # Add the element to the rear of the queue.
        self.rear += 1  # Move the rear pointer to the next position.

    # Dequeue (retrieve) the element from the front of the queue.
    def dequeue(self) -> int:
        if self.front == self.rear:
            return -1  # If the queue is empty, return -1.
        # Get the element at the front of the queue.
        val = self.arr[self.front]
        self.front += 1  # Move the front pointer to the next position.
        return val
