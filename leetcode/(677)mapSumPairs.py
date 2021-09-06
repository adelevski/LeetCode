


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}

    def insert(self, key: str, val: int) -> None:
        self.d[key] = val

    def sum(self, prefix: str) -> int:
        output = 0
        for k,v in self.d.items():
            if k.startswith(prefix):
                output += v
        return output