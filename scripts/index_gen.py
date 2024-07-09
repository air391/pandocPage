import os

# 获取当前目录
current_dir = './posts'
# 获取当前目录下的所有 md 文件
md_files = [f[:-3] for f in os.listdir(current_dir) if f.endswith('.md') and f != 'index.md']


# 生成 md 内容
md_content = """
# Navigation Page

"""

for md_file in md_files:
    # 生成链接
    link = f'- [{md_file}]({md_file}.html) \n'
    md_content += link

# 将内容写入 index.html 文件
with open(os.path.join(current_dir, 'index.md'), 'w', encoding='utf-8' ) as f:
    f.write(md_content)

print("index.md 文件已生成。")
