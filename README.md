# Monad MCP Server

This is a lightweight open-source MCP server for the Monad Dev Community Mission 2.

## Features

- Flask API
- Monad testnet integration
- Get balance by address

## Usage

```bash
pip install -r requirements.txt
export FLASK_APP=mcp_server
flask run
```

Then send a POST to `/balance` with:
```json
{ "address": "0xYourAddress" }
```