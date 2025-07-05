import buttplug
import asyncio
import time
import logging

async def plug_connect():
    client = buttplug.Client("ButtPlug", buttplug.ProtocolSpec.v3)
    connector = buttplug.WebsocketConnector("ws://127.0.0.1:12345", logger=client.logger)
    try:
        await client.connect(connector)
    except Exception as e:
        logging.error(f"Could not connect to server, exiting: {e}")
        return
    
    await client.start_scanning()
    await asyncio.sleep(3)
    await client.stop_scanning()

    if len(client.devices) != 0:
        for key, val in client.devices.items():
            print(f'{key}: {val.name}')
        if len(client.devices) > 1:
            device = client.devices[int(input("Enter the number of the device you'll be using: "))]
        else: device = client.devices[list(client.devices.keys())[0]]
        print(device.name)
        if len(device.actuators) != 0:
            await device.actuators[0].command(0.5)
        if len(device.linear_actuators) != 0:
                await device.linear_actuators[0].command(1000, 0.5)
        if len(device.rotatory_actuators) != 0:
                await device.rotatory_actuators[0].command(0.5, True)

        return device
    return None