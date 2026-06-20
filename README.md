# OpenFable Dataset

## What is this? 

This repository is an attempt to generate a dataset in order to make open source models as perfect as Claude Fable. Although this proof-of-concept is being made using ChatGPT and has no reasoning included, still can improve the results of a good open model such as Qwen 3.5.

## How to execute

First, you need python 3.10 and above. Then:

1. Clone this repository.
2. Install requirements by running `pip install -r requirements.txt`
3. Move `config.py.example` to `config.py` and modify it as needed (see [configuration](#configuration))
4. Edit `main.py` and find your own category of interest. 
5. Run `main.py` and wait for it to start working. 

### Configuration

1. `MODEL` : The model you use in order to generate questions or problems.
2. `ANSWERING_MODEL` : The model you may use to generate answers. It can be a better model or the same as previous one. 
3. `SYSTEM_PROMPT` : It comes from [This project](https://github.com/prp-e/open-fable)
4. `OPENAI_ENDPOINT` : It can be original OpenAI's base url or can be anything else. I suggest using [this one](https://freemodel.dev/invite/FRE-c3b7b75e) to get a good amount of free usage on GPT 5.5 or 5.4
5. `OPENAIP_API_KEY` : API Key you obtain from the OpenAI compatible providers.

## Models

## Final Goal

A tool whci helps you distill any big model any time, anywhere. 