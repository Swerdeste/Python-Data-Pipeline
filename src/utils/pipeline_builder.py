from genpipes import compose
import yaml
import importlib
import inspect


class PipelineBuilder:

    def __init__(self):
        self.pipe = None
        self.steps = []
    def build(self, config_path):
        with open(config_path) as f:
            steps = yaml.safe_load(f)
        for step in steps:
            step_name = step['step-name']
            del step['step-name']
            step_path = step['filepath']
            del step['filepath']
            step_job = getattr(importlib.import_module(step_path), step_name)
            step_description = inspect.getdoc(step_job)

            step_config = step

            self.steps.append(
                (
                    step_description,
                    step_job,
                    step_config
                )
            )
        self.pipe = compose.Pipeline(steps=self.steps)

        return compose.Pipeline(step)

    def run(self):
        data = self.pipe.run()
        return data
