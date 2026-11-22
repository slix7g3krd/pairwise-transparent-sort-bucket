# pairwise-transparent-sort-bucket

## 领域

游戏、图形与多媒体

## 主题

半透明分桶排序

## 说明

按透明度分桶、深度剥离回读与 coverage 随 mip 缩放。

初始状态下 `render/transparent_sort_bucket.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
