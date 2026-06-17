import os
import requests

DOCS_DIR = "pages"
OUTPUT_FILE = os.path.abspath("index.html")

# ★ リポジトリ情報を追加
OWNER = "FEEL-TECH-TEST"
REPO = "project-docs4"  # このリポジトリ名に合わせる
TOKEN = os.environ.get("ORG_TOKEN", "")
HEADERS = {"Authorization": f"token {TOKEN}"} if TOKEN else {}

# ★ Releases APIで最新リリースを取得
releases_btn = ""
releases_api = f"https://api.github.com/repos/{OWNER}/{REPO}/releases"
rel_res = requests.get(releases_api, headers=HEADERS)
releases = rel_res.json()
if isinstance(releases, list) and len(releases) > 0:
    release_url = releases[0]["html_url"]
    release_tag = releases[0].get("tag_name", "latest")
    releases_btn = f'<a href="{release_url}" target="_blank">最新リリース ({release_tag})</a>'

files = []
for root, _, filenames in os.walk(DOCS_DIR):
    for name in filenames:
        path = os.path.join(root, name)
        rel = os.path.relpath(path, ".")
        files.append(rel)
files.sort()

html_top = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>ファイルダウンロード</title>
    <style>
        .btn {{
            display: inline-block;
            padding: 8px 14px;
            background: #0366d6;
            color: white;
            text-decoration: none;
            border-radius: 8px;
            margin-right: 8px;
        }}
        .btn:hover {{
            background-color: #0056b3;
        }}
    </style>
</head>
<body>
<h1>ファイルダウンロード</h1>
<div>
<a href="https://feel-tech-test.github.io/portal-site/" class="btn" target="_blank">ポータルに戻る</a>
</div>
<ul>
"""

html_bottom = """
</body>
</html>
"""

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(html_top)
    for file in files:
        f.write(f'<li><a href="{file}">{file}</a></li>\n')
    # ファイルリストの下にReleasesリンクを追加
    if releases_btn:
        f.write(f'<li>{releases_btn}</li>\n')
        f.write('</ul>\n')
    else:
        f.write(html_bottom)
    f.write(html_bottom)

print("index.html generated at root")
print("OUTPUT:", os.path.abspath(OUTPUT_FILE))

print("index.html generated at root")
print("OUTPUT:", os.path.abspath(OUTPUT_FILE))

print("index.html generated at root")
print("OUTPUT:", os.path.abspath(OUTPUT_FILE))
