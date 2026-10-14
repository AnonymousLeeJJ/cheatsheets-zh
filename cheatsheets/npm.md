# npm 速查表

## 安装与依赖

| 命令 | 说明 |
| --- | --- |
| `npm init -y` | 快速生成 package.json |
| `npm install <包>` / `npm i <包>` | 安装到 dependencies |
| `npm i -D <包>` | 安装到 devDependencies（开发依赖） |
| `npm i <包>@1.2.3` | 安装指定版本 |
| `npm i` | 按 package.json 安装全部依赖 |
| `npm ci` | 严格按 lock 文件安装（CI 环境推荐） |
| `npm uninstall <包>` | 卸载 |
| `npm update <包>` | 更新到允许的最新版 |

## 版本号规则（SemVer）

`主版本.次版本.修订号` → `^1.2.3` 允许次版本升级（默认）｜ `~1.2.3` 只允许修订升级 ｜ `1.2.3` 锁死

## 脚本

| 命令 | 说明 |
| --- | --- |
| `npm run` | 列出所有可用脚本 |
| `npm run <脚本名>` | 执行 scripts 里的命令 |
| `npm start` / `npm test` | 特殊脚本可省略 run |

```json
{
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  }
}
```

## 查看信息

| 命令 | 说明 |
| --- | --- |
| `npm ls <包>` | 查看安装版本和依赖树 |
| `npm outdated` | 查看哪些包有新版本 |
| `npm view <包> versions` | 查看该包的所有发布版本 |
| `npm view <包>` | 查看包详情（描述、仓库地址等） |
| `npm audit` | 安全漏洞扫描 |
| `npm audit fix` | 自动修复可修复的漏洞 |

## 全局与缓存

| 命令 | 说明 |
| --- | --- |
| `npm i -g <包>` | 全局安装（CLI 工具） |
| `npm ls -g --depth=0` | 查看全局安装的包 |
| `npm root -g` | 全局安装路径 |
| `npm cache clean --force` | 清缓存（玄学问题先试试） |

## 发布自己的包

```bash
npm login                # 登录
npm version patch        # 版本号 +0.0.1 并打 git tag
npm publish              # 发布
npm publish --tag beta   # 发 beta 版（不覆盖 latest）
```

## npx（不安装直接跑）

| 命令 | 说明 |
| --- | --- |
| `npx <包>` | 临时下载并执行，用完即弃 |
| `npx create-react-app my-app` | 脚手架经典用法 |
| `npx cowsay hi` | 快速试用一个包 |

## 国内加速

```bash
# 切换淘宝镜像
npm config set registry https://registry.npmmirror.com

# 单次使用
npm i --registry=https://registry.npmmirror.com

# 切回官方源
npm config set registry https://registry.npmjs.org
```

## pnpm / yarn 对照

| 操作 | npm | pnpm | yarn |
| --- | --- | --- | --- |
| 安装全部 | `npm i` | `pnpm i` | `yarn` |
| 加依赖 | `npm i x` | `pnpm add x` | `yarn add x` |
| 加开发依赖 | `npm i -D x` | `pnpm add -D x` | `yarn add -D x` |
| 卸载 | `npm un x` | `pnpm rm x` | `yarn remove x` |
| 跑脚本 | `npm run dev` | `pnpm dev` | `yarn dev` |
