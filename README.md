## 介绍
1. 使用flask+keras构建一个森林大火识别API
3. 模型构建和训练在first.py中
## 使用方式
1. 启动web_server.py：开启Flask服务器，调用模型，准备接图片
2. 在页面中选择本地图片，获得预测结果
## 注意事项
1. 在flask框架中进行预测 需要将预测语句放在with graph.as_default()中，否则会报错
2. 加载模型语句不要放在app启动语句后，速度会很慢
