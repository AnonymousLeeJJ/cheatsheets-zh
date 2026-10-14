# Docker 速查表

## 镜像

| 命令 | 说明 |
| --- | --- |
| `docker pull <镜像>:<标签>` | 拉取镜像 |
| `docker images` | 查看本地镜像 |
| `docker build -t <名字>:<标签> .` | 用当前目录 Dockerfile 构建 |
| `docker rmi <镜像>` | 删除镜像 |
| `docker image prune` | 清理悬空镜像 |
| `docker save -o x.tar <镜像>` / `docker load -i x.tar` | 导出 / 导入镜像 |

## 容器生命周期

| 命令 | 说明 |
| --- | --- |
| `docker run -d --name web -p 8080:80 nginx` | 后台运行并映射端口 |
| `docker run -it --rm ubuntu bash` | 交互式运行，退出即删 |
| `docker ps` / `docker ps -a` | 运行中 / 全部容器 |
| `docker stop <容器>` / `docker start <容器>` | 停止 / 启动 |
| `docker restart <容器>` | 重启 |
| `docker rm <容器>` | 删除容器 |
| `docker rm -f $(docker ps -aq)` | 强制删除所有容器（慎用） |

## 排查调试

| 命令 | 说明 |
| --- | --- |
| `docker logs -f <容器>` | 跟踪日志 |
| `docker logs --tail 100 <容器>` | 看最后 100 行 |
| `docker exec -it <容器> bash` | 进入容器终端 |
| `docker inspect <容器>` | 查看完整配置（IP、挂载等） |
| `docker stats` | 实时资源占用 |
| `docker cp <容器>:/路径 ./本地` | 容器与宿主互拷文件 |

## 常用 run 参数

| 参数 | 说明 |
| --- | --- |
| `-d` | 后台运行 |
| `-p 宿主:容器` | 端口映射 |
| `-v 宿主:容器` | 目录挂载 |
| `-e KEY=VALUE` | 环境变量 |
| `--name` | 容器命名 |
| `--rm` | 退出后自动删除 |
| `--restart unless-stopped` | 开机/异常自启 |
| `--network <网络>` | 指定网络 |

## Compose

| 命令 | 说明 |
| --- | --- |
| `docker compose up -d` | 启动全部服务 |
| `docker compose down` | 停止并删除 |
| `docker compose logs -f <服务>` | 看某服务日志 |
| `docker compose ps` | 查看服务状态 |
| `docker compose up -d --build` | 重新构建并启动 |
| `docker compose exec <服务> sh` | 进入服务容器 |

## 清理

| 命令 | 说明 |
| --- | --- |
| `docker system df` | 查看磁盘占用 |
| `docker system prune` | 清理停止的容器、悬空镜像、未用网络 |
| `docker system prune -a --volumes` | 深度清理（慎用，会删未使用镜像和数据卷） |
