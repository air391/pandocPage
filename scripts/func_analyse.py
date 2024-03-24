import ast

def analyze_calculate_function(code_str):
    # 解析代码字符串为抽象语法树
    tree = ast.parse(code_str)

    # 初始化输入和输出描述
    input_description = []
    output_description = []

    # 遍历语法树节点
    for node in ast.walk(tree):
        # 检查函数定义节点
        if isinstance(node, ast.FunctionDef):
            # 检查函数名称是否为 calculate
            if node.name == 'calculate':
                # 获取函数参数列表的名称作为输入描述
                input_description = [arg.arg for arg in node.args.args]

                # 检查函数注释是否存在
                if node.returns:
                    # 提取函数注释中的返回值描述
                    return_annotation = ast.get_source_segment(code_str, node.returns)
                    # 从函数注释中提取输出描述
                    output_description = extract_output_description_from_annotation(return_annotation)
                output_num = []
                # 检查函数体内的语句
                for statement in node.body:
                    # 检查返回值语句
                    if isinstance(statement, ast.Return):
                        # 如果函数返回了一个值，则提取其元素的表达式作为输出描述
                        if isinstance(statement.value, ast.Tuple):
                            output_num = len(statement.value.elts)
                        else:
                            output_num = 1
                assert output_num == len(output_description), f"描述与返回值个数不符:{output_num}/{output_description}"
    return input_description, output_description

def extract_output_description_from_annotation(annotation):
    # 使用字符串分割操作提取多个返回值描述
    descriptions = annotation.split(',')
    # 清理每个描述中的空白字符，并添加到列表中
    cleaned_descriptions = [description.strip() for description in descriptions]
    return cleaned_descriptions

# 要分析的 Python 代码字符串
code = """
def calculate(a, b) -> "a+b, a-b,c":
    c = a*b
    return a + b, c
"""
if __name__ == "__main__":
    input_description, output_description = analyze_calculate_function(code)

    print("输入描述:", input_description)
    print("输出描述:", output_description)
