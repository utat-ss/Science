import numpy as np

#need acces to drive for the csv

def adding_snr_noise(refl_values):

    snr = 30

    #snr index
    snr_ratio = 1 / snr

    #intialize np array of zeros
    new_refl_values = np.zero_like(refl_values)

    #generate random noise for each reflectant
    random_gaussian = np.random.normal(loc=0, scale=1, size=refl_values.shape)

    #add noise to flectances
    scaled_noise = snr_ratio*random_gaussian*refl_values
    new_refl_values = scaled_noise + refl_values

    return new_refl_values








