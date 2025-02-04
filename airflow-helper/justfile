## Python version
PYTHON_VERSION := "3.10"

## Folder structure:
DOC_FOLDER := "docs"
ASSETS_FOLDER := DOC_FOLDER + "/assets"
AUTOMATION_FOLDER := "/automation"

## Project info
GCP-PROJECT := "gcp-project"
PROJECT_NAME := "airflow-composer-template"
GITHUB_URL := "https://github.com/harryalexanderdunn/airflow-helper"
VENV_NAME := "venv"

## Packages available from the package manager
PACKAGE_MANAGER_DEPENDENCIES := '"sed" "grep" "gawk"'

## Project Setup pipeline
project-setup: create-env-file install-python3 create-virtual-env

## Project Setup for first time users that need to download packages in WSL and setup with GCP
full-project-setup: package-manager-dependencies install-python3 create-env-file create-virtual-env initialise-sdk-environment gcp-setup lazydocker-install docker

## Documentation creation/update pipeline
update-docs: update-python-docs update-unit-test-docs update-data-dictionary-docs

## Setup GCP credentials
gcp-setup:
    @echo 'Follow the instructions once loaded'
    gcloud auth application-default login --no-launch-browser

## Reinitialise GCP configuration, create new configuration or switch configuration. i.e switch between gcp projects
initialise-sdk-environment:
    gcloud auth login --no-launch-browser
    gcloud init

## install package manager dependencies
package-manager-dependencies:
	for package in {{PACKAGE_MANAGER_DEPENDENCIES}}; do \
		echo `sudo apt-get install $package`;\echo "$package installed."; \
	done

## install python3
install-python3:
    sudo apt install software-properties-common
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update 
    sudo apt list --upgradable
    sudo apt upgrade
    sudo apt install python{{ PYTHON_VERSION }} python3-pip ipython3
    sudo apt install python{{ PYTHON_VERSION }}-venv
    @echo 'Python packages installed'

## install lazydocker
lazydocker-install:
    #!/bin/bash
    curl https://raw.githubusercontent.com/jesseduffield/lazydocker/master/scripts/install_update_linux.sh | bash

## create virtualenv
create-virtual-env:
    python{{ PYTHON_VERSION }} -m venv .{{ VENV_NAME }}
    ./.{{ VENV_NAME }}/bin/pip install -r requirements-dev.txt
    @echo 'Run `source ./.{{ VENV_NAME }}/bin/activate` to activate your environment'
    @echo 'Run `deactivate` to deactivate your environment'

# how to run virtual env
print-venv-activation:
    @echo 'Run `source ./.{{ VENV_NAME }}/bin/activate` to activate your environment'

## Create the dotenv file for running it locally.
create-env-file:
    echo "AIRFLOW_UID=1000" > .env

## install libraries
install-libraries:
    ./.{{ VENV_NAME }}/bin/pip install -r requirements-dev.txt

## uninstall libraries
uninstall-libraries:
    ./.{{ VENV_NAME }}/bin/pip uninstall -r requirements-dev.txt

## Generate docs from the python code within the helpers section
update-python-docs:
    @echo "Generating Python Script docs from sections outlined below"

## Generate docs from the unit tests code within the tests section
update-unit-test-docs:
    @echo "Generating Python Script docs from sections outlined below"

## Update the production data dictionaries
update-data-dictionary-docs:
    @echo "Generating Data Dictionary from Automation Script"
    ./.{{ VENV_NAME }}/bin/python{{ PYTHON_VERSION }} {{ AUTOMATION_FOLDER }}/data_dictionary.py

#Install docker by following the steps outlined on their website.
docker:
	sudo apt-get install ca-certificates curl gnupg
	sudo install -m 0755 -d /etc/apt/keyrings
	curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
	sudo chmod a+r /etc/apt/keyrings/docker.gpg
	echo \
		"deb [arch="`dpkg --print-architecture`" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
		"`cat /etc/os-release | sed -n 's/^VERSION_CODENAME="*\([^"]*\)"*/\1/p'`" stable" | \
		sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
	sudo apt-get update
	sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
	sudo docker run hello-world
	-sudo groupadd docker
	sudo usermod -aG docker `echo $USER`
	# This echo should be before the `newgrp` command since if it's after it doesn't always work.
	echo "Test the installation with \`docker run hello-world\`. You may need to log out and back in if it doesn't work."
	-newgrp docker

# Docker container commands
clean-docker-containers:
    docker rm $(docker ps -aq)

force-remove-docker-containers:
    docker rm -vf $(docker ps -aq)

show-running-containers:
    docker ps

show-all-containers:
    docker ps -a

# Create the local app setup using docker compose.
local-airflow:
  mkdir -p ./airflow/dags
  mkdir -p ./airflow/config
  mkdir -p ./airflow/logs
  mkdir -p ./airflow/plugins
  mkdir -p ./airflow/secrets
  chmod +r ~/.config/gcloud/application_default_credentials.json
  docker compose -f airflow-docker-compose.yaml build 
  docker compose -f airflow-docker-compose.yaml up airflow-init
  docker compose -f airflow-docker-compose.yaml up -d
  @echo "Run lazydocker to view the docker image running airflow"

# Create the local app setup using docker compose. Lightweight version of airflow
local-airflow-lite:
  mkdir -p ./airflow/dags
  mkdir -p ./airflow/config
  mkdir -p ./airflow/logs
  mkdir -p ./airflow/plugins
  mkdir -p ./airflow/secrets
  chmod +r ~/.config/gcloud/application_default_credentials.json
  docker compose -f airflow-docker-compose-lite.yaml build 
  docker compose -f airflow-docker-compose-lite.yaml up -d
  @echo "Run lazydocker to view the docker image running airflow"

# remove containers for local airflow app once finished
destroy-airflow:
  docker compose -f airflow-docker-compose.yaml down --volumes --rmi all
  docker compose -f airflow-docker-compose.yaml down --volumes --remove-orphans

# remove containers for local airflow app once finished. Remove lightweight version containers
destroy-airflow-lite:
  docker compose -f airflow-docker-compose-lite.yaml down --volumes --rmi all
  docker compose -f airflow-docker-compose-lite.yaml down --volumes --remove-orphans

# Ruff commands

lint-check:
    ruff check

lint-code:
    ruff format
