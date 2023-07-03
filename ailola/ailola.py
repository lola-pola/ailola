#!/usr/bin/python

import os
import openai
import click
import colorama
import requests
from colorama import Fore, Style



def create_terraform(query,provider,temperature):
    if provider == "azure":
        openai.api_type = "azure"
        openai.api_base = os.getenv("OPENAI_API_BASE")
        openai.api_version = "2023-03-15-preview"
        openai.api_key = os.getenv("OPENAI_API_KEY")
        engine =  os.getenv("OPENAI_ENGINE")
    else:
        openai.api_key = os.getenv("OPENAI_API_KEY")
        engine =  os.getenv("OPENAI_ENGINE")
    if provider == "azure":   
        response = openai.ChatCompletion.create(
        engine=engine,
        messages = [{"role":"system","content":"You are a file name generator, only generate valid names for Terraform templates, \
                    You are a Terraform HCL generator, only generate valid Terraform HCL without provider \
                        templates."},{"role":"user","content":query}],
        temperature=temperature,
        stop=None)
    else:
        response = openai.ChatCompletion.create(
        model=engine,
        messages = [{"role":"system","content":"You are a file name generator, only generate valid names for Terraform templates, \
                    You are a Terraform HCL generator, only generate valid Terraform HCL \
                        templates."},{"role":"user","content":query}],
        temperature=temperature,
        stop=None)
    
    return str(response['choices'][0]['message']['content'])





def validate_terraform(query,provider,temperature):
    if provider == "azure":
        openai.api_type = "azure"
        openai.api_base = os.getenv("OPENAI_API_BASE")
        openai.api_version = "2023-03-15-preview"
        openai.api_key = os.getenv("OPENAI_API_KEY")
        engine =  os.getenv("OPENAI_ENGINE")
    else:
        openai.api_key = os.getenv("OPENAI_API_KEY")
        engine =  os.getenv("OPENAI_ENGINE")
    if provider == "azure":   
        response = openai.ChatCompletion.create(
        engine=engine,
        messages = [{"role":"system","content":"You are a file name validator, only validate Terraform templates, \
                    You are a Terraform HCL validator and suggest security changes and terraform changes \
                        templates."},{"role":"user","content":query}],
        temperature=temperature,
        stop=None)
    else:
        response = openai.ChatCompletion.create(
        model=engine,
        messages = [{"role":"system","content":"You are a file name validator, only validate Terraform templates, \
                    You are a Terraform HCL validator \
                        templates."},{"role":"user","content":query}],
        temperature=temperature,
        stop=None)
    
    return str(response['choices'][0]['message']['content'])





def debug_url(query,provider,temperature):
    if provider == "azure":
        openai.api_type = "azure"
        openai.api_base = os.getenv("OPENAI_API_BASE")
        openai.api_version = "2023-03-15-preview"
        openai.api_key = os.getenv("OPENAI_API_KEY")
        engine =  os.getenv("OPENAI_ENGINE")
    else:
        openai.api_key = os.getenv("OPENAI_API_KEY")
        engine =  os.getenv("OPENAI_ENGINE")
    if provider == "azure":   
        response = openai.ChatCompletion.create(
        engine=engine,
        messages = [{"role":"system","content":"You are a validator for jenkins, only validate jenkins console log, \
                    You are a Jenkins validator and debug current console \
                    "},{"role":"user","content":query}],
        temperature=temperature,
        stop=None)
    else:
        response = openai.ChatCompletion.create(
        model=engine,
        messages = [{"role":"system","content":"You are a validator for jenkins, only validate jenkins console log, \
                    You are a Jenkins validator and debug current console \
                    "},{"role":"user","content":query}],
        temperature=temperature,
        stop=None)
    
    return str(response['choices'][0]['message']['content'])



@click.command()
@click.option('--data', type=(str))
@click.option('--validate',type=(str))
@click.option('--debug',type=(str))
@click.option('--provider', required=True, type=(str),default="azure")
@click.option('--temperature', type=(float),default=1.0)
def cli(data,provider,validate,temperature, debug):
    if validate:
        with open(validate, 'r') as f:
            res = validate_terraform(query=f.read(),provider=provider,temperature=temperature)
            click.echo(Fore.YELLOW +str(res))

    elif debug:
        res = requests.get(debug)
        res = debug_url(query=res.text,provider=provider,temperature=temperature)
        click.echo(Fore.YELLOW +str(res))
    else:
        res = create_terraform(query=data,provider=provider,temperature=temperature)
        click.echo(Fore.BLUE +str(res))
    
    
if __name__ == '__main__':
    cli()
