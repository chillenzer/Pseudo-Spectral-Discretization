from pseudospectral import Derivative1D, FreeFermion2D
import pytest
import numpy as np

SPECTRA = [
    {"type": Derivative1D, "config": {"num_lattice_points": 3}},
    {"type": Derivative1D, "config": {"num_lattice_points": 101}},
    {"type": Derivative1D, "config": {"num_lattice_points": 3, "L": 3}},
    {"type": Derivative1D, "config": {"num_lattice_points": 101, "L": 42}},
]


################## Common Fixtures for PyTests ######################
@pytest.fixture(params=SPECTRA)
def spectrum(request):
    return request.param["type"](**request.param["config"])


@pytest.fixture
def arbitrary_index_single_eigenfunction(spectrum):
    """
    Python fixture to initialize the arbitrary index for the single eigenfunction test.
    """
    return np.random.randint(0, spectrum.num_lattice_points)


@pytest.fixture
def arbitrary_index_multiple_eigenfunctions(
    spectrum,
):
    """
    Python fixture to initialize the arbitrary index for the two eigenfunctions test.
    """
    return np.random.choice(spectrum.num_lattice_points, np.random.randint(spectrum.num_lattice_points), replace=False)


@pytest.fixture
def arbitrary_single_coefficient():
    """
    Python fixture to initialize the single coefficient for the tests.
    """
    return np.random.randn()


############################# FIXTURES FOR FERMION 2D ################

@pytest.fixture
def spectrum_fermion2D():
    """
    Python fixture to create an instance of the FreeFermions2D class for the tests.
    """
    return FreeFermion2D(n_t=3, n_x=3, L_t=1, L_x=1, mu=0, m=0, theta_t=0, theta_x=0)

@pytest.fixture
def arbitrary_index_single_eigenfunction_fermion2D(spectrum_fermion2D):
    """
    Python fixture to initialize the arbitrary index for the single eigenfunction test.
    """
    # return (np.random.randint(0, spectrum_fermion2D.n_t), 
            # np.random.randint(0, spectrum_fermion2D.n_x), 
            # np.random.choice([-1, 1]))
    return (1, 2, 1)