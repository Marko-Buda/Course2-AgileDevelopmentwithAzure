#!/usr/bin/env bash

#git clone git@github.com:Marko-Buda/Course2-AgileDevelopmentwithAzure.git
cd Course2-AgileDevelopmentwithAzure/
az webapp up -n project2_CI_and_CD
az webapp config set -g Course2-Agile-Development-with-Azure -n project2_CI_and_CD
