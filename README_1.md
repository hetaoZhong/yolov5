# 本地环境运行

## 本地环境
删除环境，重新激活
E:\work_space\holy\.venv\Scripts\activate
升级python
D:\work_space\holy\.venv\Scripts\python.exe -m pip install --upgrade setuptools wheel -i https://pypi.tuna.tsinghua.edu.cn/simple

## 安装依赖
E:\work_space\holy\venv_cup\Scripts\python.exe -m pip freeze > requirements.txt
不要使用下面的情话源
E:\work_space\holy\venv_cup\Scripts\python.exe -m pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

## 安装 LabelImg
D:\work_space\yolov5\.venv\Scripts\python.exe -m pip install labelImg    
## LabelImg运行参考 https://yi7twv.yuque.com/yi7twv/zvqmrm/ycy70u
D:\work_space\yolov5\.venv\Scripts\labelImg.exe
