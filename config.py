# encoding: utf-8
import warnings
import numpy as np


class DefaultConfig(object):
    seed = 0

    # dataset options
    dataset = 'market1501'
    datatype = 'person'
    mode = 'retrieval'
    # optimization options
    loss = 'triplet'
    optim = 'adam'
    max_epoch = 400
    train_batch = 32 
    test_batch = 32
    adjust_lr = False
    lr = 0.0001
    gamma = 0.1
    weight_decay = 5e-4
    momentum = 0.9
    random_crop = False
    margin = None
    num_gpu = 1
    evaluate = False
    savefig = None 
    re_ranking = False


    #for self training
    lambda_value = 0.1
    num_instances = 4
    tgt_dataset = 'market1501'
    rho = 1.6e-3
    selftrain_iterations = 30


    #for AlignedReid
    htri_only = None
    test_distance = 'global'


    # model options
    model_name = 'bfe'  # triplet, softmax_triplet, bfe, ide
    last_stride = 1
    pretrained_model = None
    
    # miscs
    print_freq = 30
    eval_step = 50
    save_dir = './pytorch-ckpt/market'
    workers = 0
    start_epoch = 0
    best_rank = -np.inf

    def _parse(self, kwargs):
        for k, v in kwargs.items():
            if not hasattr(self, k):
                warnings.warn("Warning: opt has not attribut %s" % k)
            setattr(self, k, v)
            if 'cls' in self.dataset:
                self.mode='class'
            if 'market' in self.dataset or 'cuhk' in self.dataset or 'duke' in self.dataset:
                self.datatype = 'person'
            elif 'cub' in self.dataset:
                self.datatype = 'cub'
            elif 'car' in self.dataset:
                self.datatype = 'car'
            elif 'clothes' in self.dataset:
                self.datatype = 'clothes'
            elif 'product' in self.dataset:
                self.datatype = 'product'

    def _state_dict(self):
        return {k: getattr(self, k) for k, _ in DefaultConfig.__dict__.items()
                if not k.startswith('_')}

opt = DefaultConfig()
