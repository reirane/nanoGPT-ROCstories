import time

out_dir = 'out-commonsense-finetune-learning_rate_2_5'
eval_interval = 5
eval_iters = 40
wandb_log = True # feel free to turn on
wandb_project = 'commonsense-gpt2-learning_rate_2_5'
wandb_run_name = 'ft-' + str(time.time())

dataset = 'commonsense-gpt'
init_from = 'gpt2' # this is the largest GPT-2 model

# only save checkpoints if the validation loss improves
always_save_checkpoint = False

# the number of examples per iter:
# 1 batch_size * 32 grad_accum * 1024 tokens = 32,768 tokens/iter
# shakespeare has 301,966 tokens, so 1 epoch ~= 9.2 iters
batch_size = 12
gradient_accumulation_steps = 32
max_iters = 38

# finetune at constant LR
learning_rate = 2.5e-5
dropout = 0.0
decay_lr = False
