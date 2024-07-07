import os
import subprocess

# 输入和输出目录
input_dir = 'posts'
output_dir = 'contents'
css_file = r'style.css'
template_file = r'posts/template.html'
filter = r'scripts/filter.py'
# 确保输出目录存在
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 遍历输入目录中的所有文件
for filename in os.listdir(input_dir):
    if filename.endswith('.md'):
        # 构造输入和输出文件的路径
        input_file = os.path.join(input_dir, filename)
        output_file = os.path.join(output_dir, os.path.splitext(filename)[0] + '.html')
        
        # 使用 Pandoc 将 Markdown 文件转换为 HTML
        subprocess.run(['pandoc', 
                        '-s','--toc',
                        '--css', css_file,
                        '--template', template_file,
                        '--filter', filter,
                        '--mathml',
                        input_file, '-o', output_file])

print("Markdown 文件转换完成。")
