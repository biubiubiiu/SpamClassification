from .base_operation import BaseOperation


class Repeat(BaseOperation):
    def __init__(self, ops, repeat_times):
        super(Repeat, self).__init__()

        if not isinstance(ops, BaseOperation):
            raise ValueError('ops should be subclass of BaseOperation')
        if not isinstance(repeat_times, int) or repeat_times <= 0:
            raise ValueError('repeat times should greater than 1 integer')

        self.ops = ops
        self.repeat_times = repeat_times

    def __call__(self, s):
        ret = s
        for _ in range(self.repeat_times):
            ret = self.ops(ret)
        return ret
