def evaluate_expression(expr: str) -> float:
    """
    计算基本数学表达式(+-*/)
    :param expr: 数学表达式字符串
    :return: 计算结果
    """
    try:
        # 安全评估数学表达式
        return float(eval(expr, {"__builtins__": None}, {}))
    except (SyntaxError, TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Invalid expression: {expr}") from e