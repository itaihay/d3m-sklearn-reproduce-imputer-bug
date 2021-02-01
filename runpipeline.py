import os

from d3m.container.dataset import Dataset, D3MDatasetLoader
from d3m.metadata import base as metadata_base, pipeline as pipeline_module, problem
from d3m.runtime import Runtime
from d3m import index

problem_path = 'problem1/problemDoc.json'
dataset_train_path = 'problem1/train/datasetDoc.json'
dataset_predict_path = 'problem1/predict/datasetDoc.json'
pipeline_path = 'pipeline.json'

# Loading problem description.
problem_description = problem.parse_problem_description(problem_path)

# Loading dataset.
path = 'file://{uri}'.format(uri=os.path.abspath(dataset_train_path))
dataset = D3MDatasetLoader().load(dataset_uri=path)

path2 = 'file://{uri}'.format(uri=os.path.abspath(dataset_predict_path))
dataset_predict = D3MDatasetLoader().load(dataset_uri=path2)

# Loading pipeline description file.
with open(pipeline_path, 'r') as file:
    pipeline_description = pipeline_module.Pipeline.from_json(string_or_file=file)

# Creating an instance on runtime with pipeline description and problem description.
runtime = Runtime(pipeline=pipeline_description,
                  problem_description=problem_description,
                  context=metadata_base.Context.TESTING)

# Fitting pipeline on input dataset.
fit_results = runtime.fit(inputs=[dataset])
fit_results.check_success()

# Producing results using the fitted pipeline.
produce_results = runtime.produce(inputs=[dataset_predict])
produce_results.check_success()

print(produce_results.values)
