import mindspore
from mindnlp.core import no_grad
from mindnlp.transformers import AutoModelForCausalLM, AutoTokenizer
from mindspore._c_expression import _framework_profiler_step_start
from mindspore._c_expression import _framework_profiler_step_end

class chat_model:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("THUDM/glm-4-9b-chat",trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained(
            "THUDM/glm-4-9b-chat",
            ms_dtype=mindspore.float16,
            # mirror='modelscope',
            # trust_remote_code=True
        ).eval()
        print("*****Load Complete*****")

    def query(self, question:str):
        inputs = self.tokenizer.apply_chat_template(
            [{"role": "user", "content": question}],
            add_generation_prompt=True,
            tokenize=True,
            return_tensors="ms",
            return_dict=True
        )
        gen_kwargs = {"max_length": 100, "do_sample": True, "top_k": 1}
        with no_grad():
            outputs = self.model.generate(**inputs, **gen_kwargs)
            outputs = outputs[:, inputs['input_ids'].shape[1]:]
            return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

if __name__ == '__main__':
    model = chat_model()
    print(model.query("你好"))
        
