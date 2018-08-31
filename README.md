# DLHub Schemas
[![Build Status](https://travis-ci.org/DLHub-Argonne/dlhub_schemas.svg?branch=master)](https://travis-ci.org/DLHub-Argonne/dlhub_schemas)

This repository contains all of the data format schemas used by the Data and Learning Hub for Science (DLHub). 
The schemas describe how to document machine learning models and datasets in a format that faciliates easy discovery and re-use.

## Structure

The main schema types are defined in the root folder (`schemas`) and include how to describe datasets and the components of an ML model (which we call "servables"). 

The main schema types are supported by various subtypes (e.g., specific types of inputs), which are available in various subfolders.
