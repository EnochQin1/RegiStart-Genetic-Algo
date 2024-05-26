# RegiStartMatchingAlgorithm

## Project Description

The purpose of the RegiStart High-Performance Matching Algorithm is to match organizers to targets.<br>

>Organizer: a student who encourages a target to vote. Organizers are part of a specific subset of the student body.

>Target: a student who is not registered to vote.

Throughout the semester, we experimented with two types of algorithms: a hand-made algorithm that has only one possible output for a given input, and a genetic algorithm that starts out with a number of possible, randomly-generated outputs, and attempts to make these outputs better by mixing outputs together or mutating an output slightly. After thoroughly reviewing and tuning the code for the genetic algorithm, we found that although the genetic algorithm took significantly longer to run, it performed significantly better than the hand-made algorithm. The genetic algorithm achieved an average relationship score of 1.9 for our sample dataset, surpassing the hand-made algorithm's performance, which completed in under 30 seconds but with less effectiveness.

## Project Requirements

Our project uses the PyCharm IDE. The free community version is available at https://www.jetbrains.com/pycharm/.<br><br>
We developed this using Windows 10, but it should work on any Windows, Mac, or Linux machine that meets PyCharm's installation requirements.

### Setup:

1. Install PyCharm.
2. Clone our repository.
3. Right click the "Matching Algorithm PyCharm Project" folder in the repository and open it as a PyCharm Project.
4. Configure the virtual environment.
    1. Click Add Configuration.
    2. Click the "+" button.
    3. Click "Python".
    4. In the "Python Interpreter" field, select a Python interpreter.
    5. Click "OK".
5. Install modules in the virtual enviroment by typing the following commands into the PyCharm terminal.
    1. `pip install numpy`
    2. `pip install pandas`
6. Run the program by right clicking on the main.py file and press "run". This will output a pandas dataframe with the finished matches and will print the average relationship and standard deviation of the algorithm.
