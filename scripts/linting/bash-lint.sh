#!/usr/bin/env bash

set -e
set -x

#mypy $1
flake8 $1
black $1 #--check
isort $1 #--check-only
pydocstyle $1