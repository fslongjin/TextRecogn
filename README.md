# TextRecogn
Uncovering AIGC Texts with Machine Learning

## 在线体验

[textrecogn.longjin666.cn](https://textrecogn.longjin666.cn)

在线版本上传的数据，将在24小时后删除！

为保护数据隐私，使用在线版的时候，请务必设置复杂的下载密码！

## How to download all resources?

1. Install git lfs
2. Clone this repo.

## How to run?

### 1. Build docker image

If you want to build image yourself, following the scripts:

```shell
docker build -t loooongjin/text_recogn:ernie3-nano .
```

Or you can pull the docker image:

```shell
docker pull loooongjin/text_recogn:ernie3-nano
```


### 2. Run!


```shell
docker run --rm -it -p 8000:8000 loooongjin/text_recogn:ernie3-nano
```

### 3. Check!

Put all `docx` files in `./input` , then:

```shell
python check.py
```


## AD: DragonOS龙操作系统

DragonOS是使用Rust自研内核的，具有Linux二进制兼容性的服务器操作系统。它由社区驱动开发，完全商业中立，Rust内核操作系统全国排行（按github star排序）稳居前3名！

- 仓库：https://github.com/DragonOS-Community/DragonOS
- 官网：https://dragonos.org


## 本项目贡献者

- [@fslongjin](https://github.com/fslongjin)
- [@zhuweihao12138](https://github.com/zhuweihao12138)


## 赞赏本项目

**赞赏资金在扣除TextRecogn的在线服务的服务器成本后，多余款项将全部捐入DragonOS社区公款账户！**

<img src="./static/sponsor.jpg" width="300px" />



## 关于训练数据

数据集来自 `HC3 数据集`，本模型(基于ernie3-nano)在其中英文数据上进行了约7个epoch的微调，随机分了3万条数据作为测试集（中英文各50%）

- Ernie3-nano版本：测试集正确率94.1%
- Ernie3-base版本：测试集正确率97.41% (稍后开源，这几天有点忙)
