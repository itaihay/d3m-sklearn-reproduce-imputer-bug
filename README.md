This code reproduces a bug with the `d3m.primitives.data_cleaning.imputer.SKlearn` primitive.

### What is the bug
The imputer does not save a reference to imputed columns during training. When predicting it can impute different columns and produce a bug.
The error is in step 5 of the pipeline, which is the primitive `d3m.primitives.data_cleaning.imputer.SKlearn`.

The error message can be shown if run in debug mode, with a breakpoint in `d3m/runtime.py` in line **1078**.
It states:
> X has 11 features per sample, expected 12

### When does the bug occur?
When predicting on a dataset object with missing values.

### How to run
1. Use the image `registry.gitlab.com/datadrivendiscovery/images/primitives:ubuntu-bionic-python36-stable`

2. Run  the file `runpipeline.py`

### How did we reproduce
1. Fitted on the full dataset
2. Took a few rows and omitted data from a single column, so that it would be with null values
3. Tried to predict on the rows we took

The prediction task does work properly on data without missing values. 