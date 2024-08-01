from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# model_name = "shailja/fine-tuned-codegen-2B-Verilog"  # Replace with your fine-tuned model name
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForCausalLM.from_pretrained(model_name).to(device)


def predict(input):
    return input
# def predict(input):
#         # Tokenize the input text
#         input_ids = tokenizer.encode(input, return_tensors="pt").to(device)
        
#         # Generate the response
#         sample_outputs = model.generate(input_ids, 
#                                         max_length=128, 
#                                         do_sample=True, 
#                                         top_k=50, 
#                                         top_p=0.95, 
#                                         temperature=0.7,
#                                         num_return_sequences=1)

#         # Decode the generated text
#         generated_text = tokenizer.decode(sample_outputs[0], skip_special_tokens=True)
#         return generated_text
