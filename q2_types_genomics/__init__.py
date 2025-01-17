# ----------------------------------------------------------------------------
# Copyright (c) 2023, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import importlib

from ._version import get_versions

__version__ = get_versions()['version']
del get_versions

importlib.import_module('q2_types_genomics.kraken2')
importlib.import_module('q2_types_genomics.feature_data')
importlib.import_module('q2_types_genomics.per_sample_data')
importlib.import_module('q2_types_genomics.genome_data')
importlib.import_module('q2_types_genomics.reference_db')
