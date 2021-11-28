from setuptools import setup

setup(
    name='bmi_calculator',
    version='0.0.1',
    packages=['bmi_calculator'],
    install_requires=[
        'python-decouple==3.5',
        'pandas==1.3.4',
    ],
    entry_points={
        "console_scripts": [
            "calculate_bmi = bmi_calculator.calculate_bmi:main"
        ]
    },
)