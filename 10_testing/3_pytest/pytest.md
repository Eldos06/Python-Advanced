[[pytest]] [[10_testing/3_pytest/models/user.py|user]] [[10_testing/3_pytest/testing/test_models/test_user.py|test_user]]
[
Markdown

````python
---
tags:
  - python
  - testing
  - pytest
  - coverage
---

# Pytest & Coverage Cheat Sheet

Comprehensive summary of commands, flags, and configuration adjustments based on standard Python advanced testing workflows.

## 🛠️ Installation & Setup

Before running tests, ensure `pytest` and its coverage extension `pytest-cov` are installed in your virtual environment:

```bash
pip install pytest pytest-cov
# Generate requirements file tracking the dependencies
pip freeze > requirements.txt
````

## 🚀 Execution & Coverage Commands

### 1. Basic Execution

Run all tests discovered within the target test suite directory:

Bash

```python
pytest
```

### 2. Basic Coverage Metrics

Measure test coverage targeted specifically at a module folder (e.g., your actual source code folder like `models`):

Bash

```python
pytest --cov=./models
```

> [!WARNING] Avoid Relative Module Paths
> 
> Running `pytest --cov=/.models` with a leading forward slash triggers:
> 
> `CoverageWarning: Module /.models was never imported.`
> 
> Always use `./` or relative syntax (`--cov=models`) to preserve lookups.

### 3. Interactive HTML Coverage Reports

Generate a clean, interactive HTML visual directory to review exact line-by-line misses:

Bash

```python
pytest --cov=./ --cov-report=html:cov-report
```

_This outputs a dedicated folder named `cov-report/`. Open `index.html` inside it to inspect the visual breakdown._

## 🔍 Fine-Tuning Verbosity & Summaries

Use these flags to dictate what information `pytest` prints out on execution.

|**Command Flag**|**Description**|
|---|---|
|`-s`|Disables per-test capturing. Allows `print()` statements to output directly to the terminal during test cycles.|
|`-v`|**Verbose mode**. Explicitly prints each test case name alongside individual `SUBPASSED` parameters.|
|`-r <chars>`|**Reporting modifier**. Controls the "short test summary info" block output behavior.|

### Summary Flag Mixes (`-r`)

- `pytest -s -r fp`: Shows detailed tracking only for **f**ailed and **p**assed tests.
    
- `pytest -s -r fs`: Shows detailed tracking only for **f**ailed and **s**kipped tests (ideal for diagnosing platform mismatches).
    
- `pytest -s -r fps`: Comprehensive tracking across **f**ailed, **p**assed, and **s**kipped tests.
    

## ⚠️ Configuration Warnings Fix

If you encounter the following warning in your console logs:

> `PytestConfigWarning: Unknown config option: testpath`

### Solution

Open your `pytest.ini` configuration file located in the root directory and correct the misspelling. The actual configuration key is plural:

Ini, TOML

```python
[pytest]
# Change 'testpath' to 'testpaths'
testpaths = testing
```



Markdown

````python
---
tags:
  - python
  - testing
  - pytest
  - configuration
---

# Pytest Configuration Notes (`pytest.ini` vs `.coveragerc`)

A breakdown of the project's testing configuration framework, tracking automated flags, coverage omissions, and syntax warnings.

---

## 🛠️ Configuration Analysis

### 1. `pytest.ini` Refusal & Typos
Your current file contains two issues causing configuration warnings:
```ini
[pytest]
addopts = --cov=./ --cov-report=html:cov-report
testpath =
    testinig
````

- **The `testpath` Warning:** Pytest natively expects the plural key `testpaths`. Using the singular form triggers the console error: `PytestConfigWarning: Unknown config option: testpath`.
    
- **The Directory Typo:** Your folder is physically named `testing`, but the configuration path is misspelled as `testinig`.
    

#### 🔄 Optimized `pytest.ini`

Update the file to this clean, automated state:

Ini, TOML

```python
[pytest]
# Automatically applies coverage metrics and dumps visual HTML reports on every raw 'pytest' execution
addopts = --cov=./ --cov-report=html:cov-report

# Specifies the target directory for test discovery (fixed typo and changed to plural)
testpaths = 
    testing
```

## 🚫 Coverage Omissions (`.coveragerc`)

Your tracking file tells the `coverage` engine what files to ignore when calculating percentages:

Ini, TOML

```javascript
[run]
omit = testing/*
```

### 💡 Why this is important for your project:

1. **Separates Source from Tests:** By omitting `testing/*`, your overall coverage metrics reflect only your _actual_ application logic (e.g., your `models/user.py` file).
    
2. **Prevents Inflated Metrics:** Assertions and test setups inside test files will always run at virtually 100% execution. Leaving them out ensures your metrics reflect true code health.
    

## 📈 Combined Architecture Lifecycle

When you run the simple `pytest` command in your terminal, the internal workflow maps out as follows:

```javascript
[Command: pytest]
       │
       ▼
┌────────────────────────────────────────┐
│ 1. Reads pytest.ini                    │
│    • Injects: --cov=./                 │
│    • Injects: --cov-report=html        │
│    • Targets: testing/ folder          │
└──────────────┬─────────────────────────┘
               │
               ▼
┌────────────────────────────────────────┐
│ 2. Reads .coveragerc                   │
│    • Ignores execution paths inside    │
│      the testing/ module directory     │
└──────────────┬─────────────────────────┘
               │
               ▼
┌────────────────────────────────────────┐
│ 3. Generates Output                    │
│    • Compares models/ execution        │
│    • Compiles raw data into HTML       │
│    • Spits report out to /cov-report   │
└────────────────────────────────────────┘
```

## 🚀 Pro-Tips for Obsidian Linking

- Use `[[cov-report/index.html]]` inside your daily logs to quickly link out to your generated browser reports.
    
- If you start tracking third-party APIs or migrations later, simply add them underneath your omission configuration block:
    
    Ini, TOML
    
    ```python
    [run]
    omit = 
        testing/*
        migrations/*
    ```