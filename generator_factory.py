from generator import OFAGenerator


class PromptGeneratorFactory:
    method = None

    def initialize(self, method, conf, phase):
        self.method = self._get_method(method)
        return self.method(conf, phase)

    @staticmethod
    def _get_method(method):
        if method == 'ofa':
            return OFAGenerator
