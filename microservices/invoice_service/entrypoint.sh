#!/bin/bash

set -e

CMD_STR="fastapi dev main-basic.py --host 0.0.0.0 --port 80"

exec /bin/bash -c "$CMD_STR"
