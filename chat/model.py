import mindspore
from RAG import RAG
from mindnlp.core import no_grad
# from mindnlp.transformers import AutoModelForCausalLM, AutoTokenizer
from mindspore._c_expression import _framework_profiler_step_start
from mindspore._c_expression import _framework_profiler_step_end

# from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig

class chat_model:
    def __init__(self, model_type:str = "Qwen"):
        self.RAG = RAG()
        self.model_type = model_type
        if model_type == 'GLM':
            from mindnlp.transformers import AutoModelForCausalLM, AutoTokenizer
            self.tokenizer = AutoTokenizer.from_pretrained(
                "THUDM/glm-4-9b-chat",
                # trust_remote_code=True,
                local_files_only = True,
                cache_dir = '/data/code1/Mind-Overflow/chat/.mindnlp/',
            )
            print("*****Load Tokenizer Complete*****")
            self.model = AutoModelForCausalLM.from_pretrained(
                "THUDM/glm-4-9b-chat",
                ms_dtype=mindspore.float16,
                cache_dir = '/data/code1/Mind-Overflow/chat/.mindnlp/',
                local_files_only = True,
                # device = 'cuda:0',
                # mirror='modelscope',
                # trust_remote_code=True
            ).to('cuda:0').eval()
            print("*****Load Model Complete*****")
        elif model_type == "Qwen":
            from transformers import AutoModelForCausalLM, AutoTokenizer
            self.tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen-7B-Chat", trust_remote_code=True)
            self.model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B-Chat", device_map="auto", trust_remote_code=True).eval()

    def query(self, question:str, use_RAG:bool):
        if self.model_type == "GLM":
            print("原始提问\n",question)
            question = self.RAG.query(question)
            print("RAG\n",question)
            inputs = self.tokenizer.apply_chat_template(
                [{"role": "user", "content": question}],
                add_generation_prompt=True,
                tokenize=True,
                return_tensors="ms",
                return_dict=True
            )
            gen_kwargs = {"max_length": 100, "do_sample": True, "top_k": 1, "max_new_tokens":300}
            with no_grad():
                outputs = self.model.generate(**inputs, **gen_kwargs)
                outputs = outputs[:, inputs['input_ids'].shape[1]:]
                return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        elif self.model_type == "Qwen":
            # print("原始提问\n",question)
            if use_RAG:
                question = self.RAG.query(question)
                print("RAG\n",question)

            # inputs = self.tokenizer(question, return_tensors='pt')
            # inputs = inputs.to(self.model.device)
            # pred = self.model.generate(**inputs)
            response, history = self.model.chat(self.tokenizer, question, history=None, max_new_tokens=5000)
            return response


    def direct_query(self, question: str):
        inputs = self.tokenizer.apply_chat_template(
            [{"role": "user", "content": question}],
            add_generation_prompt=True,
            tokenize=True,
            return_tensors="ms",
            return_dict=True
        )
        gen_kwargs = {"max_length": 4100, "do_sample": True, "top_k": 1}
        with no_grad():
            outputs = self.model.generate(**inputs, **gen_kwargs)
            outputs = outputs[:, inputs['input_ids'].shape[1]:]
            return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

if __name__ == '__main__':
    model = chat_model()
    print(model.query("如何求解一个矩阵的逆"))
