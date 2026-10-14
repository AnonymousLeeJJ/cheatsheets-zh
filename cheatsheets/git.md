# Git 速查表

## 初始与克隆

| 命令 | 说明 |
| --- | --- |
| `git init -b main` | 初始化仓库，主分支命名为 main |
| `git clone <url>` | 克隆远程仓库 |
| `git clone --depth 1 <url>` | 浅克隆（只要最新提交，大仓库提速） |
| `git config --global user.name "名字"` | 设置全局用户名 |
| `git config --global user.email "邮箱"` | 设置全局邮箱 |

## 日常三板斧

| 命令 | 说明 |
| --- | --- |
| `git status` | 查看工作区状态 |
| `git add <文件>` / `git add -A` | 暂存指定文件 / 全部改动 |
| `git commit -m "说明"` | 提交 |
| `git commit --amend` | 修改上一次提交（未推送前） |
| `git push` / `git pull` | 推送 / 拉取 |

## 分支操作

| 命令 | 说明 |
| --- | --- |
| `git branch` | 查看本地分支 |
| `git switch -c <分支>` | 创建并切换到新分支 |
| `git switch <分支>` | 切换分支 |
| `git merge <分支>` | 合并指定分支到当前分支 |
| `git branch -d <分支>` | 删除已合并的分支 |
| `git rebase main` | 把当前分支变基到 main 上 |

## 后悔药

| 命令 | 说明 |
| --- | --- |
| `git restore <文件>` | 丢弃工作区的修改 |
| `git restore --staged <文件>` | 取消暂存（不丢改动） |
| `git reset --soft HEAD~1` | 撤销上一次提交，改动回到暂存区 |
| `git reset --hard HEAD~1` | 撤销上一次提交并**丢弃改动**（危险） |
| `git reflog` | 查看操作历史，找回"丢失"的提交 |
| `git revert <提交>` | 生成一个反向提交来撤销（安全，可推送） |

## 暂存与现场保护

| 命令 | 说明 |
| --- | --- |
| `git stash` | 暂存当前改动，干净切分支 |
| `git stash pop` | 恢复最近一次暂存并删除记录 |
| `git stash list` | 查看所有暂存 |

## 查看与排查

| 命令 | 说明 |
| --- | --- |
| `git log --oneline --graph --all` | 图形化查看分支历史 |
| `git diff` / `git diff --staged` | 查看工作区 / 暂存区差异 |
| `git blame <文件>` | 查看每行最后是谁改的 |
| `git show <提交>` | 查看某次提交的内容 |
| `git log -S "关键字"` | 搜索引入某关键字的提交 |

## 远程相关

| 命令 | 说明 |
| --- | --- |
| `git remote -v` | 查看远程地址 |
| `git fetch` | 拉取远程更新但不合并 |
| `git push -u origin <分支>` | 首次推送并关联上游 |
| `git push --force-with-lease` | 安全强推（比 --force 安全） |
