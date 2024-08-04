# class shape :
#     def __init__(self) :
#         pass
#     def area (self) :
#         return 0
#     def perimeter (self) :
#         return 0

# class square (shape) :
#     def __init__(self, length) :
#         self.length = length

#     def area (self) :
#         return self.length * self.length

#     def perimeter (self) :
#         return 4 * self.length

# shape = shape()
# print("shape area =",shape.area()) #0
# print("shape perimeter =",shape.perimeter()) #0

# square = square(4)

# print("square area =",square.area()) #16
# print("square perimeter =",square.perimeter()) #16


class QueueOutOfRangeException(Exception):
    pass


class queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        if self.isEmpty():
            raise ValueError("queue is empty")
        else:
            return self.queue.pop()


class second_queue(queue):

    objects = {}
    def __init__(self, name, size=10):
        super().__init__()
        self.name = name
        self.size = size
        second_queue.objects[name] = self

    def enqueue(self, item):
        if len(self.queue) == self.size:
            raise QueueOutOfRangeException("queue is full")
        else:
            super().enqueue(item)

    @classmethod
    def get_objects(cls, name):
        return cls.objects.get(name)

    @classmethod
    def save(cls, filename):
        with open(filename, "w") as f:
            for name, obj in cls.objects.items():
                f.write(f" queue name :{name}  ,queue size :{obj.size},  queue elements :{','.join(map(str, obj.queue))}\n")

    @classmethod
    def load(cls, filename):
        with open(filename, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                name = parts[0].split(":")[1].strip()
                size = int(parts[1].split(":")[1].strip())
                queue_elements = parts[2].split(":")[1].strip().split(",")
                queue_elements.extend(parts[3:])
                obj = cls(name, size)
                obj.queue = queue_elements
                cls.objects[name] = obj
                # print(parts)
                # print(name)
                # print(size)
                print(type(parts[2].split(":")[1].strip().split(",")))
                print("this is queue elements",queue_elements)


q2 = second_queue("Queue1", 10)
q2.enqueue(1)
q2.enqueue(2)
q2.enqueue("python")
q2.enqueue("python")
q2.enqueue("java")
q2.enqueue("javascript")
q2.enqueue("rust")
q2.dequeue()
q2.dequeue()
q2.dequeue()
q2.dequeue()
second_queue.save('python\queues.txt')
second_queue.objects = {}
# print(q2.get_objects("Queue1").isEmpty())
second_queue.load("python\queues.txt")

print(q2.objects.keys())
print(q2.get_objects("Queue1"))


# queue = second_queue("first-queue", 10)
# print(queue.isEmpty())
# queue.enqueue("hello")
# queue.enqueue("world")
# queue.enqueue("python")
# queue.enqueue("is")
# queue.enqueue("very")
# queue.enqueue("very")
# queue.enqueue("very")
# queue.enqueue("very")
# queue.enqueue("very")
# queue.enqueue("very")
# queue.enqueue("very")
# queue.enqueue("very")
# queue.enqueue("very")
# queue.enqueue("awesome")
# queue.dequeue()
# print(queue.isEmpty())
# print(queue.queue)
