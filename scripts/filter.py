#!/usr/bin/env python
import pandocfilters as pf
import json
from func_analyse import analyze_calculate_function

# 用于存储交互部分的信息
interact_data = {'interactions': []}
interaction_id_counter = 0

def generate_interactive_block(interaction_id, inputs, outputs):
    # 生成交互块的 HTML 代码
    input_fields = ''.join([f'<div class="input-container"><span>{desc}</span><input type="text" placeholder="Enter {desc}"></div>' for desc in inputs])
    output_fields = ''.join([f'<div class="output-container"><span>{desc}</span><input type="text" readonly placeholder="{desc}"></div>' for desc in outputs])
    interactive_code = f'''
        <div class="interactive-python" id="{interaction_id}">
            <div class="interactive-input">
                {input_fields}
                <button onclick="runPython('{interaction_id}')">Run</button>
            </div>
            <div class="interactive-output" id="{interaction_id}-output">
                {output_fields}
            </div>
        </div>
    '''
    return pf.RawBlock('html', interactive_code)



def python_interactive(key, value, format, meta):
    global interact_data, interaction_id_counter
    # 如果当前块是代码块并且语言为 python-interactive
    if key == 'CodeBlock' and 'python-interactive' in value[0][1]:
        # 为交互块生成唯一的 ID
        interaction_id_counter += 1
        interaction_id = f"interactive-{interaction_id_counter}"
        python_code = value[1]
        # 分析 Python 代码，获取输入输出描述信息
        input_descriptions, output_descriptions = analyze_calculate_function(python_code)
        # 将交互部分的信息保存到全局变量中
        interact_data['interactions'].append({'id': interaction_id, 'inputs': input_descriptions, 'outputs': output_descriptions})
        # 生成交互块的 HTML 代码
        interact = generate_interactive_block(interaction_id, input_descriptions, output_descriptions)
        original = pf.CodeBlock(['',['python'],[]], value[1])
        return [original, interact]

def main():
    pf.toJSONFilter(python_interactive)
    # 在 Pandoc 过滤器执行完毕后，将交互部分的信息写入文件
    with open('interact_data.json', 'w') as file:
        json.dump(interact_data, file)

if __name__ == "__main__":
    main()
