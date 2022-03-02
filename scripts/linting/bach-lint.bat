@echo off
title Lint Script
set file_name=%1
echo linting %file_name%
flake8 %file_name%
black %file_name%
isort %file_name%
pydocstyle %file_name%
echo Done