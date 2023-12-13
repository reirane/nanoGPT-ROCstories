import time

out_dir = 'out-commonsense-finetune-lrdecay-gradient16-batch16-3e-4'
eval_interval = 5
eval_iters = 40
wandb_log = True # feel free to turn on
wandb_project = 'commonsense-gpt2-lrdecay-gradient16-batch16-3e-4'
wandb_run_name = 'ft-' + str(time.time())

dataset = 'commonsense-gpt'
init_from = 'gpt2' # this is the largest GPT-2 model

# only save checkpoints if the validation loss improves
always_save_checkpoint = False

# the number of examples per iter:
# 1 batch_size * 32 grad_accum * 1024 tokens = 32,768 tokens/iter
# shakespeare has 301,966 tokens, so 1 epoch ~= 9.2 iters
batch_size = 16
gradient_accumulation_steps = 16
max_iters = 28


# finetune at constant LR
learning_rate = 3e-4
decay_lr = True
lr_decay_iters = 28
