import numpy as np

## Some Fixtures like Spectrum, arbitrary_index_single_eigenfunction, arbitrary_single_coefficient, arbitrary_index_multiple_eigenfunctions
## are defined in the conftest.py file.and imported in all the test files automatically.

########################################## HELPER FUNCTIONS ##########################################
def arbitrary_multiple_coefficients(length=1):
    """
    Python function to initialize a numpy array of the given length
    with arbitrary coefficients sampled from a normal distribution for the tests.
    """
    return np.random.randn(length)


############################################ TEST FUNCTION ############################################
# def test_transforms_from_real_to_spectral_basis(spectrum_fermion2D, 
#                                                 arbitrary_index_single_eigenfunction_fermion2D, 
#                                                 arbitrary_single_coefficient
#                                                 ):
#     """
#     Python test function to test the transformation of an eigenvector
#     from real space to spectral space.
#     """

#     eigenfunction = (arbitrary_single_coefficient * 
#                     spectrum_fermion2D.eigenfunction(
#                         arbitrary_index_single_eigenfunction_fermion2D)(*spectrum_fermion2D.lattice(output_basis="real"))
#                     )
#     result = spectrum_fermion2D.transform(eigenfunction, input_basis="real", output_basis="spectral")

#     length = 2 * spectrum_fermion2D.n_t * spectrum_fermion2D.n_x
#     expected = arbitrary_single_coefficient * np.eye(length)[arbitrary_index_single_eigenfunction_fermion2D, :]
#     assert np.isclose(expected, result).all()



def test_transforms_multiple_components_from_real_to_spectral_basis(spectrum_fermion2D, 
                                                                    arbitrary_index_multiple_eigenfunctions_fermion_2D):
    """
    Python test function to test the transformation of linear combination
    of eigenvectors from real space to spectral space.
    """

    arbitrary_coefficients = arbitrary_multiple_coefficients(len(arbitrary_index_multiple_eigenfunctions_fermion_2D))

    t, x = spectrum_fermion2D.lattice()
    eigenfunctions = spectrum_fermion2D.eigenfunction(arbitrary_index_multiple_eigenfunctions_fermion_2D)(t.reshape(-1, 1), x.reshape(-1, 1))
    result = spectrum_fermion2D.transform(
                np.sum(arbitrary_coefficients[:, np.newaxis] * eigenfunctions, axis = 0), 
                input_basis="real", output_basis="spectral"
            )

    expected = np.zeros(2 * spectrum_fermion2D.n_x * spectrum_fermion2D.n_t)
    expected[arbitrary_index_multiple_eigenfunctions_fermion_2D] = arbitrary_coefficients
    assert np.isclose(expected, result).all()


# def test_transforms_from_spectral_to_real_basis(spectrum, arbitrary_single_coefficient, arbitrary_index_single_eigenfunction):
#     """
#     Python test function to test the transformation of spectral coefficients
#     with a single component from spectral space to real space.
#     """

#     spectral_vector = arbitrary_single_coefficient * np.eye(spectrum.num_lattice_points)[arbitrary_index_single_eigenfunction, :]
#     result = spectrum.transform(spectral_vector, input_basis="spectral", output_basis="real")

#     sample_points = np.linspace(0, spectrum.L, spectrum.num_lattice_points, endpoint=False)
#     expected = arbitrary_single_coefficient * spectrum.eigenfunction(arbitrary_index_single_eigenfunction)(sample_points)
#     assert np.isclose(expected, result).all()


# def test_transforms_multiple_components_from_spectral_to_real_basis(spectrum, arbitrary_index_multiple_eigenfunctions):
#     """
#     Python test function to test the transformation of linear combination of eigenvectors
#     in spectral space with arbitrary coefficients to real space.
#     """

#     arbitrary_coefficients = arbitrary_multiple_coefficients(len(arbitrary_index_multiple_eigenfunctions))
#     spectral_coefficients = np.zeros(spectrum.num_lattice_points)
#     spectral_coefficients[arbitrary_index_multiple_eigenfunctions] = arbitrary_coefficients

#     # Transform from spectral space to real space
#     result = spectrum.transform(spectral_coefficients, input_basis="spectral", output_basis="real")

#     # Generate expected function values in real space
#     sample_points = np.linspace(0, spectrum.L, spectrum.num_lattice_points, endpoint=False)
#     eigenfunctions = spectrum.eigenfunction(arbitrary_index_multiple_eigenfunctions)(sample_points.reshape(-1, 1))
#     expected = eigenfunctions @ arbitrary_coefficients
#     assert np.isclose(expected, result).all()
