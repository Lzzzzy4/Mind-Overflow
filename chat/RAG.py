# from langchain.document_loaders import JSONLoader
from langchain_community.document_loaders import JSONLoader
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.vectorstores import Chroma
import json

class RAG:
    def __init__(self, path:str = "/data/code1/Mind-Overflow/chat/db.json"):
        with open(path) as f:
            temp = json.load(f)
        self.dic = {}
        for i in temp:
            self.dic[i['question']] = i['output']
        loader = JSONLoader(path, jq_schema = '.[].question')
        documents = loader.load()

        model_name = "moka-ai/m3e-base"
        model_kwargs = {'device': 'cuda:0'}
        encode_kwargs = {'normalize_embeddings': True}
        embedding = HuggingFaceBgeEmbeddings(
            model_name=model_name,
            model_kwargs=model_kwargs,
            encode_kwargs=encode_kwargs,
            query_instruction="为文本生成向量表示用于文本检索"
        )
        self.db = Chroma.from_documents(documents, embedding)

    def query(self, question:str):
        context = self.db.similarity_search(question)
        reference = ''
        # for i,ans in enumerate(context):
        #     reference += f"参考提问{i}：\n{ans.page_content}\n\n"
        #     reference += f"参考回答{i}：\n{self.dic[ans.page_content]}\n\n"

        reference += f"参考提问：\n{context[0].page_content}\n\n"
        reference += f"参考回答：\n{self.dic[context[0].page_content]}\n\n"

        prompt = (
            f"我将向你提问，你回答的规则是：若参考信息中存在有效信息，"
            f"必须优先使用参考信息中的内容回复，并结合你的知识稍作润色；"
            f"否则直接用你的知识回答。    "
            f"参考信息：\n{reference}(若引号为空，请忽略） "
            f"我的问题是：{question}   "
            f"务必注意，所有的回答必须使用Markdown格式，不能含有其他格式，请回答的详细些，篇幅长一些。"
            f"如果存在数学计算请给出每一步的具体过程。"
            )   

        return prompt

if __name__ == '__main__':
    t = RAG()
    print(t.query("线性代数"))