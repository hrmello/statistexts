from tqdm import tqdm
import numpy as np
from scipy.optimize import curve_fit

####################
#### Parameters ####
####################
N_SUBSAMPLES = 100
sample_range = range(100,500,25)

def ttr(text):
    '''
    Lexical diversity measured by Type-Token Ratio, measured using the number of unique words 
    and the total number of words in the whole text
    
    This kind of measure is bad to compare texts of different lengths.
    For details see here https://en.wikipedia.org/wiki/Lexical_diversity
    '''
    return round(len(set(text))/len(text),2)

def select_random_subsample(text_from_tokens, sample_size):
    return np.random.choice(np.array(text_from_tokens), size = sample_size, replace = False)

def ttr_subsample(tokens):
    return len(set(tokens))/len(tokens)

def TTR_function(x, D):
    return np.multiply((D/x),((1+2*x/D)**(1/2) - 1), dtype = np.float)

def compute_D(text_from_tokens):
    '''
    This algorithm was implemented based on page 328 of the following paper:
    https://www.researchgate.net/publication/283149921_Measuring_Vocabulary_Diversity_Using_Dedicated_Software
    '''
    best_fit_ds = list()
    best_fit_ds_std = list()

    for i in range(0,3):
        ttr_step_list = list()
        std_ttr_step_list = list()
        D_sample = list()

        for N in tqdm(sample_range):
            ttr_sample_list = list()

            for i in range(N_SUBSAMPLES):
                random_tokens = select_random_subsample(text_from_tokens, N)
                ttr = ttr_subsample(random_tokens)
                ttr_sample_list.append(ttr)

            ttr_sample_list = np.array(ttr_sample_list)
            mean_ttr = ttr_sample_list.mean()        
            std_ttr = ttr_sample_list.std()
            ttr_step_list.append(mean_ttr); std_ttr_step_list.append(std_ttr)

            D = - N*(mean_ttr**2)/(2*(mean_ttr - 1))
            D_sample.append(D)

        D_avg = np.array(D_sample).mean()
        D_std = np.array(D_sample).std()
        best_D_fit, best_D_std = curve_fit(TTR_function, xdata = np.array(sample_range), ydata = np.array(ttr_step_list))
        best_fit_ds.append(best_D_fit)
        best_fit_ds_std.append(best_D_std)
        
    best_fit_ds = np.array(best_fit_ds)
    best_fit_ds_std = np.array(best_fit_ds_std)
    
    return best_fit_ds.mean(), best_fit_ds_std.mean() 
