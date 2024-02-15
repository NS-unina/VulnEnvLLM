## Guideline

This document will have the following simple structure:

1. **Problems' Description number 1**:
    - Solution number 1;
    - Solution number 2.
2. **Problems' Description number 2**:
    - Solution number 1.
3. **Problems' Description number 3**:
    - Solution number 1;
    - Solution number 2;
    - Solution number 3.

## Docker Analysis and Evaluation

1. Many vulnerabilities are related to misconfiguration of the service or web app and very often LLM models don't comprehend particular configuration file syntax or generate in separate files or don't generate them at all:
    - Training model on different but common configuration file extension, like XML, JSON or .config, or on common service configuration such as Apache, Wordpress, Python and more;
    - Use second auxiliary prompt to generate only the configuration file and a script to write/upload the file in the right path;
    - Give simple or no explanation of what to write and where to write it and have the end user carry it out;
  
2. Too often dowload url are wrong, common reason are: outdated software, the prompt mislead the model, simple error such as different punctuation mark, software isn't available anymore:
    - Check any url beforhand with cli utilities (wget or curl); if they're empty or they raise any error or they've different extension signature than the expected one;
    - Train the model with the most common download archives or the most comprehensive newsletter.
  
3. Missing building library when building complex software:
    - Check and understand error log, download again and retry;
    - Train over software requirements online.
  
4. During building process model use cli utilities that assume are already downloaded:
    - Analyze produced dockerfile and try to install all utilities anyway.
  
5. Some commands aren't required to the correct building process and block it, such as ADD and COPY or other directive used to configure and customize the image:
    - Forbidding creation of such commands, unless explictly required from user;
    - Always comment them out if created, unless explictly required from user.

6. Most software require to go through a wizard setup:
    - Automate initial configurations as much as possible and have the end user carry the rest out.
  
7. Many software and services requires a database, usually they can use multiple type but MySQL is always supported:
    - Using docker-compose to build a fully working enviroment and let the model generate both dockerfile (the webapp and the database);
    - Using docker-compose to build together a fully working enviroment but pre-build dockerfile of MySQL database and most common, like MariaDB, Cassandra and so on;
    - Build only the dockerfile and leave the database and its connection to the end user.