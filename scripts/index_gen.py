import os

# 获取当前目录
current_dir = './contents'
# 获取当前目录下的所有 HTML 文件
html_files = [f for f in os.listdir(current_dir) if f.endswith('.html') and f != 'index.html']

# 生成 HTML 内容
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Navigation Page</title>
</head>
<body>
    <h1>Navigation Page</h1>
    <ul>
"""

for html_file in html_files:
    # 生成链接
    link = f'<li><a href="{html_file}">{html_file}</a></li>'
    html_content += link

html_content += """
    </ul>
</body>
</html>
"""

# 将内容写入 index.html 文件
with open(os.path.join(current_dir, 'index.html'), 'w') as f:
    f.write(html_content)

print("index.html 文件已生成。")
