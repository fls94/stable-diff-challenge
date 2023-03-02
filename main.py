import argparse
from utils import load_config
from generator_factory import PromptGeneratorFactory


parser = argparse.ArgumentParser()
parser.add_argument('--conf_path', type=str, default='conf.json')
parser.add_argument('--phase', type=str, default='train')
parser.add_argument('--method', type=str, default='ofa')
args = parser.parse_args()
conf = load_config(args.conf_path)

method = args.method
phase = args.phase
factory = PromptGeneratorFactory()
print(factory.method)
prompt_generator = factory.initialize(method, conf, phase)
print(factory.method)
result = prompt_generator.do_operation(phase, conf)
print(result)
