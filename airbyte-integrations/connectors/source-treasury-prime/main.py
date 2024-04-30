#
# Copyright (c) 2024 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_treasury_prime import SourceTreasuryPrime

if __name__ == "__main__":
    source = SourceTreasuryPrime()
    launch(source, sys.argv[1:])
