from ofa.model import OFAModel
from vit.model import VitModel
from abc import abstractmethod


class Generator:
    def do_operation(self, phase, conf):
        if phase == "train":
            data = self._load_data_train(conf)
            return self._train(data)
        else:
            data = self._load_data_eval(conf)
            return self._evaluate(data)

    @abstractmethod
    def _train(self, data):
        pass

    @abstractmethod
    def _evaluate(self, data):
        pass

    @abstractmethod
    def _load_data_train(self, conf):
        pass

    @abstractmethod
    def _load_data_eval(self, conf):
        pass


class VitGenerator(Generator):
    def __init__(self, conf, phase):
        self.model = VitModel()

    def _train(self, data):
        pass

    def _evaluate(self, data):
        pass

    def _load_data_eval(self, conf):
        pass

    def _load_data_train(self, conf):
        pass


class OFAGenerator(Generator):
    def __init__(self, conf, phase):
        self.model = OFAModel()

    def _train(self, data):
        pass

    def _evaluate(self, data):
        pass

    def _load_data_eval(self, conf):
        pass

    def _load_data_train(self, conf):
        pass
