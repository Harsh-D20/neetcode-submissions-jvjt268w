class TimeMap:

    def __init__(self):
        self.tmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.tmap:
            self.tmap[key].append((value, timestamp))
        else:
            self.tmap[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        ret = ""
        if key in self.tmap:
            data = self.tmap[key]
            for v,t in data:
                if t <= timestamp:
                    ret = v
        return ret