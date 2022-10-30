
import torch

x_uni_randn=torch.randn(2,3)
print('x_rand:{0}\n{1}'.format(x_uni_randn.type(),x_uni_randn))
print('mean:\n',x_uni_randn.mean())