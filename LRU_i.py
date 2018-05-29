from collections import OrderedDict
class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.order_dict = OrderedDict()
        self.dict_size = 0

    def get(self, key):
        #print self.order_dict, key, self.dict_size, self.capacity, "get"
        val = -1
        if self.order_dict.get(key):
            val = self.order_dict[key]
            del self.order_dict[key]
            self.order_dict[key]=val
        return val

    def put(self, key, value):
        #print self.order_dict, key, self.dict_size, self.capacity, "put"
        if self.dict_size < self.capacity or self.order_dict.get(key):
            val = self.order_dict.get(key,None)
            if val:
                del self.order_dict[key]
                self.order_dict[key]=value
            else:
                self.order_dict[key] = value
                self.dict_size += 1
        else:
            while self.dict_size >= self.capacity:
                self.order_dict.popitem(last=False)
                self.dict_size -= 1
            self.order_dict[key] = value
            self.dict_size += 1