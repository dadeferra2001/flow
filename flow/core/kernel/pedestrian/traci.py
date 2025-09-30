from flow.core.kernel.pedestrian.base import KernelPedestrian

class TraCIPedestrian(KernelPedestrian):
    def __init__(self, master_kernel, sim_params):
        KernelPedestrian.__init__(self, master_kernel, sim_params)

    def initialize(self, pedestrians):
        pass

    def update(self, reset):
        pass