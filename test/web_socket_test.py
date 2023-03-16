import websocket
import json
import get_prices

cst = get_prices.res_header["CST"]
security_token = get_prices.res_header["X-SECURITY-TOKEN"]

# WebSocket
def on_message(ws, message):
    print("Message: " + message)
    if json.loads(message)["destination"] != 'ping':
        ws.send(json.dumps({
            "destination": "ping",
            "correlationId": "5",
            "cst": cst,
            "securityToken": security_token
        }))

def on_error(ws, error):
    print("Error: " + str(error))


def on_close(ws, close_status_code, i):
    print("Connection closed with status code: " + str(close_status_code))
    print(i)


def on_open(ws):
    print("Connection opened")

    ws.send(json.dumps({
        "destination": "OHLCMarketData.subscribe",
        "correlationId": "3",
        "cst": cst,
        "securityToken": security_token,
        "payload": {
            "epics": [
                "US100"
            ],
            "resolutions": [
                "MINUTE"
            ],
            "type": "classic"
        }
    }))


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://api-streaming-capital.backend-capital.com/connect",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open 
    ws.run_forever()
