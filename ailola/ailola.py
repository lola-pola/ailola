#!/usr/bin/python

import os
import click
import openai
import colorama
import requests
from datetime import datetime
from colorama import Fore, Style



def general_prompt(general_query,provider,temperature):
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
        messages = general_query,
        temperature=temperature,
        stop=None)
    else:
        response = openai.ChatCompletion.create(
        model=engine,
        messages = general_query,
        temperature=temperature,
        stop=None)
    
    return str(response['choices'][0]['message']['content'])




@click.command()
@click.option('--create_terraform', type=(str))
@click.option('--validate_terraform',type=(str))
@click.option('--linux_help',type=(str))
@click.option('--debug_url',type=(str))
@click.option('--create_k8s',type=(str))
@click.option('--provider', required=True, type=(str),default="azure")
@click.option('--temperature', type=(float),default=1.0)
@click.option('--model', type=(str),default="yoniggprt")
@click.option('--debug_linux',type=(str))
@click.option('--ask',type=(str))
@click.option('--create_file',type=(str))
@click.option('--create_web',type=(str))


def cli(create_terraform,provider,
        validate_terraform,temperature,
        debug_url,create_k8s,
        model,debug_linux,
        linux_help,ask,
        create_file,create_web):
    
    def get_relevant(key,query):
        prompt = {'create_terraform':[{"role":"system","content":"You are a file name generator, only generate valid names for Terraform templates,You are a Terraform HCL generator, only generate valid Terraform HCL templates."},{"role":"user","content":query}],
                  'validate_terraform':[{"role":"system","content":"You are a Terraform HCL validator, only validate valid Terraform HCL templates."},{"role":"user","content":query}],
                  'create_k8s':[{"role":"system","content":"You are a k8s template generator, only generate valid k8s templates."},{"role":"user","content":query}],
                  'debug_url' : [{"role":"system","content":"You are a validator for jenkins, only validate jenkins console log, \You are a Jenkins validator and debug current console "},{"role":"user","content":query}],
                  'debug_linux' : [{"role":"system","content":"You are a debugger for linux, only debugger linux commands, \You are a linux debugger "},{"role":"user","content":query}],
                  'linux_help' : [{"role":"system","content":"You are a linux command line expert, only answer linux commands, \You are a linux coomand line expert  "},{"role":"user","content":query}],
                  'create_web' : [{"role":"system","content":"You are a web creator command line expert, only answer web examples with all user requests "},{"role":"user","content":query}],
                  'ask' : [{"role":"system","content":"You are a dev and devops expert, only answer dev and devops answers, \You are a dev and devops expert  "},{"role":"user","content":query}]

              }
        return prompt[key]
    
    def create_file_from_output(output,file_name):
        file_name = file_name
        with open(file_name, 'w') as f:
            f.write(output)
    
    
    if validate_terraform:
        with open(validate, 'r') as f:
            res = general_prompt(general_query=get_relevant(key="validate_terraform",query=f.read()),provider=provider,temperature=temperature)
            click.echo(Fore.YELLOW +str(res))
            if create_file:
                create_file_from_output(res,create_file)
    elif debug_url:
        res = requests.get(debug_url)
        res = general_prompt(general_query=get_relevant(key="debug_url",query=res.text),provider=provider,temperature=temperature)
        click.echo(Fore.GREEN +str(res))
        if create_file:
            create_file_from_output(res,create_file)
        
    elif debug_linux:
        res = general_prompt(general_query=get_relevant(key="debug_linux",query=debug_linux),provider=provider,temperature=temperature)
        click.echo(Fore.GREEN +str(res))  
        if create_file:
            create_file_from_output(res,create_file)    
    elif create_web:
        res = general_prompt(general_query=get_relevant(key="create_web",query=create_web),provider=provider,temperature=temperature)
        click.echo(Fore.BLUE +str(res))  
        if create_file:
            create_file_from_output(res,create_file)             
    elif create_k8s:
        res = general_prompt(general_query=get_relevant(key="create_k8s",query=create_k8s),provider=provider,temperature=temperature)
        click.echo(Fore.BLUE +str(res))
        if create_file:
            create_file_from_output(res,create_file)
        
    elif linux_help:    
        res = general_prompt(general_query=get_relevant(key="linux_help",query=linux_help),provider=provider,temperature=temperature)
        click.echo(Fore.BLUE +str(res))
        if create_file:
            create_file_from_output(res,create_file)

    elif create_terraform:    
        res = general_prompt(general_query=get_relevant(key="create_terraform",query=create_terraform),provider=provider,temperature=temperature)
        click.echo(Fore.BLUE +str(res))
        if create_file:
            create_file_from_output(res,create_file)

    elif ask:    
        res = general_prompt(general_query=get_relevant(key="ask",query=ask),provider=provider,temperature=temperature)
        click.echo(Fore.BLUE +str(res))
        if create_file:
            create_file_from_output(res,create_file)
  
    else:
        res = 'Before you start please make sure you have the following env variables: \n \
           export OPENAI_ENGINE=GPT3\n\
            export OPENAI_API_KEY=xxxxx\n\
            export OPENAI_API_BASE=https://xxxx.openai.azure.com/\n\
\n\
\n\
\n\
            what do you want to do today? \n \
           --create_terraform "create vm with ssh" \n\
            --validate_terraform file location \n\
            --debug_url give jenkins url to debug in out put console \n\
            --create_k8s "create http server with hpa that scale up to 10 replicas with http request"\n\
            --linux_help "how do i list all folder with sizes in human readable" \n\
            --linux_help "how do i run loop for all files in directory and echo + addding the word test" \n\
            --debug_linux "im getting this error `cat /var/log/system.log`"\n\
            --file_name "create a file name from date time"\n\
            --create_web "create simple web page"\n\
            --ask "create a script that find the oldest file in dir in bash and in python"\n'

        click.echo(Fore.YELLOW +str(res))

    
    
if __name__ == '__main__':
    cli()

