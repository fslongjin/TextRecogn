import os
import requests
import base64
import logging
from datetime import datetime
import tkinter as tk
from tkinter import filedialog
import ctypes

input_dir = "./input"
output_dir = "./output"

os.makedirs(input_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)

# 生成带有时间戳的日志文件名
log_filename = f'./logs/AIGCone-{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log'

# 设置日志级别
logging.basicConfig(
    filename=log_filename,  
    level=logging.DEBUG,
    format='[%(levelname)s] - %(message)s',
)

Custom_titles = 'TextRecogn-AIGC单文件检测'

print("")
print("感谢使用TextRecogn项目，github地址https://github.com/fslongjin/TextRecogn.")
print("")
print("日志仅保存在本地用于诊断脚本问题，不上传至服务器，请放心使用")
print("")

logging.info('感谢使用TextRecogn项目，github地址https://github.com/fslongjin/TextRecogn')
logging.info('本日志仅保存在本地用于诊断脚本问题，不上传至服务器，请放心使用')

URL = "http://localhost:8000/ai_check"
output_dir = "./output"

def select_file():
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    file_path = filedialog.askopenfilename()  # 打开文件选择对话框
    return file_path

file_path = select_file()
print(f"你选择的文件是：{file_path}")

with open(file_path, "rb") as f:
    response = requests.post(URL, files={"file": ("a.docx", f, "application/octet-stream")})

    # 检查网络请求是否成功
    if response.status_code != 200:
        logging.error(f"网络请求失败，状态码{response.status_code} 返回信息{response.text}")
        print(f"网络请求失败，状态码{response.status_code} 返回信息{response.text}")
        print("")
    else:
        # 将结果保存到 output_dir
        output_file = os.path.join(output_dir, os.path.basename(file_path))
        with open(output_file, "wb") as f:
            f.write(base64.b64decode(response.text))

        logging.info(f"处理结束，结果已保存到 {output_file}")
        print(f"处理结束，结果已保存到 {output_file}")
        print("")
