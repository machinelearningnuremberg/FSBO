from benchmark_plot import BenchmarkPlotter

if __name__ == "__main__":

    data_path = "hpob-data/"
    results_path = "benchmark_results/"
    output_path = "plots/"
    type_of_spaces = "discrete" #options: discrete, continuous

    if type_of_spaces == "discrete":
        experiments = ["Random", "FSBO", "TST", "DGP", "RGPE" , "BOHAMIANN", "DNGO", "TAF", "GP", "FSBO2"]
    else:
        experiments = ["RS-C", "DGP-C", "GP-C", "FSBO2-C"]

    n_trials = 100

    benchmark_plotter  = BenchmarkPlotter(experiments = experiments, 
                                            name = type_of_spaces+"_benchmark",
                                            n_trials = n_trials,
                                            results_path = results_path, 
                                            output_path = output_path, 
                                            data_path = data_path)

    benchmark_plotter.plot()
    benchmark_plotter.draw_cd_diagram(bo_iter=50, name="Rank@5")
