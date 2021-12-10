# Overview
For this project, you will create a functional CI/CD system which will deploy a runnable Flask ML application using Azure Pipelines, Cloud Shell and GitHub Actions.

This project consists of three major parts that need to be done in order to successfully deploy an application as a product of CI/CD proccess. 
The three main parts are:   
 1. Setup Azure Cloud Shell and GitHub Actions
 2. Setup Continuous Integration
 3. Setup Continuous Delivery

For the application to be succesfully deployed the above mentioned parts need to be done in the order they were listed.

    Setup of Azure Cloud Shell and GitHub Actions are defined under steps 4. to 6.
    Setup of Continuous Integration is mentioned under steps 3. and 4.
    Setup of Continuous Delivery instructions is mentioned here under steps 6. to 8. 

## Project Plan
<TODO: Project Plan

* A link to a Trello board for the project
* A link to a spreadsheet that includes the original and final project plan>

## Instructions

* Architectural Diagram which represents key parts of the system and its workflow can be seen [here]()

<TODO:  Instructions for running the Python project.  How could a user with no context run this project without asking you for any help.  Include screenshots with explicit steps to create that work. Be sure to at least include the following screenshots:

* Project running on Azure App Service

* Project cloned into Azure Cloud Shell

* Passing tests that are displayed after running the `make all` command from the `Makefile`

* Output of a test run

* [![Python application test with Github Actions](https://github.com/Marko-Buda/Course2-AgileDevelopmentwithAzure/actions/workflows/pythonapp.yml/badge.svg?branch=main)](https://github.com/Marko-Buda/Course2-AgileDevelopmentwithAzure/actions/workflows/pythonapp.yml)

* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

* Running Azure App Service from Azure Pipelines automatic deployment

* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```

* Output of streamed log files from deployed application

> 

## Enhancements

<TODO: A short description of how to improve the project in the future>

## Demo 

<TODO: Add link Screencast on YouTube>


