import os
import json
from pathlib import Path

//define the location of OS Appdata folder
def patch_brave_origin():
    base = Path(os.environ["LOCALAPPDATA"])

    state_file = (
        base /
        "BraveSoftware" /
        "Brave-Origin-Nightly" /
        "User Data" /
        "Local State"
    )

    if not state_file.exists():
        print("Local State file not found!")
        return

    try:
        data = json.loads(state_file.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"Failed to read JSON: {e}")
        return
//Tells Brave Origin that the product has been puchased
    brave_cfg = data.get("brave", {})
    brave_cfg["origin"] = {
        "purchase_validated": True
    }
    data["brave"] = brave_cfg

    sku_payload = {
        "credentials": {
            "items": {
                "dobrylicka": "1"
            }
        }
    }

    data["skus"] = {
        "state": {
            "1": json.dumps(sku_payload, separators=(",", ":"))
        }
    }

    try:
        state_file.write_text(
            json.dumps(data, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )

        print("Done.")
    except Exception as e:
        print(f"Failed to save file: {e}")

if __name__ == "__main__":
    patch_brave_origin()
