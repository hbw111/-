# break和continue

### 相同点：两个语句都是跳出循环。

### 不同点：break语句的作用是直接终止整个循环，其后面内容都不执行，并会返回设置的跳出后的值。而continue语句的作用是只跳出本次循环并开始下一轮循环。


```python
for i in range(1,10):
        if i % 2 == 0:
            break
print(i)

```

    2
    


```python
a={1,}
a.remove(1)
for i in range(1,10):
        if i % 2 == 0:
            a.add(i)            
            continue
print(a)
```

    {2, 4, 6, 8}
    


```python

```
