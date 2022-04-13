## Reference 

1. Assign 
2. as an element of List / Tuple / Dict
3. Functions

```python

def func(a, b): 
    return a + b

func(a=tom)
```

## How to avoid the ref func assignment? 
1. builtin copy
    + call_fn(arg1=copy(mutable_obj))
    + call_fn(arg1=deepcopy(mutable_obj)) # including some mutables objects
2. list copy
    + another_list = original_list[:]

# Softmax 
+ Input: values
+ Outputs: converts to [p1, p2, ,,,. pN] -> sum(p1, p2, .. pN) = 1

"""
def softmax(vec):
    return np.exp(vec) / np.sum(np.exp(vec))

-> 
def softmax(vec):
    vec = vec - vec.max(vec)
    return np.exp(vec) / np.sum(np.exp(vec))
"""
## Numerical Comparison

1. np.testing.assert_almost_equal
2. abs(a - b) <= 1e-5
3. round
## Memory-View 
### Speed up x2
当我们需要反复大量的进行一段数据的读取操作或者改变原数据的赋值操作，使用memoryview的时候，每次不不要重新在内存中进行赋值。

## Weak-Ref

当我们存储、读取大的对象或者文件的时候，该文件或者对象会被多次赋值（或者引用）


## 持久化

Running for a long time, get some objects.

objects -> save

next time we could use it again. 

+ pickle







