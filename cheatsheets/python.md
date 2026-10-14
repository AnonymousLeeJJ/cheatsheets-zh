# Python 速查表

## 数据类型与常用操作

```python
# 字符串
s = "hello world"
s.upper(); s.split(); s.replace("o", "0"); s.strip()
s.startswith("he"); "world" in s
f"格式化 {name}，保留两位 {pi:.2f}"

# 列表
lst = [1, 2, 3]
lst.append(4); lst.insert(0, 0); lst.pop(); lst.remove(2)
lst.sort(reverse=True); sorted(lst); lst[::-1]  # 反转
lst[1:3]  # 切片

# 字典
d = {"a": 1}
d.get("b", 0)          # 安全的取值
d.setdefault("c", [])  # 没有则设默认值
d.keys(); d.values(); d.items()
{a: b for a, b in d.items() if b}  # 字典推导式

# 集合（去重/交并差）
a, b = {1, 2, 3}, {2, 3, 4}
a & b   # {2, 3} 交集
a | b   # {1,2,3,4} 并集
a - b   # {1} 差集
```

## 推导式与常用内建

```python
[x*2 for x in range(10) if x % 2 == 0]      # 列表推导
enumerate(lst)                                # 带索引遍历
zip(a, b)                                     # 并行遍历
any(lst); all(lst)                            # 任一/全部
max(lst, key=lambda x: x.age)                 # 按属性取最大
sorted(lst, key=lambda x: -x.score)
```

## 文件与 JSON

```python
# 文件（with 自动关闭）
with open("a.txt", encoding="utf-8") as f:
    content = f.read()

# JSON
import json
data = json.loads('{"a": 1}')           # 字符串 → 对象
text = json.dumps(data, ensure_ascii=False, indent=2)  # 对象 → 字符串
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
```

## 异常处理

```python
try:
    result = 10 / x
except ZeroDivisionError as e:
    print("除零了", e)
except (ValueError, TypeError):
    pass
else:
    print("没异常才执行")
finally:
    print("一定执行")

raise ValueError("自定义错误信息")
```

## 类

```python
class User:
    count = 0                      # 类属性

    def __init__(self, name):
        self.name = name           # 实例属性
        User.count += 1

    def __repr__(self):            # print 时显示
        return f"User({self.name})"

    @property
    def upper_name(self):          # 像属性一样调用
        return self.name.upper()

    @staticmethod
    def is_valid(name):
        return len(name) > 0
```

## 实用标准库

```python
from pathlib import Path
p = Path("a/b.txt")
p.exists(); p.read_text(encoding="utf-8"); p.parent; p.suffix

from collections import Counter, defaultdict
Counter("hello")                   # 字符计数
dd = defaultdict(list)             # 不怕 KeyError

from datetime import datetime, timedelta
datetime.now() + timedelta(days=7)
datetime.now().strftime("%Y-%m-%d %H:%M")

import itertools
itertools.chain([1,2],[3,4]); itertools.combinations([1,2,3], 2)
```

## 环境管理

```bash
python -m venv .venv            # 建虚拟环境
.venv\Scripts\activate          # Windows 激活
source .venv/bin/activate       # Mac/Linux 激活
pip install -r requirements.txt # 装依赖
pip freeze > requirements.txt   # 导出依赖
```

## 现代写法速查

```python
# 海象运算符
if (n := len(data)) > 10:
    print(n)

# 类型标注
def greet(name: str, age: int = 18) -> str:
    return f"{name} {age}"

# match 语句（3.10+）
match status:
    case 200: return "OK"
    case 404: return "没找到"
    case _:   return "其他"
```
