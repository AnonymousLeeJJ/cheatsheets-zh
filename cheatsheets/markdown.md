# Markdown 速查表

## 标题与文本

```markdown
# 一级标题
## 二级标题
### 三级标题

**加粗**    *斜体*    ~~删除线~~    `行内代码`
> 引用内容
```

## 列表

```markdown
- 无序列表项
  - 缩进两个空格嵌套

1. 有序列表
2. 第二项

- [ ] 未完成任务
- [x] 已完成任务
```

## 链接与图片

```markdown
[链接文字](https://example.com)
[锚点链接](#标题名)
![图片描述](图片地址)

<!-- 图片加宽度（HTML 写法，GitHub 支持） -->
<img src="图片地址" width="300">
```

## 代码

````markdown
行内：`print("hi")`

代码块：
```python
def hello():
    return "指定语言有语法高亮"
```

对比块（diff 高亮）：
```diff
- 删除的行
+ 新增的行
```
````

## 表格

```markdown
| 左对齐 | 居中 | 右对齐 |
| :--- | :---: | ---: |
| a | b | c |
```

## 分割线与其他

```markdown
---
***          （三种分割线写法）

脚注：这是一个脚注[^1]
[^1]: 脚注内容

<!-- 注释，不会渲染 -->

键盘按键：<kbd>Ctrl</kbd> + <kbd>C</kbd>
```

## GitHub 专属扩展

```markdown
@用户名              提及某人
#123                引用 issue/PR
SHA 值               自动链接到提交

<details>
<summary>点击展开折叠内容</summary>
藏起来的内容
</details>

- [ ] 任务列表会自动统计进度（在 issue/PR 里）

警告块（GitHub 新语法）：
> [!NOTE]
> 提示信息

> [!WARNING]
> 警告信息

> [!IMPORTANT]
> 重要信息
```

## README 排版技巧

1. 标题层级从 `#` 开始依次递进，不要跳级
2. 中英文之间加空格：`使用 Git 管理代码`
3. 长文档开头放 `<div align="center">` 居中的标题 + 徽章区
4. 用 `<!-- toc -->` 风格的目录或手写锚点目录
5. 徽章生成：https://shields.io
