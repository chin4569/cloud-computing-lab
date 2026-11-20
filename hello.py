# 云计算实验：Git 演示程序（第二次修改）


def greet(name):
    return f"Hello, {name}! Welcome to cloud-computing-lab."


def add(a, b):
    """返回两个整数的和。"""
    return a + b


def main():
    name = "同学"
    print(greet(name))
    print(f"1 加 2 等于 {add(1, 2)}。")
    print("这是第二次提交修改后的版本。")


if __name__ == "__main__":
    main()
