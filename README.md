# Batch Gradient Descent
Simple example of "Batch" Gradient Descent.

Our best hypothesis function is found by minimising the
sum of the squared difference between the prediction of y
and the actual value of y.

## Limitations
Gradient descent will find the local minimum from a given
start point, rather than the global minimum.

This doesn't matter in our example, for our choice
of cost function there is only one local minimum, therefore
the local and global minimum are the same.

The alpha parameter must be tweaked. If it is too large
it may diverge away from the minimum and may even cause
an overflow error. Too small and it may take too many
iterations to find the answer. 
