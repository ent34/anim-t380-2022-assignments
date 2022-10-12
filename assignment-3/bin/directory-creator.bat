@echo off

REM Script Name: Directory Creator
REM Author: Erika Taylor
REM Date: October 11, 2022
REM Description: This script creates a directory

REM Moves up to assignment-3 directory
cd..

REM Creates directory assets\%asset%\maya\scenes
mkdir assets
cd assets
mkdir %asset%
cd %asset%
mkdir maya
cd maya
mkdir scenes


