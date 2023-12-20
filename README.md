
# fine tuning do nanoGPT

Repositório do material de treinamento baseado nos trabalhos de Andrej Karpathy, e GUAN.
Material é parte dos entregáveis da disciplina de GPT: métodos e desafios de modelos de linguagem (IN1165)
Alunos responsáveis por este fork: Bruno Jeronimo e Leilane Cruz

## instalação

```
pip install torch numpy transformers datasets tiktoken wandb tqdm
```

Dependências:

- [pytorch](https://pytorch.org) 
- [numpy](https://numpy.org/install/) 
-  `transformers` for huggingface transformers (to load GPT-2 checkpoints)
-  `datasets` for huggingface datasets  (if you want to download + preprocess OpenWebText)
-  `tiktoken` for OpenAI's fast BPE code 
-  `wandb` for optional logging 
-  `tqdm` for progress bars 

## quick start

Para executar quaisquer dos modelos, acessar link abaixo, realizar o download da pasta e executar o comando destacado no terminal, substituindo "modelcheckpoint" pelo nome da pasta de referência de acordo:

https://drive.google.com/drive/folders/1dVzDmUMWUWEqNZF74rJytJKzhg5_Ycpa?usp=sharing

```
$ python sample.py --out_dir=modelcheckpoint --num_samples=30 --max_new_tokens=150 --top_k=60 --temperature=0.7 --start="Complete the following text within five sentences:[MALE] enjoyed going outside."
```
Parâmetros adicionais: 
Caso deseje alterar o prompt
--start:"Seu prompt aqui" 

As opções de dispositivo por padrão são setadas para CUDA. Caso deseje rodar via CPU ou esteja utilizando um macbook com Chip M1 ou superior, selecionar o correspondente:
--device=cpu 
--device=mps


