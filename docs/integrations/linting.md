---
id: linting
title: Linting
---

As part of the build process we run a few linters to catch common programming errors, stylistic errors and possible security issues. Linters are run only when working with the [package (directory) structure](package-dir).

All linters are run via the demisto-sdk:

```
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
  --no-xsoar-linter             Do NOT run XSOAR linter
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

**Note**: this script is also used to run pytest. See: [Unit Testing](unit-testing)

An example of the result for running our lint checks on the HelloWorld package will look like: 
```buildoutcfg
➜  content git:(master) ✗ demisto-sdk lint -i Packs/HelloWorld/Integrations/HelloWorld
Execute lint and test on 1/1 packages
HelloWorld - Facts - Using yaml file /home/sb/dev/demisto/content/Packs/HelloWorld/Integrations/HelloWorld/HelloWorld.yml
HelloWorld - Facts - Pulling docker images, can take up to 1-2 minutes if not exists locally 
HelloWorld - Facts - demisto/python3:3.8.2.6981 - Python 3.8
HelloWorld - Facts - Tests found
HelloWorld - Facts - Lint file /home/sb/dev/demisto/content/Packs/HelloWorld/Integrations/HelloWorld/HelloWorld_test.py
HelloWorld - Facts - Lint file /home/sb/dev/demisto/content/Packs/HelloWorld/Integrations/HelloWorld/HelloWorld.py
HelloWorld - Flake8 - Start
HelloWorld - Flake8 - Successfully finished
HelloWorld - XSOAR Linter - Start
HelloWorld - XSOAR Linter - Successfully finished
HelloWorld - Bandit - Start
HelloWorld - Bandit - Successfully finished
HelloWorld - Mypy - Start
HelloWorld - Mypy - Successfully finished
HelloWorld - Vulture - Start
HelloWorld - Vulture - Successfully finished
HelloWorld - Flake8 - Start
HelloWorld - Flake8 - Successfully finished
HelloWorld - Image create - Trying to pull existing image devtestdemisto/python3:3.8.2.6981-02b43abe979132c89892e089d5b8254d
HelloWorld - Image create - Found existing image devtestdemisto/python3:3.8.2.6981-02b43abe979132c89892e089d5b8254d
HelloWorld - Image create - Copy pack dir to image devtestdemisto/python3:3.8.2.6981-02b43abe979132c89892e089d5b8254d
HelloWorld - Image create - Image sha256:ba9f6ede55 created successfully
HelloWorld - Pylint - Image sha256:ba9f6ede55 - Start
HelloWorld - Pylint - Image sha256:ba9f6ede55 - exit-code: 0
HelloWorld - Pylint - Image sha256:ba9f6ede55 - Successfully finished
HelloWorld - Pytest - Image sha256:ba9f6ede55 - Start
        ============================= test session starts ==============================
        platform linux -- Python 3.8.2, pytest-5.0.1, py-1.8.1, pluggy-0.13.1
        rootdir: /devwork
        plugins: json-0.4.0, forked-1.1.3, mock-2.0.0, asyncio-0.10.0, datadir-ng-1.1.1, requests-mock-1.7.0, xdist-1.31.0
        collected 10 items

        HelloWorld_test.py ..........                                            [100%]

        -------------- generated json report: /devwork/report_pytest.json --------------
        ========================== 10 passed in 0.43 seconds ===========================
HelloWorld - Pytest - Image sha256:ba9f6ede55 - exit-code: 0
HelloWorld - Pytest - Image sha256:ba9f6ede55 - Successfully finished
Flake8       - [PASS]
XSOAR linter - [PASS]
Bandit       - [PASS]
Mypy         - [PASS]
Vulture      - [PASS]
Pytest       - [PASS]
Pylint       - [PASS]
Pwsh analyze - [SKIPPED]
Pwsh test    - [SKIPPED]

Passed Unit-tests:
  - Package: HelloWorld
      - Image: demisto/python3:3.8.2.6981
         - HelloWorld_test.py::test_say_hello
         - HelloWorld_test.py::test_start_scan
         - HelloWorld_test.py::test_status_scan
         - HelloWorld_test.py::test_scan_results
         - HelloWorld_test.py::test_search_alerts
         - HelloWorld_test.py::test_get_alert
         - HelloWorld_test.py::test_update_alert_status
         - HelloWorld_test.py::test_ip
         - HelloWorld_test.py::test_domain
         - HelloWorld_test.py::test_fetch_incidents

#########
 Summary 
#########
Packages: 1
Packages PASS: 1
Packages FAIL: 0
Packages WARNING (can either PASS or FAIL): 0

[INFO] 

############################
 unit-tests coverage report
############################
Name                                                     Stmts   Miss  Cover
----------------------------------------------------------------------------
Packs/HelloWorld/Integrations/HelloWorld/HelloWorld.py     277     83    70%
----------------------------------------------------------------------------
TOTAL                                                      277     83    70%

```

## Flake8

This is a basic linter. It can be run without having all the dependencies available and will catch common errors. We also use this linter to enforce the standard python pep8 formatting style. On rare occasions you may encounter a need to disable an error/warning returned from this linter. Do this by adding an inline comment of the sort on the line you want to disable the error:

```python
#  noqa: <error-id>
```

For example:

```python
example = lambda: 'example'  # noqa: E731
```

When adding an inline comment always also include the error code you are disabling for. That way if there are other errors on the same line they will be reported.

More info: https://flake8.pycqa.org/en/latest/user/violations.html#in-line-ignoring-errors

## Pylint

This linter is similar to flake8 but is able to catch some additional errors. We run this linter with error reporting only. It requires access to dependent modules and thus we run it within a docker image similar with all dependencies (similar to how we run pytest unit tests). On rare occasions you may encounter a need to disable an error/warning returned from this linter. Do this by adding an inline comment of the sort on the line you want to disable the error:

```
# pylint: disable=<error-name>
```

For example:

```python
a, b = ... # pylint: disable=unbalanced-tuple-unpacking
```

Is is also possible to `disable` and then `enable` a block of code. For example (taken from CommonServerPython.py):

```python
# pylint: disable=undefined-variable
if IS_PY3:
    STRING_TYPES = (str, bytes)  # type: ignore
    STRING_OBJ_TYPES = (str)
else:
    STRING_TYPES = (str, unicode)  # type: ignore
    STRING_OBJ_TYPES = STRING_TYPES  # type: ignore
# pylint: enable=undefined-variable
```

**Note**: pylint can take both the error name and error code when doing inline comment disables. It is best to use the name which is clearer to understand.

More info: https://pylint.readthedocs.io/en/latest/user_guide/message-control.html

For classes that generate members dynamically (such as goolgeapi classes) pylint will generate multiple `no-member` errors as it won't be able to detect the members of the class. In this case it is best to add a `.pylintrc` file which will include the following:

```
[TYPECHECK]

ignored-classes=<Class Name List>
```

See following [example](https://github.com/demisto/content/blob/fe2bd5cddc6e521e08ef65fcd456a4214f8c4d93/Integrations/Gmail/.pylintrc)

## Mypy

Mypy uses type annotations to check code for common errors. It contains type information for many popular libraries (via [typeshed project](https://github.com/python/typeshed)). Additionally, it allows you to define type annotations for your own functions and data structures. Type annotations are fully supported as a language feature in python 3.6 and above. In earlier versions type annotations are provided via the use of comments.

We run mypy in a relatively aggressive mode so it type checks also functions which don't contain type definitions. This may sometimes cause extra errors. If you receive errors you can always ignore the line with an inline comment of:

```python
# type: ignore[<error-name>]
```

For example:

```python
a = 1
b = "2"
a = b  # type: ignore[assignment]
```

**Note**: mypy introduced the `ignore[<error-name>]` syntax only in version 0.730. See: [error code docs](https://mypy.readthedocs.io/en/latest/error_codes.html). You may see in the code ignores of the form: `type: ignore` without the `error-name`. This would usually be from old code written before the support for `error-name` ignores. We do not recommend using this ignore style as it ignores all errors and increases the risk of ignoring unexpected serious errors.

Dealing with **_Need type annotation errors_**: If you receive such an error instead of simply adding an `ignore` comment it is better to define the type of the variable which is missing type annotation. This error is usually received when an empty dict or list is defined and mypy can not infer the type of the object. In this case it is better to define the type as `dict` or `list`. For example python 2 code:

```python
my_list = []  # type: list
```

Or with python 3 annotations

```
my_list: list = []
```

If you know the type that the list will hold use the type constructor `List` that can specify also what type it holds. For example a list which we know that will hold strings in python 2 code:

```python
my_list = []  # type: List[str]
```

Or with python 3 annotations

```python
my_list: List[str] = []
```

**Note:** When using type constructors such as `List` or `Dict` there is need to import the type from the typing module in python 3. In python 2 as part of running mypy our wrapper script will include the typing module.

More info at: https://mypy.readthedocs.io/en/latest/index.html

## Bandit

[Bandit](https://github.com/PyCQA/bandit) is a tool designed to find common security issues in Python code.

We run `bandit` with a confidence level of HIGH. In the rare case that it reports a false positive, you can exclude the code by adding a comment of the sort: `# nosec`. See: https://github.com/PyCQA/bandit#exclusions .


## XSOAR Linter

This is a custom linter, based on pylint, whose main purpose is to catch errors regarding Cortex XSOAR code standards. The linter is activated using the pylint load plugins ability. We run this linter only with custom Cortex XSOAR error and warning messages (all other messages are disabled). On rare occasions, you may encounter a scenario in which you need to disable an error or warning message from being returned from by linter. To do this add an inline comment, as shown below, on the line you want to disable the error:

```
# pylint: disable=<error-name>
```

For example:

```python
print('Success!') # pylint: disable=print-exists
```

It is also possible to `disable` and then `enable` a block of code. The following example is taken from CommonServerPython.py:

```python
# pylint: disable=sys-exit-exists
if IS_PY3:
    pass
else:
    sys.exit(1)
# pylint: enable=sys-exit-exists
```

**Note**: Pylint can take both the error name and error code when using an inline comment disable message. Please note, that it is best to use the name which is most clear to understand.
