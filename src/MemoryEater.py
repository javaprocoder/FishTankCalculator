import gc

class MemoryEater:
    def __init__(self):
        self.data = "X" * 10**6  # 1MB of data

memory_hog = []

try:
    while True:
        memory_hog.append(MemoryEater())
        if len(memory_hog) % 1000 == 0:
            print(f"Objects created: {len(memory_hog)}")
        gc.collect()  # Attempt to trigger garbage collection
except MemoryError:
    print("Memory exhausted! Garbage collector couldn't free up enough space.")