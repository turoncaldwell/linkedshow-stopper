class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def simulate_response_time(self, data):
        # Simulate response time counter
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        print(f"Simulated response time for data: {data}")

# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.simulate_response_time(100)
    ll.simulate_response_time(200)
