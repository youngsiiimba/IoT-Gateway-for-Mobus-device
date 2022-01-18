# Modbus IoT

This code is designed to read temperature data from MOXA ioLogik E2262 controller and then have this data sent to the Azure IoT Hub.

## Requirements
To get this code to work on your own modbus device, you'll need:

* to install the dependencies required to get the program to run
* the IP address of your modbus address
* the connection string for the device you create on the Azure IoT Hub
* to install device explorer in order to view the data being sent to the Azure IoT Hub


## Installing depedecies 
A few of the libraries used in this project don't come preinstalled by default with python so you'll need to install them. This can easily be achieved by using the following steps:

1. open command prompt in the project folder and create a virtual enviroment `python -m venv env`
2. now activate your enviroment using `env\Scripts\activate.bat`
3. finally install the dependencies required to get the pogram to run using `pip install -r requirements.txt`

If the `python` or `pip` commands don't work in your command prompt/terminal please refer to [this](https://www.makeuseof.com/tag/install-pip-for-python/) article to help you setup python correctly.

## Extracting data from modbus device
In order to extract the data from the MOXA ioLogik E2262 controller, you'll need to know it's IP address.

The IP address can easily be obtained and changed from MOXA's ioAdmin software. This software can be downloaded from Moxa's official site [here](https://www.moxa.com/en/support/product-support/software-and-documentation/search?psid=71178)

Once you have the ioAdmin installed on your computer, follow these next steps:

1. Open ioAdmin and let it search for your device.
1. Once ioAdmin has found your device, take note of it's IP Address.
1. Now you'll need to change the IP address of your computer to match the same network as your Moxa device.

Steps 1 to 3 are all you need to connect to the Moxa device and extract data from it, but we not only need to extract data but also push the data to the Azure IoT Hub and for this to happen we need internet access; So we need to change the IP address of our Moxa device and computer to those that allow our computer to have internet access again. For this follow from step 4 onwards.

1. Connect to your Moxa device from ioAdmin, then login to the device.(By default there shouldn't be any login credentials required to login)
1. Once connected and logged in, now export the configuration file to your computer
1. Open the configuration file and change the IP address in the configuration file to one that will allow it to connect to the same network as your router.
1. Now go back to ioAdmin and import the configuration file you just edited. This will change the IP address of your Moxa device.
1. Finally change the IP address of your computer to one that will allow it to connect to the same network as your router. Alternatively, just let the computer automatically get it's IP address from the router.

If you need more help configuring your Moxa device, please refer to the manual for the Moxa ioLogik E2200 series [here](https://www.moxa.com/en/support/product-support/software-and-documentation/search?psid=71178)

Also in your configuration file, you'll be able to view the register address for your various analog and digital I/O ports

## How to create an IoT Hub from the Azure portal and get device connection string

You'll need to create an IoT Hub to receive your data. Once you've created your IoT Hub you'll need to create a new 'device' and copy it's connection string into the code.

Please find a detailed tutorial on how to do this from Microsofts documentation [here](https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-create-through-portal)


## How to install Device Explorer and view the data being sent to Azure IoT Hub
This section describes how to download, build and use the Device Explorer tool for managing and using IoT Hub devices.

1. Download the [DeviceExplorer.msi](https://github.com/Azure/azure-iot-sdks/releases/download/2016-11-17/SetupDeviceExplorer.msi) by using the link [here](https://github.com/Azure/azure-iot-sdks/releases/download/2016-11-17/SetupDeviceExplorer.msi)
2. Install Device Explorer 
3. In the Configuration tab, add the connection string for your IoT Hub. Then click "Update" For information about how to find this connection string, please refer to microsofts documentation [here](https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-create-through-portal)
4. Click on the "Data" tab
5. Click on the drop down menu labelled "Device ID" and find the device you created. If you haven't created a device yet please refer to Microsofts documentation [here](https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-create-through-portal)
6. Finally click on "Monitor" and Device Explorer will start listening for incoming data

