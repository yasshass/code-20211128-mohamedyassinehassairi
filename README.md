### Python BMI Calculator Offline Coding Challenge V7

##### The project structure
 ```
.
├── README.md
├── bmi_calculator
│   ├── __init__.py
│   ├── calculate_bmi.py
│   └── settings.py
├── bmi_calculator.toml
├── data
│   ├── data.json
│   └── output_data.json
├── requirements.txt
├── setup.py
├── .gitignore
├── tests
│   ├── __init__.py
│   └── bmi_calculation.py
└── tox.ini
 ```
#### BMI calculation
In the calculator_bmi module, the following tasks are implemented:
 - read data from json file as a pandas dataframe
 - add a column containing BMI, then a column containing BMI range, then a column containing the associated Health risk
 - display the number of overweight people 
 - save the resulting dataframe in a json file
 
 #### Configuration, tests and build
 - For configuration a settings.py is used with the decouple library to read variables set in an .env file or as environment variables.
 - For tests, unittest is used for unit testing with tox to automate the testing
 - For build, setuptools is used to package the project, exposing a entrypoint 'calculate_bmi'. 
 command to run : JSON_OUTPUT_PATH=<json_output_path> JSON_INPUT_PATH=<json_input_path> python -m bmi_calculator.calculate_bmi. 
 or JSON_OUTPUT_PATH=<json_output_path> JSON_INPUT_PATH=<json_input_path> calculate_bmi
 
