class LRUCache:
    def __init__(self, capacity: int = 10) -> None:
        self.capacity = capacity
        self.dict = {}

    def get(self, key: str) -> str:
        return self.dict.get(key, "")

    def set(self, key: str, value: str) -> None:
        if key in self.dict:
            del self.dict[key]
            self.dict[key] = value
        elif len(self.dict) > self.capacity - 1:
            del self.dict.pop[next(iter(self.dict))]
            self.dict[key] = value
        else:
            self.dict[key] = value

    def rem(self, key: str) -> None:
        if key in self.dict:
            del self.dict[key]

    def getall(self) -> None:
        return print(self.dict)
