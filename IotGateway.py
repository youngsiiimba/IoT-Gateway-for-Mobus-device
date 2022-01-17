from pyModbusTCP import client, utils
from pyModbusTCP.client import ModbusClient

from azure.iot.device import IoTHubDeviceClient, Message


#Create an IoT Hub from the Azure portal, then in your IoT Hub click on "Devices" in the side panel and create a new device.
#After creating your device, copy and paste the connection string for your device here
CONNECTION_STRING = "HostName=rotary-kiln-iothub.azure-devices.net;DeviceId=Device1;SharedAccessKey=nuukNAmFyTcbYh/gS9LrgS9uUWM24fnrGAr/EEz67SQ="
MSG_TXT = '{{"temperature": {temperature}}}'

def iothub_client_init():
    # Create an IoT Hub client
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client

def iothub_client_telemetry(temperatureData):

    try:
        client = iothub_client_init()
        print ( "IoT Hub device sending periodic messages, press Ctrl-C to exit" )
        
           
        temperature = temperatureData

        #format the message for Azure IoT Hub
        msg_txt_formatted = MSG_TXT.format(temperature=temperature)
        message = Message(msg_txt_formatted)

            # Add a custom application property to the message.
            # An IoT hub can filter on these properties without access to the message body.
          #  if temperature > 30:
          #    message.custom_properties["temperatureAlert"] = "true"
          #  else:
          #    message.custom_properties["temperatureAlert"] = "false"

        # Send the message.
        print( "Sending message: {}".format(message) )
        client.send_message(message)
        print ( "Message successfully sent.")

    except KeyboardInterrupt:
        print ("IoTHubClient stopped.")


if __name__ == '__main__':
    client = ModbusClient(host='10.0.0.25', port=502, debug=False)
      
    if client.open():
        print("Connected to ModbusTCP server")
    else:
        print("Failure connecting to ModbusTCP server")
    
    while client.open():
        #reg_addr = 1 because I connected a Thermocouple to the TC1 analog input pin on Moxa ioLogik E2262
        #The read_input_registers() function returns a list of integer values, and the temperature value we looking for is located at index 2, finally we have to divide the number by 10 to get the temperature value as a float value
        data = client.read_input_registers(reg_addr=1, reg_nb=95)[2] / 10
        iothub_client_telemetry(data)
        time.sleep(1)

