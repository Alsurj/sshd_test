#!/bin/bash --login
set -e

conda activate $HOME/app/envdocker

exec "$@"

#nvidia-smi


