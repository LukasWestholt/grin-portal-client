import asyncio
import json
import ssl
from typing import Any

import websockets

from config.env import ws_url
from grin_portal_client.Answer import Answer

class GrinPortalWebsocket:
    def __init__(self):
        self.ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        self.ssl_context.check_hostname = False
        self.ssl_context.verify_mode = ssl.CERT_NONE

    async def send_requests(self, messages_to_send: list[Any]) -> Answer | None:
        try:
            async with websockets.connect(ws_url, ssl=self.ssl_context) as websocket:
                print(f"Connected to {ws_url}")
                await self.read_response(websocket)

                # Send each message multiple times
                for i, data in enumerate(messages_to_send):
                    message = json.dumps(data)
                    try:
                        await self.send(websocket, i, message)
                        out = await self.read_response(websocket)
                        if out:
                            return out
                    except websockets.exceptions.ConnectionClosedOK:
                        print("Connection is closed.")
                        return await self.send_requests(messages_to_send)
                websocket.transport.close()
                print("Connection is closed.")
        except (websockets.exceptions.InvalidStatus, TimeoutError):
            print("Connection could not be established to " + ws_url + ".")
        print("Finished requests.")

    @staticmethod
    async def send(websocket, i: int, message: str) -> None:
        print(f"Sending message: {i}")
        await websocket.send(message)

    async def read_response(self, websocket) -> Answer | None:
        response = await self._read_response(websocket)
        if isinstance(response, Answer):
            return response

        while self.is_loading_response(response):
            response = await self._read_response(websocket)
            if isinstance(response, Answer):
                return response

    async def _read_response(self, websocket) -> Answer | list:
        async with asyncio.timeout(10):
            response = await websocket.recv()
        resp_obj = self.interpret_response(response)
        print(f"Received response: {resp_obj}")
        return resp_obj

    @staticmethod
    def is_loading_response(response: list) -> bool:
        if len(response) != 1:
            return False
        if ["o"] == response or r"ACK " in response[0]:
            return False
        return True

    @staticmethod
    def modify_string(input_str):
        start = input_str.find("{")
        end = input_str.rfind("}")
        if start != -1 and end != -1 and start < end:
            return "[" + input_str[start:end + 1].replace("\\\"", "\"").replace("\\\\", "\\") + "]"
        start = input_str.find("[")
        end = input_str.rfind("]")
        if start != -1 and end != -1 and start < end:
            return input_str[start:end + 1].replace("\\\"", "\"").replace("\\\\", "\\")
        raise RuntimeError(input_str)

    def interpret_response(self, response: str) -> Answer | list:
        if response == "o":
            response = '["o"]'
        json_str = self.modify_string(response)
        json_data: list = json.loads(json_str)

        try:
            answer = Answer(json_data[0]["values"]["acmgClass"], json_data[0]["values"]["detailed_effect_PTV"],
                   json_data[0]["values"]["Protein_effect_ptv"])
            return answer
        except (KeyError, TypeError):
            pass
        return json_data
