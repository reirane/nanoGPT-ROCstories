import torch
import intel_extension_for_pytorch as ipex
...
model = Model()
criterion = ...
optimizer = ...
model.train()
# For Float32
model, optimizer = ipex.optimize(model, optimizer=optimizer)
# For BFloat16
model, optimizer = ipex.optimize(model, optimizer=optimizer, dtype=torch.bfloat16)
# Invoke the code below to enable experimental feature torch.compile
model = torch.compile(model, backend="ipex")
...
optimizer.zero_grad()
output = model(data)
