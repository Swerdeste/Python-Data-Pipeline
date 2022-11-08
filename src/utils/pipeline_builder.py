from genpipes import compose


class PipelineBuilder:

    def __init__(self, config):
        self.config = config

    def build(self):
        return compose.Pipeline(self.config)

    def run(self):
        return self.build().run()
