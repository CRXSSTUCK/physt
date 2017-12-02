import numpy as np

from .schema import Schema

__all__ = ["Histogram",]


class Histogram:
    """

    Attributes
    ----------
    - values
    - bins
    
    """
    def __init__(self, schema: Schema, values: np.ndarray):
        # self.dtype = int
        self._values = values
        self._schema = schema

    @property
    def schema(self):
        return self._schema

    @property
    def bins(self) -> np.ndarray:
        return self._schema.bins

    @property
    def values(self) -> np.ndarray:
        return self._values

    def __array__(self) -> np.ndarray:
        """Convert to numpy array.

        Returns
        -------
        np.ndarray
            The array of frequencies

        See also
        --------
        frequencies
        """
        return self.values

    def copy(self, shallow:bool=False) -> 'Histogram':
        """"Create an identical copy of the histogram.
        
        Parameters
        ----------
        shallow:
            If True, the values are not copied, but shared.
        """
        new_schema = self._schema.copy()
        new_values = self._values if shallow else self._values.copy()

        return self.__class__(schema=schema, values=values)

    def normalize(self, inplace=False) -> 'Histogram':
        if not inplace:
            copy = self.copy(shallow=True)
            return copy.normalize(inplace=False)
        else:
            # TODO: Make sure to convert to float
            self.values = self.values / self.values.sum()
            return self
    
    @property
    def densities(self) -> np.ndarray:
        pass
