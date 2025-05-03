import asyncio
from .math_parser import evaluate_expression

def print_commands(text: str, colur="black"):
    # 解析为HTML
    if not text:
        return ""
    
    # 处理printf命令格式
    if text.startswith('printf(') and text.endswith(';'):
        text = text[7:-2]  # 去除printf()包裹
    elif text.startswith('print(') and text.endswith(';'):
        text = text[6:-2]  # 去除print()包裹
    
    # 检查是否是数学表达式
    if '+' in text or '-' in text or '*' in text or '/' in text:
        try:
            text = str(evaluate_expression(text))
        except ValueError as e:
            return f"<p style=\"color:red\">ERROR: {str(e)}</p>"
    # 如果是get_time命令，直接返回时间字符串
    elif text.startswith('get_time(') and text.endswith(';'):
        from .get_time import time_command  # 导入time_command函数
        text = time_command()
    else:
        # 移除引号
        text = text.replace('"', '').replace("'", "")
    
    text = f"<p style=\"color:{colur}\">{text}</p>"
    print(text)
    return text