import re
from .answer_accurate_grammar import answer_accurate_grammar
from llama_cpp import Llama
from .constants import LOGICAL_MODEL

# Run this to check if your tokens per second are good, and your GPU is working. Libraries update frequently and sometimes they break.

def sanity_check(logic_llm):
    retries = 0
    while (retries <= 4):
        decision_prompt = f"""Hi there, """
        # print("DEBUG\n\n" + decision_prompt)
        completion = logic_llm(decision_prompt, max_tokens=100, stop=["</s>","# Input:"], echo=True,grammar=answer_accurate_grammar,temperature=0.2)["choices"][0]["text"]
        # print(completion)

        return
            
            
if __name__ == "__main__": # test
    logic_llm = Llama(model_path=LOGICAL_MODEL,n_gqa=8,offload_kqv=True,n_ctx=8000,n_gpu_layers=1000,rope_freq_scale=0.33,rope_scaling_type=1) # load the logical LLM and offload everything
    
    
    
    d = sanity_check(logic_llm)
    print(d)
    