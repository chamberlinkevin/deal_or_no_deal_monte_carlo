import json, os

class Config:
    """
    This config file reads from config.json and initializes values to be used in a Python environment. 
    """

    def __init__(self):
        """
        Initialize class with variables necessary for simulation parameters.
        """

        if os.getcwd().endswith("libraries") or os.getcwd().endswith("tests"):
            config_path = os.path.abspath(
                os.path.abspath(
                    os.path.join(os.getcwd(), os.pardir, "config.json")
                )
            )
        else:
            config_path = os.path.abspath(
                os.path.join(os.getcwd(), "config.json")
            )

        with open(config_path, "r") as f:
            self.config = json.load(f)

        self.n_trials = self.config.get("n_trials")

        self.l_all_case_values = self.config.get("l_all_case_values")

        self.dict_cases_per_round = self.config.get("dict_cases_per_round")

        self.l_trial_results = []

        self.l_trial_highest_results = []
