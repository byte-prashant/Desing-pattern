
from queue import PriorityQueue
from collections import Counter
import heapq

# bump priority by adding to freq count


class Item(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val

    def __lt__(self, other):
        return self.val > other.val

    def __cmp__(self, other):
        return cmp(self.val > other.val)


class LFUCache:

    def __init__(self, capacity: int):
        self.counter = dict()
        self.capacity = capacity
        self.list = []
        self.heap = None

    def get(self, key: int) -> int:
        if str(key) not in self.counter:
            print(-1)
            return -1
        key = str(key)
        val = self.counter[key]['value']
        self.counter[key]['count'] += 1
        self.list = [Item(k, v['count'])
                     for k, v in self.counter.items()]
        heapq.heapify(self.list)
        print("heapify_list", [(i.key, i.val) for i in self.list])
        print(val)
        return val

    def put(self, key: int, value: int) -> None:
        key = str(key)

        if key in self.counter:
            return self.get(key)

        self.counter[key] = {'value': value, 'count': 1}
        # print(self.list)

        item = Item(str(key), 1)
        print("key", item.key)
        if (len(self.list) >= self.capacity):
            item = heapq.heappushpop(self.list, item)
            del self.counter[item.key]
        else:
            heapq.heappush(self.list, item)
        # print(self.counter, self.list)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
if __name__ == '__main__':
    cache = LFUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)
    cache.put(3, 3)
    cache.get(2)
    cache.get(3)
    cache.put(4, 4)
    cache.get(1)
    cache.get(3)
    cache.get(4)