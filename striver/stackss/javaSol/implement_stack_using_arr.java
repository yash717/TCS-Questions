public class Solution {

  static class Stack {

    int arr[]; // Declare an integer array to store the stack elements.
    int top1 = -1; // Initialize the top pointer to -1 to indicate an empty stack.
    int cap1 = 0; // Initialize the capacity of the stack to 0.

    // Constructor to create a stack with the given capacity.
    Stack(int capacity) {
      arr = new int[capacity]; // Create a new integer array with the specified capacity.
      cap1 = capacity; // Set the capacity of the stack.
    }

    // Method to push an element onto the stack.
    public void push(int num) {
      if (top1 == cap1 - 1) {
        return; // If the stack is full, do nothing (return without pushing).
      }
      top1++; // Increment the top pointer.
      arr[top1] = num; // Store the element at the top of the stack.
    }

    // Method to pop and return the top element from the stack.
    public int pop() {
      if (top1 == -1) {
        return -1; // If the stack is empty, return -1 to indicate no element to pop.
      }
      int val = arr[top1]; // Get the element at the top of the stack.
      top1--; // Decrement the top pointer to remove the element.
      return val; // Return the popped element.
    }

    // Method to return the top element of the stack without popping.
    public int top() {
      if (top1 == -1) {
        return -1; // If the stack is empty, return -1 to indicate no top element.
      }
      return arr[top1]; // Return the top element of the stack.
    }

    // Method to check if the stack is empty.
    public int isEmpty() {
      if (top1 == -1) {
        return 1; // If the top pointer is -1, the stack is empty, so return 1.
      } else {
        return 0; // Otherwise, the stack is not empty, so return 0.
      }
    }

    // Method to check if the stack is full.
    public int isFull() {
      if (top1 == cap1 - 1) {
        return 1; // If the top pointer is at the capacity - 1, the stack is full, so return 1.
      } else {
        return 0; // Otherwise, the stack is not full, so return 0.
      }
    }
  }
}
