import sys
from os.path import abspath, dirname

# Add the parent directory of the current file to sys.path
sys.path.append(abspath(dirname(dirname(__file__))))

import include.gpt as gpt

def create_test_for_module(module_file_path):
    module_file_name = module_file_path.split("/")[-1]
    with open(module_file_path) as module:
        module_text = module.read()

        prompt = f"""
        Perform these steps:
        1) Read the code inside the <code></code> brackets bellow:
        <code>
        {module_text}
        </code>
        2) Understand what it does and how it works. Take your time doing this and do
        not mess up the math.
        3) Create a few (around 5) good tests for this code using PyTest and only PyTest. 
        4) Double check to see if you are creating apropriate tests and that they will
        not fail.

        Remember to start your tests code the line bellow. Do not ommit it.
        from src.tip_calculator import calculate_tip

        Your answer should be just the code, at most some comments on the 
        code for clarity, but without anything else.
        """

        test_code = gpt.get_completion(prompt)
        print(test_code)

    with open("test_"+module_file_name, "w") as test_file:
        test_file.write(test_code)


if __name__ == "__main__":
    create_test_for_module("/home/douglas/code/Python/100DaysOfCode/2Day-100DaysOfPythonGPT-TipCalculator/src/tip_calculator.py")

