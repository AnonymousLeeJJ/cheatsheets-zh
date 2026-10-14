# HTTP 速查表

## 请求方法

| 方法 | 语义 | 幂等 |
| --- | --- | --- |
| GET | 获取资源 | ✅ |
| POST | 创建资源/提交数据 | ❌ |
| PUT | 全量更新 | ✅ |
| PATCH | 部分更新 | ❌ |
| DELETE | 删除资源 | ✅ |
| HEAD | 只取响应头 | ✅ |
| OPTIONS | 预检/查询支持的方法 | ✅ |

## 状态码速记

**1xx 信息** ｜ **2xx 成功** ｜ **3xx 重定向** ｜ **4xx 你的锅** ｜ **5xx 服务器的锅**

| 状态码 | 含义 | 常见场景 |
| --- | --- | --- |
| 200 | OK | 成功 |
| 201 | Created | POST 创建成功 |
| 204 | No Content | 删除成功，无返回体 |
| 301 / 302 | 永久 / 临时重定向 | 域名迁移 / 登录跳转 |
| 304 | Not Modified | 缓存有效，不用重新下载 |
| 400 | Bad Request | 参数格式错误 |
| 401 | Unauthorized | 没登录 / Token 失效 |
| 403 | Forbidden | 登录了但没权限 |
| 404 | Not Found | 资源不存在 |
| 405 | Method Not Allowed | GET 接口用了 POST |
| 409 | Conflict | 重复创建/状态冲突 |
| 422 | Unprocessable Entity | 参数校验失败 |
| 429 | Too Many Requests | 触发限流 |
| 500 | Internal Server Error | 服务器崩了 |
| 502 | Bad Gateway | 网关上游挂了 |
| 503 | Service Unavailable | 服务过载/维护 |
| 504 | Gateway Timeout | 上游超时 |

## 常用请求头

| 头部 | 作用 |
| --- | --- |
| `Authorization: Bearer <token>` | 身份认证 |
| `Content-Type: application/json` | 请求体格式 |
| `Accept: application/json` | 期望的响应格式 |
| `User-Agent` | 客户端标识 |
| `Cookie` | 携带 Cookie |
| `If-None-Match: <etag>` | 协商缓存 |
| `X-Requested-With: XMLHttpRequest` | 标识 Ajax 请求 |

## 常用响应头

| 头部 | 作用 |
| --- | --- |
| `Cache-Control: max-age=3600` | 缓存 1 小时 |
| `ETag` | 资源指纹，配合 304 |
| `Set-Cookie` | 种 Cookie |
| `Location` | 重定向目标 |
| `Access-Control-Allow-Origin` | CORS 允许的源 |
| `Retry-After` | 限流后多久重试 |

## curl 实战

```bash
# GET 带参数
curl "https://api.example.com/users?page=2"

# POST JSON
curl -X POST https://api.example.com/users \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer TOKEN" \
  -d '{"name":"张三","age":25}'

# 上传文件
curl -F "file=@./a.png" https://api.example.com/upload

# 看完整请求响应（排错神器）
curl -v https://api.example.com

# 只看状态码
curl -s -o /dev/null -w "%{http_code}\n" https://api.example.com
```

## 缓存逻辑一句话

强缓存（`Cache-Control`/`Expires`）不发请求 → 过期后发请求带 `If-None-Match` → 命中返回 304 → 没命中返回 200 新内容。

## Cookie 关键属性

`HttpOnly`（JS 读不到，防 XSS 偷）｜ `Secure`（仅 HTTPS）｜ `SameSite=Lax/Strict`（防 CSRF）
