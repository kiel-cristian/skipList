from random import randint, seed

class SkipNode(object):
    def __init__(self, height = 0, key = None):
        self.key = key
        self.next = [None]*height

class SkipList(object):
    def __init__(self):
        self.head = SkipNode()
        self.len = 0
        self.maxHeight = 0

    def __len__(self):
        return self.len

    def closestNodes(self, key):
        '''
        Entrega los nodos más cercanos al valor de 'key' por la izquierda, en todos los niveles.
        ie. update[0] contendrá al nodo inmediatamente anterior al que contiene a 'key' o la sobrepasa
        (en caso de que no esté presente), en la lista más 'baja'.
        '''
        update = [None]*self.maxHeight
        x = self.head
        for i in reversed(range(self.maxHeight)):
            while x.next[i] != None and x.next[i].key < key:
                x = x.next[i]
            update[i] = x
        return update

    def insert(self, key):
        node = SkipNode(self.randomHeight(), key)

        self.maxHeight = max(self.maxHeight, len(node.next))
        while len(self.head.next) < len(node.next):
            self.head.next.append(None)

        update = self.closestNodes(key)
        if self.search(key, update) == None:
            for i in range(len(node.next)):
                node.next[i] = update[i].next[i]
                update[i].next[i] = node
            self.len += 1

    def search(self, key, update = None):
        if update == None:
            update = self.closestNodes(key)
        if len(update) > 0:
            candidate = update[0].next[0]
            if candidate != None and candidate.key == key:
                return candidate
        return None

    def contains(self, key, update = None):
        return self.search(key, update) != None

    def randomHeight(self):
        height = 1
        while randint(1, 2) != 1:
            height += 1
        return height