---
aliases:
  - "Python Memory Management: Reference Counting"
  - Cyclic GC
  - and Weak References
---
# 
[[Garbage Collection]] [[GarbageCollector.py]] [[stongAndWeakLinks.ipynb]]


This comprehensive guide compiles concepts from your lectures into an optimized, deeply structured markdown note perfect for your Obsidian vault. It covers standard reference counting, cyclic reference leaks, the generational garbage collector, and advanced memory management using weak references (`weakref`).

## 1. Reference Counting (The Core Mechanism)

In CPython (the standard implementation of Python), the foundational mechanism for memory management is **Reference Counting**. Every Python object maintains an internal counter tracking how many references point to it.

### Key Principles:

- **Increment:** When an object is assigned a new name, placed in a list, or passed to a function, its reference count increases.
    
- **Decrement:** When a variable goes out of scope, is explicitly deleted (`del`), or gets reassigned, the reference count drops.
    
- **Deallocation:** The exact moment an object's reference count reaches **0**, CPython instantly reclaims its memory.
    

### The `sys.getrefcount` Quirk

To inspect an object's reference count, use `sys.getrefcount(obj)`.

> [!WARNING] The `+1` Phenomenon
> 
> `sys.getrefcount(obj)` always returns a value **exactly 1 higher** than expected. This occurs because passing the object into `getrefcount()` creates a temporary argument reference inside the function's execution frame.

Python

```python
import sys

name = 'Yeldos'
# Might return higher than 1 due to CPython string interning
print(sys.getrefcount(name)) 

names = [name, "Dosic"]
# Count increases because the list container now holds a reference to 'name'
print(sys.getrefcount(name)) 

del names # Drops the list container; reference count drops back down
```

## 2. The Problem of Cyclic References (Reference Cycles)

While reference counting is fast and deterministic, it has a major vulnerability: **Cyclic References**. A cycle occurs when two or more objects reference each other directly or indirectly, creating an isolated loop.

### Why Reference Counting Fails Here:

If objects `A` and `B` reference each other, their individual reference counts will always be at least 1. Even if you delete the primary names pointing to them from your main program scope, their internal cross-references ensure their counts never hit 0, causing a **memory leak**.

Python

```python
class Node:
    def __init__(self, value, next_value=None):
        self.value = value
        self.next_value = next_value

node_a = Node('a')
node_b = Node('b', node_a) # node_b points to node_a

# Creating a cycle:
node_a.next_value = node_b # node_a now points to node_b

# Breaking global scope links
del node_a
del node_b
# Both objects remain trapped in memory because they hold each other's ref counts!
```

## 3. The `gc` Module (Cyclic Garbage Collector)

To remediate reference cycles, Python relies on a secondary execution thread: the **Cyclic Garbage Collector (`gc`)**. This collector detects isolated clusters of objects that are unreachable from the root scope but are keeping each other alive.

### The Generational Hypothesis

The garbage collector groups trackable containers into **3 generations (0, 1, and 2)**:

- **Generation 0:** Contains all freshly allocated objects. Collected frequently.
    
- **Generation 1:** Houses objects that survived a Generation 0 collection sweep.
    
- **Generation 2:** Long-lived structures (like global variables or configuration objects) that survived Generation 1 sweeps. Collected least frequently.
    

### Performance Control: Thresholds and Triggers

The collector tracks object creations versus deletions using internal counters (`gc.get_count()`). When the generation 0 counter exceeds the designated generation threshold (`gc.get_threshold()`), a collection sweep triggers.

### `gc` Module Cheat Sheet

|**Function**|**Description**|
|---|---|
|`gc.collect(generation=None)`|Force manual collection. Returns the number of destroyed unreachable objects.|
|`gc.disable()` / `gc.enable()`|Toggles the cyclic collector off or on. (Turn off for tight, cycle-free performance critical loops).|
|`gc.get_threshold()`|Returns a tuple `(threshold0, threshold1, threshold2)` defining triggers.|
|`gc.get_count()`|Returns current allocation status counts `(num0, num1, num2)`.|
|`gc.get_referents(*objs)`|Returns a list of objects **directly pointed to** by the inputs.|
|`gc.get_referrers(*objs)`|Returns a list of objects that **point directly to** the inputs.|
|`gc.is_tracked(obj)`|Returns `True` if the GC watches the object. Atomic types (`int`, `str`) return `False`.|

## 4. Advanced Tool: Weak References (`weakref`)

The `weakref` module allows your application to reference an object **without incrementing its reference count**. This is an elegant design pattern to eliminate reference cycles altogether without relying entirely on cyclic GC sweeps.

### Standard (Strong) vs. Weak Links

Python

```python
import sys
import weakref

class B:
    pass

b = B()
print(sys.getrefcount(b))  # Returns 2 (Variable reference + temporary sys.getrefcount)

# Creating a weak reference
weak_b = weakref.ref(b)
print(sys.getrefcount(b))  # STILL 2! The weak reference did not increment the count.
```

### Dereferencing a Weak Reference

To access the underlying object, you must **call** the weak reference like a function:

- If the object is still alive, it returns the object instance.
    
- If the original object was deleted, it gracefully returns `None`.
    

Python

```python
print(weak_b())  # Returns: <__main__.B object at 0x...>

del b            # Strong link is broken, reference count falls to 0, memory freed
print(weak_b())  # Returns: None
```

### Intelligent Caching with `WeakKeyDictionary`

A standard Python dictionary holds a strong reference to both its keys and values. If you use objects as keys in a regular dictionary, those objects can never be cleaned up by memory management as long as the dictionary exists.

`weakref.WeakKeyDictionary` solves this. It holds **weak references to its keys**. When the key object loses all its other strong references outside the dictionary, it is cleared out of the dictionary automatically.

Python

```python
import weakref

class Asset:
    pass

cache = weakref.WeakKeyDictionary()
item = Asset()

# Store metadata inside cache linked to object
cache[item] = "Pre-computed configuration metadata"
print(dict(cache))  # Shows the asset entry

del item            # The strong name is deleted
print(dict(cache))  # Returns {} ! The entry self-destructed automatically
```

## 5. Scope and Object Lifecycles

Understanding variable scope is essential for predicting when memory cleanup occurs. When a function finishes execution, its local scope stack frame is destroyed, automatically dropping reference counts on all local variables.

Python

```python
def process_data():
    local_obj = Node('temporary')
    # local_obj has a ref count of 1
    
    return local_obj 

# The stack frame for process_data disappears here.
# However, if we capture the returned value:
active_reference = process_data() 
# The object lives on because 'active_reference' keeps the ref count at 1.
```

### Tags for Obsidian

`#python` `#memory-management` `#garbage-collection` `#cpython` `#weakref` `#caching`