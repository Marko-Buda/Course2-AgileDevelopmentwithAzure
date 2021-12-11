# Overview
[![Python application test with Github Actions](https://github.com/Marko-Buda/Course2-AgileDevelopmentwithAzure/actions/workflows/pythonapp.yml/badge.svg?branch=main)](https://github.com/Marko-Buda/Course2-AgileDevelopmentwithAzure/actions/workflows/pythonapp.yml)

For this project, you will create a functional CI/CD system which will deploy a runnable Flask ML application using Azure Pipelines, Cloud Shell and GitHub Actions.

This project consists of three major parts that need to be done in order to successfully deploy an application as a product of CI/CD proccess. 
The three main parts are:   
 1. Setup Azure Cloud Shell and GitHub Actions
 2. Setup Continuous Integration
 3. Setup Continuous Delivery

For the application to be succesfully deployed the above mentioned parts need to be done in the order they were listed.

    Setup of Azure Cloud Shell and GitHub Actions are defined under steps 1. to 6.
    Setup of Continuous Integration is mentioned under steps 7. to 10.
    Setup of Continuous Delivery instructions is mentioned here under steps 6. to 8. 

## Project Plan
Includes project estimation for the whole year as well a trello board for the tracking of the current progress. 

* A link to a Trello board for the project is [here](https://trello.com/b/NSTKhFFI/udacity-azure-cloud-devops-project-2)
* A link to a spreadsheet that includes the original and final project plan is [here](https://docs.google.com/spreadsheets/d/1ONBoKr3c7egFtFZl26B8JdhEi5MHQT7c2NxBg6iAjeY/edit?usp=sharing)

## Instructions

Before going through instructions for how to successfully deploy this project, please take a look at the 
* Architectural Diagram which represents key parts of the system and its workflow can be seen [here]()

<TODO:  Instructions for running the Python project.  How could a user with no context run this project without asking you for any help.  Include screenshots with explicit steps to create that work. Be sure to at least include the following screenshots:

Instructions for running the Python project are all listed in the order of execution.

1. Create a Github repository
2. Launch Azure Cloud Shell environment by clicking on the first icon located next to the Azure search bar (the bar is on the top of Azure page). 
3. In Cloud Shell enter command **_ssh-keygen_**. This creates public rsa key located on path _~/.ssh_.
4. Copy public key from id_rsa.pub file and go to your Github repository
5. Under repository ssttings select _Deploy keys_ and add your copied public key
6. In Cloud Shell you can now clone your repository ( ***Project cloned into Azure Cloud Shell** - [screenshot](https://github.com/Marko-Buda/Course2-AgileDevelopmentwithAzure/blob/main/screenshots/Cloned_github_repository.png))
7. Enter your repository in Cloud Shell by entering **_cd <name_of_your_repository>_** 
8. Create project scaffolding. You can use this repository as it contains for running the project
9. Run make all command and wait for it to finish. (***Passing tests that are displayed after running the `make all` command from the `Makefile`** - [screenshot](https://github.com/Marko-Buda/Course2-AgileDevelopmentwithAzure/blob/main/screenshots/make_all_passed_test.png))
10. Add to your repository on GitHub the following file _.github/workflows/pythonapp.yml_ and wait for GitHub Actions to finish. (***Output of a test run** - [screenshot](https://github.com/Marko-Buda/Course2-AgileDevelopmentwithAzure/blob/main/screenshots/verify_remote_tests.png))



***Project running on Azure App Service** - [screenshot]().

***Successful deploy of the project in Azure Pipelines** - [screenshot]().

***Running Azure App Service from Azure Pipelines automatic deployment** - [screenshot]().

***Successful prediction from deployed flask app in Azure Cloud Shell** - [screenshot](https://github.com/Marko-Buda/Course2-AgileDevelopmentwithAzure/blob/main/screenshots/prediction_in_cloud_shell.png).
The output should look similar to this:

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```

***Output of streamed log files from deployed application** - [screenshot]().

## Enhancements

* As can be seen from the Architectural Diagram ([here]()), the successfull execution of CI part is not a condition that needs to pass which would then trigger the execution of CD part. Currently the CD is also triggered on push change to a pull request
* Instead of using GitHub Actions for CI in the future this could be changed so that the Azure Pipelines execute both Continuous Integration and Continuous Delivery
in one cloud environment


## Demo 

<TODO: Add link Screencast on YouTube>


