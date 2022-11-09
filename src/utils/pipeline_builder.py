from genpipes import compose
import yaml
import importlib
import inspect


class PipelineBuilder:
    """
    A class used to build and run a pipeline using genpipes

    Attributes
    ----------
    steps : list(tuple)
        List of steps to run
    pipe : genpipes.compose.Pipeline
        The pipeline

    Methods
    -------
    build(config_path)
        Build the pipeline from a config file
    run()
        Run the pipeline

    """

    def __init__(self):
        """
        Constructor
        """
        self.pipe = None # Initialize the pipeline
        self.steps = [] # Initialize the steps list

    def build(self, config_path):
        """
        Build the pipeline from a config file

        :param config_path: str
            Path to the config file
            Config file are commonly in yaml format
        :return:
        """
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
        """
        Run the pipeline
        """

        data = self.pipe.run()
        return data
