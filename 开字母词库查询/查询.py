import os
import tkinter as tk
from tkinter import filedialog

# Issues
# 还是无法正确匹配空格：
# 例如查询`***********`会出现`BATTLE NO.1`
# 反之使用`B***** ****`则正常输出`BATTLE NO.1`

def wildcard_match(pattern, text):
    m, n = len(pattern), len(text)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    for i in range(1, m + 1):
        if pattern[i - 1] == '*':
            dp[i][0] = dp[i - 1][0]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if pattern[i - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
            elif pattern[i - 1] == text[j - 1] or pattern[i - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]

    return dp[m][n]

def load_phrases_from_files(file_paths):
    phrases = set()  # 使用集合存储词条，确保不会重复
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                phrase = line.strip()
                phrases.add(phrase)  # 添加到集合中
    return phrases

def find_closest_phrases(pattern, phrases):
    closest_phrases = []
    max_matched_chars = 0

    for phrase in phrases:
        if len(phrase) != len(pattern):
            continue

        if wildcard_match(pattern, phrase):
            matched_chars = sum(1 for p, t in zip(pattern, phrase) if p == t or p == '*')
            if matched_chars >= max_matched_chars:
                if matched_chars > max_matched_chars:
                    closest_phrases.clear()
                closest_phrases.append(phrase)
                max_matched_chars = matched_chars

    return closest_phrases

def browse_files():
    file_paths = filedialog.askopenfilenames(title="选择词库文件")
    return file_paths

def main():
    # 创建 Tkinter 窗口
    root = tk.Tk()
    root.withdraw()  # 隐藏 Tkinter 窗口

    # 让用户选择词库文件
    print("请选择要加载的词库文件")
    file_paths = browse_files()

    # 加载词库
    phrases = load_phrases_from_files(file_paths)

    # 多次查询，直到用户输入 exit()
    while True:
        # 查询内容
        print("\n请输入查询内容（输入 exit() 退出）：")
        query = input()

        if query.lower() == 'exit()':
            break

        # 搜索最接近的短语
        results = find_closest_phrases(query, phrases)
        if results:
            print("查询结果:")
            for result in results:
                print(result)
        else:
            print("未找到匹配的短语。")

if __name__ == "__main__":
    main()
