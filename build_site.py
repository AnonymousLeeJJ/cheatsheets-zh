# -*- coding: utf-8 -*-
"""Build docs/index.html: embed all cheatsheet markdown files, render with marked.js (CDN)."""
import json, pathlib

root = pathlib.Path(__file__).parent
sheets_dir = root / "cheatsheets"
docs = root / "docs"
docs.mkdir(exist_ok=True)

SHEET_META = {
    "git": ("Git", "🌿", "版本控制日常操作与后悔药"),
    "docker": ("Docker", "🐳", "镜像容器 Compose 一把梭"),
    "linux": ("Linux", "🐧", "文件/进程/网络高频命令"),
    "vim": ("Vim", "⌨️", "从入门到退出（真的）"),
    "regex": ("正则表达式", "🔣", "语法速查 + 实战模板"),
    "http": ("HTTP", "🌐", "状态码/头部/curl 实战"),
    "sql": ("SQL", "🗄️", "查询/连接/窗口函数/优化"),
    "markdown": ("Markdown", "📝", "基础语法 + GitHub 扩展"),
    "npm": ("npm", "📦", "依赖管理/脚本/发布"),
    "vscode": ("VS Code", "💡", "快捷键与必装插件"),
    "python": ("Python", "🐍", "常用语法与现代写法"),
}

sheets = []
for f in sorted(sheets_dir.glob("*.md")):
    key = f.stem
    name, icon, desc = SHEET_META.get(key, (key, "📄", ""))
    sheets.append({
        "id": key, "name": name, "icon": icon, "desc": desc,
        "content": f.read_text(encoding="utf-8"),
    })

html = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>开发者速查表 · Cheatsheets 中文精选</title>
<meta name="description" content="Git、Docker、Linux、Vim、正则、HTTP、SQL 等开发者高频速查表，中文整理，随查随用">
<style>
  :root {
    --bg: #f6f7f9; --card: #ffffff; --text: #1f2328; --muted: #656d76;
    --accent: #2563eb; --accent-soft: #e8effd; --border: #e3e6ea; --radius: 14px;
  }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { font-family: -apple-system, "PingFang SC", "Microsoft YaHei", "Segoe UI", sans-serif;
         background: var(--bg); color: var(--text); line-height: 1.6; }
  .wrap { max-width: 1080px; margin: 0 auto; padding: 0 20px; }
  header.hero { text-align: center; padding: 60px 20px 36px; }
  header.hero h1 { font-size: 2.3rem; }
  header.hero p.sub { color: var(--muted); margin-top: 12px; font-size: 1.05rem; }
  .toolbar { position: sticky; top: 0; z-index: 10; background: rgba(246,247,249,0.92);
             backdrop-filter: blur(8px); padding: 14px 0 12px; border-bottom: 1px solid var(--border); }
  .search { width: 100%; padding: 12px 18px; border: 1px solid var(--border); border-radius: 999px;
            font-size: 1rem; background: var(--card); outline: none; }
  .search:focus { border-color: var(--accent); }
  main { padding: 28px 0 60px; }
  .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 14px; }
  .card { background: var(--card); border: 1px solid var(--border); border-radius: var(--radius);
          padding: 22px; cursor: pointer; transition: transform .15s, box-shadow .15s; }
  .card:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(31,35,40,0.08); }
  .card .icon { font-size: 1.8rem; }
  .card h3 { margin: 8px 0 4px; font-size: 1.1rem; }
  .card p { color: var(--muted); font-size: 0.88rem; }
  .empty { text-align: center; color: var(--muted); padding: 60px 0; }
  /* sheet view */
  #sheetView { display: none; }
  .sheet-head { display: flex; align-items: center; gap: 14px; margin-bottom: 18px; flex-wrap: wrap; }
  .sheet-head .back { padding: 8px 16px; border-radius: 999px; border: 1px solid var(--border);
                      background: var(--card); cursor: pointer; font-size: 0.88rem; }
  .sheet-head .back:hover { border-color: var(--accent); color: var(--accent); }
  .sheet-body { background: var(--card); border: 1px solid var(--border); border-radius: var(--radius);
                padding: 36px 44px; }
  .sheet-body h1 { font-size: 1.6rem; border-bottom: 2px solid var(--border); padding-bottom: 12px; }
  .sheet-body h2 { font-size: 1.2rem; margin: 28px 0 10px; color: var(--accent); }
  .sheet-body table { width: 100%; border-collapse: collapse; margin: 10px 0; font-size: 0.88rem; }
  .sheet-body th, .sheet-body td { border: 1px solid var(--border); padding: 8px 12px; text-align: left; }
  .sheet-body th { background: var(--accent-soft); }
  .sheet-body tr:nth-child(even) td { background: #fafbfc; }
  .sheet-body code { background: #eff1f3; border-radius: 5px; padding: 2px 6px;
                     font-family: "SF Mono", Consolas, monospace; font-size: 0.85em; }
  .sheet-body pre { background: #1f2328; color: #e6edf3; border-radius: 10px; padding: 16px 20px;
                    overflow-x: auto; margin: 12px 0; }
  .sheet-body pre code { background: none; color: inherit; padding: 0; font-size: 0.85rem; line-height: 1.6; }
  .sheet-body ol, .sheet-body ul { margin: 8px 0 8px 24px; font-size: 0.92rem; }
  .sheet-body p { margin: 8px 0; }
  footer { text-align: center; padding: 36px 20px 48px; color: var(--muted); font-size: 0.88rem; }
  footer a { color: var(--accent); text-decoration: none; }
  @media (max-width: 700px) { .sheet-body { padding: 22px 18px; } }
</style>
</head>
<body>
<header class="hero">
  <h1>⚡ 开发者速查表</h1>
  <p class="sub">Git · Docker · Linux · Vim · 正则 · HTTP · SQL · 更多 —— 中文整理，随查随用</p>
</header>

<div class="toolbar">
  <div class="wrap">
    <input class="search" id="search" type="search" placeholder="🔍 搜索命令或关键词，如：stash、端口、替换…">
  </div>
</div>

<main class="wrap">
  <div id="homeView"><div class="grid" id="grid"></div></div>
  <div id="sheetView">
    <div class="sheet-head">
      <button class="back" id="backBtn">← 返回列表</button>
    </div>
    <article class="sheet-body" id="sheetBody"></article>
  </div>
</main>

<footer>
  <p>用 ❤️ 维护 · <a href="https://github.com/AnonymousLeeJJ/cheatsheets-zh" target="_blank" rel="noopener">GitHub 仓库</a> · 欢迎 Star ⭐ 与投稿</p>
</footer>

<script src="https://cdn.jsdelivr.net/npm/marked@12/marked.min.js"></script>
<script id="sheets-data" type="application/json">__DATA__</script>
<script>
const SHEETS = JSON.parse(document.getElementById('sheets-data').textContent);
const grid = document.getElementById('grid');
const homeView = document.getElementById('homeView');
const sheetView = document.getElementById('sheetView');
const sheetBody = document.getElementById('sheetBody');

function renderGrid(q) {
  const kw = (q || '').toLowerCase();
  const list = SHEETS.filter(s => !kw ||
    (s.name + s.desc + s.content).toLowerCase().includes(kw));
  grid.innerHTML = list.length ? list.map(s => `
    <div class="card" data-id="${s.id}">
      <div class="icon">${s.icon}</div>
      <h3>${s.name}</h3>
      <p>${s.desc}</p>
    </div>`).join('')
    : '<div class="empty">没有找到相关内容 🧐</div>';
  grid.querySelectorAll('.card').forEach(el =>
    el.addEventListener('click', () => openSheet(el.dataset.id)));
}

function openSheet(id) {
  const s = SHEETS.find(x => x.id === id);
  if (!s) return;
  sheetBody.innerHTML = marked.parse(s.content);
  homeView.style.display = 'none';
  sheetView.style.display = 'block';
  window.scrollTo(0, 0);
  history.replaceState(null, '', '#' + id);
}

document.getElementById('backBtn').addEventListener('click', () => {
  sheetView.style.display = 'none';
  homeView.style.display = 'block';
  history.replaceState(null, '', location.pathname);
});
document.getElementById('search').addEventListener('input', e => {
  sheetView.style.display = 'none';
  homeView.style.display = 'block';
  renderGrid(e.target.value.trim());
});

renderGrid('');
if (location.hash) openSheet(location.hash.slice(1));
</script>
</body>
</html>
"""

html = html.replace("__DATA__", json.dumps(sheets, ensure_ascii=False))
(docs / "index.html").write_text(html, encoding="utf-8")
print("OK ->", docs / "index.html", f"({len(sheets)} sheets)")
