import json
import pandas as pd
import os

experiment_id = "FSBO2"
seeds = ["test0", "test1", "test2", "test3", "test4"]
results_path = "results/"


results = {}
for seed in seeds:
    
    space_path = os.path.join(results_path,seed,experiment_id)
    space_list = os.listdir(space_path)
    
    for space in space_list:
        if space not in results.keys(): results[space] = {}
            
        files = os.listdir(os.path.join(space_path,space))
        
        for file in files:
            data = pd.read_csv(os.path.join(space_path, space, file))
            task = file.split(".")[0]
            
            if task not in results[space].keys(): results[space][task] = {}
            
            temp_results = data.regret.values.tolist()
            
            temp_results += [0]*(101-len(temp_results))
            temp_results = [1-x for x in temp_results]
            results[space][task][seed] = temp_results


with open(f"benchmark_results/{experiment_id}.json", "w") as f:
    json.dump(results, f)