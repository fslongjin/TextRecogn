import os
import requests
import base64
import logging
import sys
from datetime import datetime
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import ctypes
import click
import subprocess

os.system("del /q logs")

logs_dir = "./logs"
input_dir = "./input"
output_dir = "./output"

def base_path(path):
    if getattr(sys, 'frozen', None):
        basedir = sys._MEIPASS
    else:
        basedir = os.path.dirname(__file__)
    return os.path.join(basedir, path)

tmd = base_path('')
os.chdir(tmd) 

os.makedirs(logs_dir, exist_ok=True)
os.makedirs(input_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)

# 生成带有时间戳的日志文件名
log_filename = f'./logs/AIGCall-{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log'

# 设置日志级别
logging.basicConfig(
    filename=log_filename,
    level=logging.DEBUG,
    format='[%(levelname)s] - %(message)s',
)


class CommandLineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TextRecogn-AIGC文字检测顾瑶分支 v1.5.b")

         # 创建文本框来模拟命令行界面
        self.text = tk.Text(root, wrap=tk.WORD, bg='black', fg='yellow', insertbackground='white', font=("微软雅黑", 20))
        self.text.pack(expand=True, fill=tk.BOTH)
        
        # 在文本框中插入一些行
        self.text.insert(tk.END, " 欢迎使用TextRecogn-AIGC文字检测顾瑶分支\n")
        os.system("cd")
        self.text.insert(tk.END, "\n")
        self.text.insert(tk.END, " 请单击您要使用的服务\n")
        self.text.insert(tk.END, " 1. 单文件检测\n")
        self.text.insert(tk.END, " 2. 多文件检测\n")
        self.text.insert(tk.END, " 3. 跳转至原作者项目Github\n")
        self.text.insert(tk.END, " 4. 跳转至本项目Github\n")
        self.text.insert(tk.END, " 5. 跳转至本项目介绍页\n")
        
        # 绑定鼠标点击事件
        self.text.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        # 获取鼠标点击的行号
        index = self.text.index("@%s,%s" % (event.x, event.y))
        line_number = int(index.split(".")[0])
        
        # 根据行号执行相应操作
        if line_number == 4:
            self.single_file_selection()
        elif line_number == 5:
            self.multi_file_selection()
        elif line_number == 6:
            self.goto_originauth_github()
        elif line_number == 7:
            self.goto_guyao_github()
        elif line_number == 8:
            self.goto_guyao_web()
        else:
            messagebox.showinfo("错误信息", "点击了其他行，请点击想要使用的服务")

    def single_file_selection(self):
        # 单文件选择逻辑
        messagebox.showinfo("提示", "你选择了单文件检测，正跳转至单文件检测模块，请在接下来的窗口中选择要检测的文件")
        messagebox.showinfo("提示", "检测需要时间，若30s后仍然未自动打开请重新尝试，若多次尝试均未成功，请在上一页面中找到本项目介绍页联系顾瑶")
        # 跳转到check_onlyone.py
        subprocess.run(["python", "./check_onlyone.py"])
        sys.exit()

    def multi_file_selection(self):
        # 多文件选择逻辑
        messagebox.showinfo("提示", "你选择了多文件检测，正跳转至多文件检测模块，请在output文件夹中放入要检测的文件")
        messagebox.showinfo("提示", "检测需要时间，若30s后仍然未自动打开请重新尝试，若多次尝试均未成功，请在上一页面中找到本项目介绍页联系顾瑶")
        # 跳转到check_all.py
        subprocess.run(["python", "./check_all.py"])
        sys.exit()

    def goto_originauth_github(self):
        # 跳转至原作者项目Github
        messagebox.showinfo("提示", "正在跳转至原作者项目Github")
        os.system("start https://github.com/fslongjin/textrecogn")

    def goto_guyao_github(self):
        # 跳转至本项目Github
        messagebox.showinfo("提示", "正在跳转至本项目Github")
        os.system("start https://github.com/Guyao146/TextRecognAIGC-COPY")

    def goto_guyao_web(self):
        # 跳转至本项目网页
        messagebox.showinfo("提示", "正在跳转至本项目介绍页")
        os.system("start https://aigc.mcylyr.cn/")

if __name__ == "__main__":
    root = tk.Tk()
    app = CommandLineApp(root)
    root.mainloop()