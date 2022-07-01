

from ray.tune import ExperimentAnalysis
analysis = ExperimentAnalysis(experiment_checkpoint_path="C:/tmp/mypath/fanger_comfort/DQN_None_493ac_00000_0_2022-06-30_15-20-14/result.json")

print(analysis.best_result_df)