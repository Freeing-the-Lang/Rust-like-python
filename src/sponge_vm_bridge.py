import subprocess
import json
import tempfile


def run_on_sponge_vm(ast_data):
    """
    Sponge VM 에 AST JSON 전달하고 실행 요청
    """

    with tempfile.NamedTemporaryFile("w", delete=False) as f:
        json.dump(ast_data, f)
        temp_path = f.name

    cmd = ["sponge-vm", "--run-json", temp_path]

    result = subprocess.run(cmd, capture_output=True, text=True)

    return result.stdout
