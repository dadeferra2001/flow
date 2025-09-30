from abc import ABCMeta, abstractmethod

class KernelPedestrian(object, metaclass=ABCMeta):
    def __init__(self, master_kernel, sim_params):
        self.master_kernel = master_kernel
        self.kernel_api = None
        self.sim_step = sim_params.sim_step

    def pass_api(self, kernel_api):
        self.kernel_api = kernel_api

    @abstractmethod
    def update(self, reset):
        pass