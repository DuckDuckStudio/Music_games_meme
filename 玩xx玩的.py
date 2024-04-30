from tkinter import messagebox
import random

text = [
    "原神", "崩坏：星穹铁道", "崩坏3", "绝区零",# 米
    "明日方舟",# 其他
    "Arcaea", "Phigros", "Orzmic", "MuseDash", "OSU!", "Project Sekai",# 音游
    "源神", "范式：启原", "阿卡抑",# 音游别名
    "弓蛇", "垂直判定", "下落式音游",# 音游专有名词
    "Visual Code", "Visual Studio",# IDE
]

r = random.choice(text)

messagebox.showinfo("系统提示", f"玩 {r} 玩的")
