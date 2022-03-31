# This code is part of OpenFE and is licensed under the MIT license.
# For details, see https://github.com/OpenFreeEnergy/gufe

class Protocol:
    """

    Attributes
    ----------

    """
    ...

    def __init__(
            self,
            chemicalstate_start,
            chemicalstate_end,
            settings=None):
        """

        """
        ...


class LigandSolventAtomMappedProtocol(Protocol):
    ...


class LigandComplexAtomMappedProtocol(Protocol):
    ...



# want a variant of the above based on engine, probably
# e.g. OpenMM, Gromacs
# since settings will be very different
# not exactly sure how to avoid long names here
