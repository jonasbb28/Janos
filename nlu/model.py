import yaml
import numpy as np

data = yaml.safe_load(open("nlu\\train.yml", "r", encoding="utf-8").read())

inputs, outputs = [], []

for command in data["commands"]:
    inputs.append(command["input"].lower())
    outputs.append("{}\{}".format(command["entity"], command["action"]))
    

# Processar texto: palavras, caracteres, bytes, sub-palavras

chars = set()

for input in inputs + outputs:
    for ch in input:
        if ch not in chars:
            chars.add(ch)
        
# Mapear char-idx

char2idx = {}
idx2char = {}

for i, ch in enumerate(chars):
    char2idx[ch] = i
    idx2char[i] = ch

max_seq = max([len(x) for x in inputs])

print(f"Número de chars: {len(chars)}")
print(f"Maior sequência: {max_seq}")

# Criar dataset one-hot (número de exemplos, tamanho da sequencia, número de caracteres) 
# Criar dataset disperso (número de exemplos, tamanho da sequencia)
input_data = np.zeros((len(inputs), max_seq, len(chars)), dtype="int32")

for i, input in enumerate(inputs):
    for k, ch in enumerate(input):
        input_data[i, k, char2idx[ch]] = 1.0
        
print(input_data[0])

# print(inputs)
# print(outputs)