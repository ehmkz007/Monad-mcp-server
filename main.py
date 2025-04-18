
from flask import Flask, jsonify, request
import importlib.util
import os
import json

app = Flask(__name__)

@app.route("/.well-known/ai-plugin.json")
def plugin_metadata():
    return jsonify({
        "schema_version": "v1",
        "name_for_model": "MyMCPServer",
        "description_for_model": "A simple MCP server for Monad mission",
        "tools": ["/tools/hello_world"],
        "prompts": ["/prompts/greet"]
    })

@app.route("/tools/<tool_name>", methods=["GET", "POST"])
def run_tool(tool_name):
    tool_path = f"tools/{tool_name}.py"
    if not os.path.exists(tool_path):
        return jsonify({"error": "Tool not found"}), 404
    spec = importlib.util.spec_from_file_location("tool", tool_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    params = request.json if request.method == "POST" else {}
    result = module.run(params)
    return jsonify(result)

@app.route("/prompts/<prompt_name>", methods=["GET"])
def get_prompt(prompt_name):
    path = f"prompts/{prompt_name}.json"
    if not os.path.exists(path):
        return jsonify({"error": "Prompt not found"}), 404
    with open(path) as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
