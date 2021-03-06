from abc import abstractmethod


class BaseModel:
    _subclass_basename = ''

    @property
    def name(self):
        return self._subclass_basename[:-3]

    @abstractmethod
    def init_subclass_basename(self):
        pass

    def __call__(self, *args, **kwargs):
        self.init_subclass_basename()
        return self.name
