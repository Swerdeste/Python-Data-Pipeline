from src.utils.pipeline_builder import PipelineBuilder
from src.utils.ad_hoc import ad_hoc

CONFIG_PATH = "config/pipeline.yaml"

if __name__ == '__main__':
    # Build the pipeline
    pipeline = PipelineBuilder()
    pipeline.build(CONFIG_PATH)

    # Run the pipeline
    pipeline.run()

    # Now we just have to check the output

    # We can also run ad-hoc functions
    print("Les journaux citant le plus de médicaments sont {}".format(ad_hoc("data/target/output.json")))
