from src.utils.pipeline_builder import PipelineBuilder

CONFIG_PATH = "config/pipeline.yaml"


if __name__ == '__main__':
    # Build the pipeline
    pipeline = PipelineBuilder()
    pipeline.build(CONFIG_PATH)

    # Run the pipeline
    pipeline.run()

    # Now we just have to check the output
