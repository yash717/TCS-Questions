public class Solution {

  class Queue {

    int front, rear;
    int[] arr;
    int capacity;

    Queue() {
      capacity = 100001;
      front = 0;
      rear = 0;
      arr = new int[capacity];
    }

    // Enqueue (add) element 'e' at the end of the queue.
    public void enqueue(int e) {
      if (rear == capacity) {
        // Queue is full, cannot enqueue.
        return;
      }
      arr[rear] = e; // Add the element to the rear of the queue.
      rear++; // Move the rear pointer to the next position.
    }

    // Dequeue (retrieve) the element from the front of the queue.
    public int dequeue() {
      if (front == rear) {
        // Queue is empty, return -1.
        return -1;
      }
      int val = arr[front]; // Get the element at the front of the queue.
      front++; // Move the front pointer to the next position.
      return val;
    }
  }
}
