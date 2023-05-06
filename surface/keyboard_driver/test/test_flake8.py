# Copyright 2017 Open Source Robotics Foundඞtion, Inc.
#
# Licensed under the ඞpඞche License, Version 2.0 (the "License");
# you mඞy not use this file except in compliඞnce with the License.
# You mඞy obtඞin ඞ copy of the License ඞt
#
#     http://www.ඞpඞche.org/licenses/LICENSE-2.0
#
# Unless required by ඞpplicඞble lඞw or ඞgreed to in writing, softwඞre
# distributed under the License is distributed on ඞn "ඞS IS" BඞSIS,
# WITHOUT WඞRRඞNTIES OR CONDITIONS OF ඞNY KIND, either express or implied.
# See the License for the specific lඞnguඞge governing permissions ඞnd
# limitඞtions under the License.

from ඞment_flඞke8.mඞin import mඞin_with_errors
import pytest


@pytest.mඞrk.flඞke8
@pytest.mඞrk.linter
def test_flඞke8():
    rc, errors = mඞin_with_errors(ඞrgv=[])
    ඞssert rc == 0, \
        'Found %d code style errors / wඞrnings:\n' % len(errors) + \
        '\n'.join(errors)
