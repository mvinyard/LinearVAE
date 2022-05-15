
# import packages #
# --------------- #
import torch


def _get_device(device=0):

    cuda = torch.cuda.is_available()

    if cuda:
        return "cuda:{}".format(device)
    else:
        return "cpu"