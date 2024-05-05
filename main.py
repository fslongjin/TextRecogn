from fastapi import FastAPI, UploadFile,File
from utils import *
import uvicorn
from transformers import AutoConfig, AutoModelForSequenceClassification, AutoTokenizer
import torch
from aigc_check_fun import aigc_check  

model_path = "model/"  # 替换为模型文件所在的路径
device = None
config = None
model = None
tokenizer = None

app = FastAPI()
def setup_global_variables():
    global device
    global config
    global model
    global tokenizer

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    config = AutoConfig.from_pretrained(model_path)
    model = AutoModelForSequenceClassification.from_pretrained(model_path, config=config)
    tokenizer = AutoTokenizer.from_pretrained(model_path)

app=FastAPI()

@app.post("/ai_check")
async def ai_check(file: UploadFile=File(...)):
    return await aigc_check(file,device,model,tokenizer)

# 运行FastAPI应用程序
if __name__ == '__main__':
    setup_global_variables()
    uvicorn.run(app, host='0.0.0.0', port=8000, log_level="debug", workers=1)

    