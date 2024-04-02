#!/bin/bash

ENV_NAME="pydev"

PYTHON_VERSION="3.10.12"

# Check if the environment already exists
if (conda env list | grep $ENV_NAME); then
    echo "$ENV_NAME environment already exists"
else
    echo "Creating $ENV_NAME environment"
    conda create -n $ENV_NAME python=$PYTHON_VERSION -y
fi

source /opt/conda/etc/profile.d/conda.sh
conda init
conda activate $ENV_NAME

wget https://github.com/padreati/rapaio-jupyter-kernel/releases/download/1.3.0/rapaio-jupyter-kernel-1.3.0.jar
java -jar ./rapaio-jupyter-kernel-1.3.0.jar -i -auto
rm -r ./rapaio-jupyter-kernel-1.3.0.jar


