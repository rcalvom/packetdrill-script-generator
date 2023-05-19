# Packetdrill Script generator and executor

In this repository you can find some Python scripts that can generate systematically the test scripts to use as inputs to execute packetdrill.

In this scripts the following protocols are supported


## Run project

To Run successfully this project you have to configure the paths on the files under the folder `configuration_files`, in that folder you can find the configurations for every stack:

* FreeRTOS
* Contiki
* PicoTCP
* lwIP

The paths on the variables `packetdrill_command` and `target_command` has to been configured to run the correspondings for the local instalation

After configuring those paths, you have to configure the execution in `configuration.py` and `test_cases.py` as needed

In `configuration.py` you have to select the stack to execute commentin in the stack you want to test.

In `test_cases.py` you have to select the protocols to test commentin in the corresponding lines


After the previous configurations you can execute the project with the following command:


```
sudo ./main.py --clean --verbose --execute --verbose
```
