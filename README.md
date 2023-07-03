# ailola app

[![PyPI](https://img.shields.io/pypi/v/ailola.svg)](https://pypi.org/project/ailola/)

https://github.com/lola-pola/ailola/actions/workflows/dependabot/badge.svg



![build status]([https://github.com/github/docs/actions/workflows/dependabot.yml/badge.svg](https://github.com/lola-pola/ailola/actions/workflows/python-publish.yml/badge.svg))

![build status]([https://github.com/github/docs/actions/workflows/main.yml/badge.svg](https://github.com/lola-pola/ailola/actions/workflows/python-publish/badge.svg))


This is a Python command-line application that utilizes OpenAI's Chat API to generate and validate Terraform HCL (HashiCorp Configuration Language) templates. It provides two main functionalities:

Terraform HCL Generation: Given a query, the application generates valid Terraform HCL templates. It can generate templates with or without provider information, depending on the specified provider.

Terraform HCL Validation: The application can validate existing Terraform templates and suggest security changes and Terraform-specific modifications.

Prerequisites
Before running the application, make sure you have the following dependencies installed:



## Demo
[![asciicast](https://asciinema.org/a/lOGRRZVrs0OracrtxkOLtnP9K.svg)](https://asciinema.org/a/lOGRRZVrs0OracrtxkOLtnP9K)

```
pip install ailola 
```


Python (version 3.8 or above)
openai Python library
click Python library
colorama Python library
You also need to set up an OpenAI API key and set the necessary environment variables:

OPENAI_API_KEY: Your OpenAI API key
OPENAI_ENGINE: The OpenAI GPT-3.5 engine to use
OPENAI_API_BASE: (Optional) The base URL for the OpenAI API (if using Azure API endpoint)

## Installation
Clone this repository to your local machine:


```
$ git clone https://github.com/lola-pola/ailola.git
$ cd ailola
```
Install the required Python dependencies using pip:

```
$ pip install -r requirements.txt
```

Set the environment variables mentioned in the Prerequisites section.

## Usage
The application provides a command-line interface with the following options:

```
$ python ailola.py --data <query> --validate <template_file> --provider <provider> --temperature <temperature>
--data: The query used to generate the Terraform HCL template.
--validate: (Optional) Path to an existing Terraform template file for validation.
--provider: (Required) The provider to use, either "azure" or any other provider.
--temperature: (Optional) The temperature for generating or validating the template (default: 1).
```
## Examples
Generate a Terraform HCL template:

```
$ python app.py --data "Create a virtual machine"
```
Validate a Terraform template:


```
$ python app.py --validate path/to/template.tf --provider azure
```

Note: Make sure to replace path/to/template.tf with the actual path to your Terraform template file.

## Output
The application will output the generated or validated Terraform HCL template in the console. The output will be color-coded for better visibility:

## Generated template: Blue
Validation result: Yellow
Make sure to review the output and use it accordingly in your Terraform infrastructure management.

## Conclusion
This application leverages OpenAI's powerful language model to generate and validate Terraform HCL templates. It provides a convenient command-line interface to interact with the functionality. Feel free to customize and extend the application based on your specific requirements.

