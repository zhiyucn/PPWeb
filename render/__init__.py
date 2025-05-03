import asyncio
from .print_render import print_commands
from .get_time import time_command
from .math_parser import evaluate_expression
async def main(code: str = ""):
    html_body = ""
    # 初始化基本HTML
    # printf(text);
    # 解析为HTML
    for line in code.split('\n'):
        print(line)
        if line == "":  # 忽略空行
            print("empty line")
        elif line.startswith("#"):  # 忽略注释行
            print("comment line")
        else:  # 处理命令行
            line = line.strip()
            if (line.startswith('printf(') or line.startswith('print(')) and line.endswith(';'):  # 处理print/printf命令
                html_body += print_commands(line)
            #elif line.startswith('get_time(') and line.endswith(';'):  # 处理get_time命令
            #    html_body += time_command(line)
            elif '+' in line or '-' in line or '*' in line or '/' in line:  # 处理数学表达式
                from .math_parser import evaluate_expression
                try:
                    result = evaluate_expression(line.strip(';'))
                    html_body += f"<p>{result}</p>"
                except ValueError as e:
                    html_body += f"<p style=\"color:red\">ERROR: {str(e)}</p>"
            else:  # 处理未知命令
                html_body += "<p style=\"color:red\">ERROR:Unknown Command</p>"
                print(f"Unknown command: {line}")
    # 构建基本HTML结构
    html = f"""<!DOCTYPE html>
<html>
<head>
    <title></title>
</head>
<body>
    {html_body}
</body>
</html>"""
    # 打印HTML
    print(html)
    return html