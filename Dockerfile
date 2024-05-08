# 使用 NVIDIA CUDA 基础镜像
# FROM nvidia/cuda:11.6.1-cudnn8-devel-ubuntu20.04
FROM python:3.8-bullseye

# 设置工作目录
WORKDIR /app

# 将当前目录下的所有文件复制到镜像中的 /app 目录


# 安装相关依赖项
RUN apt-get clean && apt-get update --fix-missing && apt-get install -y python3-pip &&  apt-get clean

RUN pip config set global.index-url https://mirrors.bfsu.edu.cn/pypi/web/simple

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /app

RUN pip config set global.index-url https://mirrors.bfsu.edu.cn/pypi/web/simple

# 设置默认命令
CMD python3 main.py
