class Session:

    def __init__(self, name, date, time, duration, capacity, id = None):
        self.name = name
        self.date = date
        self.time = time
        self.duration = duration
        self.capacity = capacity
        self.id = id