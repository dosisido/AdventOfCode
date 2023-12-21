import os
from abc import ABC, abstractmethod 
from collections import deque
os.chdir(os.path.abspath(os.path.dirname(__file__)))
SIGNALS = ['low', 'high']

class Component(ABC):
    def __init__(self, name:str, connections:list[str], prefix:str = ''):
        self.name = name
        self.connections = connections
        self.prefix = prefix
        pass
    def next(self):
        for el in self.connections:
            yield el
    @abstractmethod
    def operation(self, signal:int, prev:str):
        pass
    def __str__(self):
        return f"{self.prefix}{self.name} -> {', '.join(self.connections)}"
    def str(self, signal):
        return f"{SIGNALS[signal]} at {self.prefix}{self.name} -> {', '.join(self.connections)}"
    @staticmethod
    def name(self):
        return self.name

class Broadcast(Component):
    def __init__(self, name, connections):
        super().__init__(name, connections)
    def operation(self, signal:int, prev:str):
        return signal
class Flip_flop(Component):
    def __init__(self, name, connections):
        super().__init__(name, connections, '%')
        self.status = False
    def operation(self, signal:int, prev:str):
        if signal == 1: return None
        self.status = not self.status
        return 1 if self.status else 0
class Conjunction(Component):
    def __init__(self, name, connections):
        super().__init__(name, connections, '&')
        self.prevs = {}
    def add_prev(self, prev:str):
        if prev not in self.prevs:
            self.prevs[prev] = 0
    def operation(self, signal:int, prev:str):
        self.prevs[prev] = signal
        if 0 in self.prevs.values():
            return 1
        return 0

def read_file():
    components:dict[str, Component] = {}
    conjunctions = []
    with open('file.txt') as f:
        for line in f:
            name, connections = line.strip().split('->')
            name = name.strip()
            connections = [x.strip() for x in connections.strip().split(',') if x != '']
            if name[0] == '%':
                name = name[1:]
                c = Flip_flop(name, connections)
            elif name[0] == '&':
                name = name[1:]
                conjunctions.append(name)
                c = Conjunction(name, connections)
            else:
                c = Broadcast(name, connections)
            components[name] = c

    for key, value in components.items():
        for to_connect in value.next():
            if to_connect in conjunctions:
                components[to_connect].add_prev(key)

    
    return components
components = read_file()

def elaborate(to_print = True):
    queue = deque()
    queue.append(('broadcaster', 0, 'button'))

    n_signals = [1, 0]
    string_to_compare = ''
    
    s = f"\tbutton -{SIGNALS[0]}-> broadcaster"
    string_to_compare += s.strip()
    if to_print: print(s)

    while queue:
        item_name, signal, sender = queue.popleft()
        if item_name not in components: continue
        item = components[item_name]
        printed = True

        next_value = item.operation(signal, sender)
        if next_value is None: continue
        
        for next in item.next():
            if next == '': continue
            if not printed:
                printed = True
                print(item.str(signal))
            n_signals[next_value] += 1
            s = f"\t{item_name} -{SIGNALS[next_value]}-> {next}"
            string_to_compare += s.strip()
            if to_print: print(s)
            queue.append((next, next_value, item_name))

    if to_print: print(f"Number of signals: {n_signals[0]} low, {n_signals[1]} high")

    return string_to_compare, n_signals

def find_iterations():
    n = [0, 0]
    A = []
    S, a = elaborate(False)
    A.append(a)
    n[0] += a[0]
    n[1] += a[1]
    index = 1
    s, a = elaborate(False)
    while s != S:
        print(f"Index: {index}")
        A.append(a)
        n[0] += a[0]
        n[1] += a[1]
        index += 1
        s, a = elaborate(False)
    
    print(f"Number of iterations at the end: {index}")
    print(f"Number of signals: {n[0]} low, {n[1]} high")
    return index, n, A

N = 1000
i, n, A = find_iterations()
div = N // i
rem = N % i
n[0] *= div
n[1] *= div

for a in A[:rem]:
    n[0] += a[0]
    n[1] += a[1]

print(f"Number of signals: {n[0]} low, {n[1]} high")
print(f"Answer: {n[0] * n[1]}")






""" 
492750000 low
 """