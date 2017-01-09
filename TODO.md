## TODO:

* Make jobs/background tasks persistent by adding a sqlite store for APScheduler and storing it in /data.
* Allow the configuration of periodic jobs from the UI.
* Find a better way to return the state, using settings.py or some config file
* Print better logging info to the dashboard
* Figure out how to install automationHat without errors (it looks ugly at buildtime)
* pin requirements to specific versions
* perhaps switch base image to minideb (https://github.com/bitnami/minideb)