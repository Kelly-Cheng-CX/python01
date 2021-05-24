import yaml


# 读取YAML
# 加载配置项
with open('python01.yaml',encoding='utf-8') as f:     # 先打开文件
    data = yaml.load(f.read(), Loader=yaml.FullLoader)  # 全量加载
print(data)
