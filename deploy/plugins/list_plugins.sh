#!/bin/bash
# Bash strict mode: http://redsymbol.net/articles/unofficial-bash-strict-mode/
set -euo pipefail


source /fwego/plugins/utils.sh

simple_log "Installed Fwego Plugins:"
for plugin_folder in "$FWEGO_PLUGIN_DIR"/*; do
    if [[ -d "$plugin_folder" ]]; then
        plugin_name="$(basename -- "$plugin_folder")"
        simple_log " - $plugin_name"
        if [[ -f "$plugin_folder/fwego_plugin_info.json" ]]; then
            plugin_info="$(cat "$plugin_folder/fwego_plugin_info.json")"
            description=$(echo "$plugin_info" | python3 -c "import sys, json; print(json.load(sys.stdin).get('description', ''))" || "")
            simple_log "      description: $description"
        fi
    fi
done
