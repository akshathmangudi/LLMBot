# LLMBot

UPDATE: From this project onwards, I will be focusing not only on implementation of the project but deployment 
with the help of GitHub Actions, Docker, Kubernetes, etc. I will also implement modularity in medium-to-larger
scale projects for organization’s sake. 

## Table of Contents
* <a href="https://github.com/akshathmangudi/LLMBot#overview">Overview</a>
* <a href="https://github.com/akshathmangudi/LLMBot#reqruiements">Requirements</a>
  * <a href="https://github.com/akshathmangudi/LLMBot#creating-virtualvenv">Creating virtualvenv</a>
  * <a href="https://github.com/akshathmangudi/LLMBot#installing-dependencies">Installing dependencies</a>
* <a href="https://github.com/akshathmangudi/LLMBot#running-the-docker-image">Running Docker</a>
* <a href="https://github.com/akshathmangudi/LLMBot#running-the-application">Running the application</a>
* <a href="https://github.com/akshathmangudi/LLMBot#licensing">Licensing</a>

## Overview

The LLMBot is a Python application that uses a language model and natural language processing in which the use can 
query multiple PDFs and can ask the bot on questions related to the PDF queried. The language model used for this
application is the OpenAI model and Hugging Face models are used for embeddings. This application generates
accurate answers to your queries. 

## Requirements
### Creating virtualenv 
Virtual environments allow you to isolate certain dependencies within a specific directory for a specific use-case. 
The positive thing about venvs is that you can save space as virtual environments can be deactivated and deleted. 

Clone the repository and change into it: 
```shell
$ git clone https://github.com/akshathmangudi/LLMBot.git
$ cd LLMBot/
```

For Python 3.6+ users: 
```shell
$ python -m venv /path/to/virtualenv
```
For activation of virtualenv:

bash/zsh: 
```bash 
$ source <venv>/bin/activate
```
fish: 
```shell
$ source <venv/bin/activate.fish
```

cmd.exe: 
```shell
$ C:\> <venv>\Scripts\activate.bat
```

For conda users, the following commands are to be sequentially passed into your terminal:
```bash
$ conda -V
$ conda update conda
$ conda create -n <envname> python=x.x anaconda
$ conda activate <envname>
```

For deactivation: 
```bash
$ conda deactivate
```

### Installing dependencies
To install the dependencies required for the streamlit application to run, run the follow command
```shell
$ pip install -r requirements.txt
```

## Running Docker
As the model has been deployed with Docker and GitHub Actions, the image can be run using these following commands. 

Log in to Docker:
```shell
$ docker login [username] 
```
After inputting your Docker ID, input your PAT as the password.

Run the container: 
```shell
$ docker run -p 8501:8501 streamlitapp:latest
```

## Running the application
To run the application, run the following command: 
```shell
$ streamlit run app.py
```

## Licensing
This repository is licensed under the MIT License. See the LICENSE file for details.