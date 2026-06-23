
import pytest

@pytest.fixture(scope='function')
def clear():
    print("setUP")
    yield
    print(f"\ncleanUP\n")

@pytest.fixture(scope='function')
def cleanUP():
    print("setUP")
    yield 'Didara'
    print(f"\ncleanUP")


def testSlean(clear):
    return clear


def testSetup(cleanUP):
    assert cleanUP == 'Didara'

import pytest

@pytest.fixture(scope='module')
def cleanUPwithMODULE():
    print("\n✨ SETUP: Creating expensive resource (module scope)")
    counter = {"calls": 0}
    yield counter
    print(f"\n✨ CLEANUP: Closing resource")

# TEST 1 ✅
def testFirstTimeNuraim(cleanUPwithMODULE):
    print("Test 1 - call")
    assert cleanUPwithMODULE["calls"] == 0

# TEST 2 - ADD THIS
def testSecondTimeNuraim(cleanUPwithMODULE):
    print("Test 2 - call")
    assert cleanUPwithMODULE["calls"] == 0

# TEST 3 - ADD THIS TOO
def testThirdTimeNuraim(cleanUPwithMODULE):
    print("Test 3 - call")
    assert cleanUPwithMODULE["calls"] == 0









