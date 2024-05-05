import os
import requests
import base64
import logging

# 设置日志级别
logging.basicConfig(level=logging.INFO)

URL = "http://localhost:8000/ai_check"
input_dir = "./input"
output_dir = "./output"

os.makedirs(input_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)

# 使用os模块遍历目录
for root, dirs, files in os.walk(input_dir):
    for file in files:
        if file.endswith(".docx"):
            # 检查文件是否已经被处理过
            if os.path.exists(os.path.join(output_dir, file)):
                logging.info(f"文件 {file} 已处理过，跳过此文件")
                continue

            logging.info(f"开始处理文件 {file}")

            input_file = os.path.join(root, file)
            with open(input_file, "rb") as f:
                response = requests.post(URL, files={"file": ("a.docx", f, "application/octet-stream")})

                # 将结果保存到 output_dir
                output_file = os.path.join(output_dir, file)
                with open(output_file, "wb") as f:
                    f.write(base64.b64decode(response.text))

            logging.info(f"处理结束，结果已保存到 {output_file}")
