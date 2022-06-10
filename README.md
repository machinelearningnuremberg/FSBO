# FSBO
**Few Shot Bayesian Optimization**
This Repo contains the implementation of [FSBO]() applied to [HPO-B]() benchmark. Please download the data from the benchmark in order to reproduce results.

## Usage

* Train on search space:
`
python fsbo_metatrain.py --space_id 6767

`

* Test on search space and dataset:

`
python fsbo_test.py --space 6767 --dataset_id 31
`



* Aggregate results in a JSON and plot results:

`
python generate_json.py
python fsbo_benchmark_plot.py
`
