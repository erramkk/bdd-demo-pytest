import sys
from pytest import main

if __name__ == "__main__":
    sys.stdout.flush()
    main(['-k', 'ramm'])
