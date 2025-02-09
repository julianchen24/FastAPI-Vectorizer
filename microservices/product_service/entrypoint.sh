#!/bin/bash
set -e
CMD_STR="fastapi dev main.py --host 0.0.0.0 --port 82"
exec /bin/bash -c "$CMD_STR"
