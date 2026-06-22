#!/home/davidomer/code/ops-and-sops/ops/portmason-py/.venv/bin/python
import sys
from portmason.commands.setup import main
if __name__ == '__main__':
    sys.argv[0] = sys.argv[0].removesuffix('.exe')
    sys.exit(main())
