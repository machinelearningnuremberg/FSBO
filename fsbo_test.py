import numpy as np
from hpob_handler import HPOBHandler
from fsbo_modules import DeepKernelGP
import os 
import argparse
import pandas as pd


def main(args):

    randomInitializer = np.random.RandomState(0) 
    search_space_id =  args.space_id
    dataset_id = args.dataset_id
    seed  = args.seed
    n_trials = args.n_trials
    experiment_id = args.experiment_id
    load_model = True #if load_Model == False the DeepKernel is randomly initialized 
    verbose = False

    torch_seed = randomInitializer.randint(0,100000)

    rootdir = os.path.dirname(os.path.realpath(__file__))
    log_dir = os.path.join(rootdir,"logs",seed, experiment_id, search_space_id)
    save_dir = os.path.join(rootdir,"results", seed, experiment_id, search_space_id)
    
    hpob_hdlr = HPOBHandler(root_dir=rootdir+"/hpob-data/", mode="v3-test")
    dim = hpob_hdlr.get_search_space_dim(search_space_id)

    os.makedirs(log_dir,exist_ok=True)
    os.makedirs(save_dir,exist_ok=True)

    log_dir = os.path.join(log_dir, f"{dataset_id}.txt")
    save_dir = os.path.join(save_dir, f"{dataset_id}.csv")

    #loads pretran model from the checkpoint "FSBO",
    checkpoint = os.path.join(rootdir,"checkpoints",experiment_id, f"{search_space_id}")

    #define the DeepKernelGP as HPO method
    method = DeepKernelGP(dim, log_dir, torch_seed, epochs= 100, load_model = load_model, 
                                            checkpoint = checkpoint, verbose = verbose)

    #evaluate the HPO method
    acc = hpob_hdlr.evaluate(method, search_space_id = search_space_id, 
                                            dataset_id = dataset_id,
                                            seed = seed,
                                            n_trials = n_trials )

    regret = [1-x for x in acc]

    pd.DataFrame({"regret": regret}).to_csv(save_dir)

            

if __name__ == "__main__":


    parser = argparse.ArgumentParser()
    parser.add_argument("--space_id", type=str, default="4796")
    parser.add_argument("--dataset_id", type=str, default="3549")
    parser.add_argument("--seed", type=str, default="test1")
    parser.add_argument("--n_trials", type=int, default=20)
    parser.add_argument("--experiment_id", type=str, default="FSBO")

    args = parser.parse_args()
    main(args)