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
    await asyncio.sleep(10)
    await client.stop_scanning()

    if len(client.devices) != 0:
        device = client.devices[1]
        print(device.name)
        if len(device.actuators) != 0:
            await device.actuators[0].command(0.5)
        if len(device.linear_actuators) != 0:
                await device.linear_actuators[0].command(1000, 0.5)
        if len(device.rotatory_actuators) != 0:
                await device.rotatory_actuators[0].command(0.5, True)

        return device
    return None