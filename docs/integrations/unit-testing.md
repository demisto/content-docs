---
id: unit-testing
title: Unit Testing
---

Unit testing should be used to test small units of code in an isolated and deterministic fashion. Unit tests should avoid performing communication with external APIs and should prefer to use mocking. Testing actual interaction with external APIs should be performed via [Test Playbooks](test-playbooks). Unit testing is currently supported for Python and PowerShell (no JS). This doc outlines Python setup. For PowerShell see [here](powershell-code).

## Environment Setup

In order to work with unit testing, the integration or automation script needs to be developed in [package (directory) structure](package-dir), where the yml file is separated from the python file and resides in its own directory.

### Setup Pipenv

To run locally the unit tests we want to setup a virtual environment with all required dependencies (both runtime and development). To achieve this we use [Pipenv](https://pipenv.readthedocs.io/en/latest/).

Our recommended way to setup an integration into the [package (directory) structure](package-dir) is to use: `demisto-sdk split`. See full command documentation [here](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/split/README.md).

Manual Setup:

* **Install pipenv**: Follow the [instructions](https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv).
* **Copy base Pipenv files**: Copy the base Pipfile and Pipfile.lock files to the target package directory from: [demisto_sdk/commands/lint/resources](https://github.com/demisto/demisto-sdk/tree/master/demisto_sdk/commands/lint/resources).
* **Install additional runtime dependencies**: using: `pipenv install <dependency>`. For example: `pipenv install ldap3`
* **Sync Pipenv**: (including dev dependencies) by running: `pipenv sync --dev`
* **Enable Virtual Env**: To enable the Pipenv virtual env in the shell run: `pipenv shell`. To exit the virtual env simply run: `exit`.

You should now have a managed virtual environment to run unit tests locally.

### Setup Vscode

We recommend using VSCode with the Cortex XSOAR Extension This is optional and you can also run/debug unit tests with other IDEs (such as Pycharm).

Setup:

* **Install the Cortex XSOAR Extension**: Install with-in VSCode by navigating to `Extension`. Or download and install from [here](https://marketplace.visualstudio.com/items?itemName=CortexXSOARext.xsoar)
* **Open VSCode**: Open VSCode where the root folder is the folder you wish to develop within.
* **Choose Interpreter**: Choose the Pipenv interpreter (with all dependencies we setup in the previous step). See: <https://code.visualstudio.com/docs/python/environments>
* **Enable PyTest**: We run our unit tests with `pytest`. See the following on how to enable PyTest: <https://code.visualstudio.com/docs/python/testing>

### Setup PyCharm

* **Install the Cortex XSOAR Plugin**: Install with-in PyCharm by navigating to `Preferences.. -> Plugins`. Or download and install from [here](https://plugins.jetbrains.com/plugin/12093-demisto-add-on-for-pycharm)
* **Open Pycharm**: Open PyCharm where the root folder is the folder you wish to develop within.
* **Choose Interpreter**: Choose the Pipenv interpreter (with all dependencies we setup in the previous step). See: <https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html>
* **Enable PyTest**: We run our unit tests with `pytest`. See the following on how to enable PyTest: <https://www.jetbrains.com/help/pycharm/pytest.html>

## Use `main` in Integration/Automation

When writing unit tests you will import the Integration/Automation file in order to test specific files. Thus, there is need to make sure that the file is written in such a way that when importing it will not execute. This can be done with a simple `main` function which is called depending on how the file was executed. When the Integration/Automation script is called by Cortex XSOAR it will have the property `__name__` set to either `__builtin__` or `builtins` depending upon the python version. Adding the following code will ensure the script is not run when imported by the unit tests:

```python
# python2 uses __builtin__ python3 uses builtins
if __name__ == "__builtin__" or __name__ == "builtins":
    main()
```

## Write Your Unit Tests

Unit tests should be written in a separate Python file named: `<your_choice>_test.py`. Within the unit test file, each unit test function should be named: `test_<your name>`. More information on writing unit tests and their format is available at the [PyTest Docs](https://docs.pytest.org/en/latest/contents.html). Good place to see example unit tests: [Proofpoint TAP v2 integration](https://github.com/demisto/content/blob/master/Packs/ProofpointTAP/Integrations/ProofpointTAP_v2/ProofpointTAP_v2_test.py)

### Mocking

We use [pytest-mock](https://github.com/pytest-dev/pytest-mock/) for mocking. `pytest-mock` is enabled by default and installed in the base environment mentioned above. To use a `mocker` object, simply pass it as a parameter to your test function. The `mocker` can then be used to mock both the demisto object and also external APIs. An example of using a `mocker` object is available [here](https://github.com/demisto/content/blob/master/Packs/CommonScripts/Scripts/ParseEmailFiles/ParseEmailFiles_test.py).

## Running Your Unit Tests

### Command Line

To run your unit tests from the command line simply run from within the virtual env:

```bash
pytest -v
```

Sample run:
![code sample](../doc_imgs/integrations/unit-test-sample-run.png)

It is also possible to run from outside the virtual env by running:

```bash
pipenv run pytest -v
```

### Run with PyCharm

Open the unit test file within PyCharm. You will see a green arrow next to each unit test function. When pressing the arrow you will get a prompt to either Debug or Run the unit test. Set breakpoints as needed and Debug the test.

Sample clip of debugging in PyCharm:

![debug test](../doc_imgs/integrations/Unit-Testing-Debug.gif)

### Run With Docker

CircleCI build will run the unit tests within the docker image the Integration/Automation will run with. To test and
run locally the same way CircleCI runs the tests, run the `demisto-sdk lint` command  

Run the script with `-h` to see command line options:

```log
demisto-sdk lint -h
Usage: demisto-sdk lint [OPTIONS]

  Lint command will perform:

      1. Package in host checks - flake8, bandit, mypy, vulture.

      2. Package in docker image checks -  pylint, pytest, powershell - test, powershell -
      analyze.

  Meant to be used with integrations/scripts that use the folder (package) structure. Will
  lookup up what docker image to use and will setup the dev dependencies and file in the target
  folder.

Options:
  -h, --help                    Show this message and exit.
  -i, --input PATH              Specify directory of integration/script
  -g, --git                     Will run only on changed packages
  -a, --all-packs               Run lint on all directories in content repo
  -v, --verbose                 Verbosity level -v / -vv / .. / -vvv  [default: 2]
  -q, --quiet                   Quiet output, only output results in the end
  -p, --parallel INTEGER RANGE  Run tests in parallel  [default: 1]
  --no-flake8                   Do NOT run flake8 linter
  --no-bandit                   Do NOT run bandit linter
  --no-mypy                     Do NOT run mypy static type checking
  --no-vulture                  Do NOT run vulture linter
  --no-pylint                   Do NOT run pylint linter
  --no-test                     Do NOT test (skip pytest)
  --no-pwsh-analyze             Do NOT run powershell analyze
  --no-pwsh-test                Do NOT run powershell test
  -kc, --keep-container         Keep the test container
  --test-xml PATH               Path to store pytest xml results
  --failure-report PATH         Path to store failed packs report
  -lp, --log-path PATH          Path to store all levels of logs
  --no-coverage                 Do NOT run coverage report.
  --coverage-report PATH        Specify directory for the coverage report files
```

Sample output:

![sample output](../doc_imgs/integrations/unit-test-sample-output.png)

## Common Unit Testing Use Cases

### Multi variables assertion

Most functions we write have several edge cases. When writing a unit test for this type of function all edge cases need to be tested.
For example let's examine the following python function:

```python
def convert_string_to_type(string: str) -> Union[str, bool, int]:
    """
    Converts the input string to it's object type
    :param string: The input string
    :return: The converted object
    """
    if string.isnumeric():
        return int(string)
    elif string in ['true', 'false', 'True', 'False']:
        return bool(string)
    return string
```

A naive unit test will be as follows:

```python
def test_convert_string_to_type():
    from File import convert_string_to_type
    string = 'true'
    assert convert_string_to_type(string) == True
    
    string = '432'
    assert convert_string_to_type(string) == 432

    string = 'str'
    assert convert_string_to_type(string) == 'str'
```

The correct way to test this function is using the @pytest.mark.parametrize fixture:

```python
@pytest.mark.parametrize('string, output', [('true', True), ('432', 432), ('str', 'str')])
def test_convert_string_to_type(string, output):
    assert convert_string_to_type(string) == output
```

We declare the inputs and outputs in the following format: 'input, output', [(case1_input, case1_output), (case2_input, case2_output), ...]
(Note that more than two variables can be delivered)

After declaring the variables and assigning their values, you need to assign the variables to the test function. In the example above we assign the variables 'string' and 'output' to the test function.

To read more on parametrize fixtures, visit: <https://docs.pytest.org/en/latest/how-to/parametrize.html>

An example of a test using the paramertrize fixture is avialable [here](https://github.com/demisto/content/blob/master/Packs/CommonScripts/Scripts/ExtractDomainFromUrlFormat/ExtractDomainFromUrlFormat_test.py#L7).

### Testing Exceptions

If a function is raising an exception in some case we want to test the right exception is raised and that the error message is correct.
For example, for testing the following function:

```python
def function():
    raise ValueError('this is an error msg')
```

We first need to import the raises function from pytest using this line of code:

```python
from pytest import raises
```

Then, we test the exception being raised.

```python
def test_function():
    from File import function
    with raises(ValueError, match='this is an error msg'):
        function()
```

If the function raises a ValueError with proper error message, the test will pass.

## Troubleshooting Tips

* The `demisto-sdk lint` by default prints out minimal output. If for some reason it is failing and not clear, run the
script with `-v` for verbose output.

* When running mypy against python 2 code and the file contains non-ascii characters it may fail with an error of the sort:
  
  `can't decode file 'ThreatConnect.py': 'ascii' codec can't decode byte 0xe2 in position 47329: ordinal not in range(128)`.
  
  To find the character use the following python one liner:
  
  `python -c "index = 47329; f = open('Integrations/ThreatConnect/ThreatConnect.py'); d = f.read(); print(d[index-20:index+20])"`
  
* The script creates a container image which is used to run pytest and pylint. The container image will be named: `devtest<origin-image>-[deps hash]`. For example: `devtestdemisto/python:1.3-alpine-1b9f5bee16a24c3f5463e324c1bb075`. You can examine the image if needed by simple using docker run. For example:

```bash
docker run --rm -it devtestdemisto/python:1.3-alpine-1b9f5bee16a24c3f5463e324c1bb075e sh
```

If you have faced the error `ValueError: unknown locale: UTF-8` when running `demisto-sdk lint`, add these lines to your ~/.bash_profile:  

```bash
export LC_ALL=en_US.UTF-8 
export LANG=en_US.UTF-8
```
