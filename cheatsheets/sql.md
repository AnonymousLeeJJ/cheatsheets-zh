# SQL 速查表

## 查询

```sql
-- 基础查询
SELECT id, name FROM users WHERE age > 18 ORDER BY id DESC LIMIT 10;

-- 去重
SELECT DISTINCT city FROM users;

-- 模糊匹配：% 任意长度，_ 单个字符
SELECT * FROM users WHERE name LIKE '张%';

-- 范围与集合
SELECT * FROM orders WHERE amount BETWEEN 100 AND 500;
SELECT * FROM users WHERE city IN ('北京', '上海');

-- 空值判断（不能用 = NULL）
SELECT * FROM users WHERE phone IS NULL;
```

## 聚合与分组

```sql
SELECT city, COUNT(*) AS cnt, AVG(age) AS avg_age
FROM users
GROUP BY city
HAVING COUNT(*) > 100          -- 分组后的过滤用 HAVING
ORDER BY cnt DESC;
```

| 聚合函数 | 说明 |
| --- | --- |
| `COUNT(*)` / `COUNT(列)` | 行数 / 非空数 |
| `SUM` `AVG` `MAX` `MIN` | 求和/平均/最大/最小 |
| `GROUP_CONCAT(列)` | 拼接分组内值（MySQL） |

## 多表连接

```sql
-- INNER JOIN：两边都有才返回
SELECT o.id, u.name FROM orders o JOIN users u ON o.user_id = u.id;

-- LEFT JOIN：左表全保留，右表没有补 NULL
SELECT u.name, COUNT(o.id) FROM users u
LEFT JOIN orders o ON o.user_id = u.id GROUP BY u.id;

-- 找「没有订单的用户」（经典反连接）
SELECT u.* FROM users u LEFT JOIN orders o ON o.user_id = u.id
WHERE o.id IS NULL;
```

## 增删改

```sql
INSERT INTO users (name, age) VALUES ('张三', 25), ('李四', 30);

UPDATE users SET age = age + 1 WHERE id = 1;   -- ⚠️ 别忘 WHERE

DELETE FROM users WHERE id = 1;                -- ⚠️ 别忘 WHERE
```

## 常用函数

| 类型 | 函数 |
| --- | --- |
| 字符串 | `CONCAT(a,b)`、`SUBSTRING(s,1,3)`、`LENGTH`、`UPPER`、`TRIM`、`REPLACE` |
| 日期 | `NOW()`、`CURDATE()`、`DATE_FORMAT(d,'%Y-%m')`、`DATEDIFF(a,b)` |
| 条件 | `IFNULL(x,0)`、`COALESCE(a,b,0)`、`CASE WHEN ... THEN ... END` |

## 窗口函数（分析利器）

```sql
-- 每个城市年龄排名
SELECT name, city, age,
  ROW_NUMBER() OVER (PARTITION BY city ORDER BY age DESC) AS rn
FROM users;

-- 累计求和
SELECT date, amount,
  SUM(amount) OVER (ORDER BY date) AS running_total
FROM sales;
```

## 索引与优化要点

1. `WHERE`、`JOIN`、`ORDER BY` 涉及的列优先建索引
2. 联合索引遵循**最左前缀**：索引 `(a,b,c)` 能服务 `a`、`a,b`、`a,b,c`，不能服务 `b,c`
3. 避免 `SELECT *`，只取需要的列
4. 避免对索引列做函数/运算：`WHERE DATE(create_time)='2026-01-01'` 会失效，改范围查询
5. `LIKE '%abc'` 前导通配符无法走索引
6. 慢查询先看 `EXPLAIN`：关注 `type`（至少 range）、`rows`、`key`

## 事务

```sql
START TRANSACTION;
UPDATE account SET balance = balance - 100 WHERE id = 1;
UPDATE account SET balance = balance + 100 WHERE id = 2;
COMMIT;   -- 出错就 ROLLBACK;
```

隔离级别速记：读未提交 < 读已提交 < **可重复读（MySQL 默认）** < 串行化，级别越高越慢但越安全。
