from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import json
import requests

app = Flask(__name__)
CORS(app)

# 假设知识库是一个简单的JSON文件
with open('knowledge_base.json', 'r', encoding='utf-8') as f:
    knowledge_base = json.load(f)

# 调用外部API并处理响应
def call_external_api(prompt):
    url = 'http://localhost:11434/api/generate'
    payload = {
        "model": "qwen2:7b",
        "prompt": prompt
    }
    response = requests.post(url, json=payload, stream=True)  # 使用流式请求
    combined_response = ''

    # 逐块读取响应
    for line in response.iter_lines():
        if line:
            try:
                json_data = json.loads(line.decode('utf-8'))
                if 'response' in json_data:
                    combined_response += json_data['response']
                if json_data.get('done'):
                    break
            except json.JSONDecodeError as e:
                print("JSON Decode Error:", e)
                return "外部API响应格式错误"

    return combined_response

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    query = request.json['query']

    # 检索相关文档
    relevant_docs = [doc for doc in knowledge_base if query in doc['content']]
    context = ' '.join([doc['content'] for doc in relevant_docs])

    # 构造生成模型的提示
    # prompt = f"基于以下内容：{context}，你的问题'{query}'的答案是："
    prompt = (f"我将向你提问，你回答的规则是：若参考信息中存在有效信息，"
              f"必须优先使用参考信息中的内容回复，并结合你的知识稍作润色；"
              f"否则直接用你的知识回答。    "
              f"参考信息：'{context}'(若引号为空，请忽略） "
              f"我的问题是：{query}   "
              f"务必注意，所有的回答必须使用Markdown格式，不能含有其他格式。")
    # print(prompt)

    # 调用外部API生成回答
    answer = call_external_api(prompt)

    ret = jsonify({'answer': answer})
    print(json.dumps({'answer': answer}, ensure_ascii=False, indent=4))
    return ret

if __name__ == '__main__':
    app.run()
