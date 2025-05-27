# ACMInductions

hello just as a little bit of a background i knew nothing about ML or DL up until 3 months ago. Ive taught myself all of this w all the concepts and a bit of the math involved too. Thank you for your time hope youll find my code sufficient

-------------------------

Also a small note for the FashionMNIST analysis:

We would expect something as advanced as the ResNet model to be performing better than a basic CNN but in this case : 

Observation:

The basic CNN slightly outperformed the ResNet-like model in terms of test accuracy.


Analysis:

FashionMNIST is a small, low-complexity dataset with grayscale images of size 28×28 — it doesn't require very deep networks.

The basic CNN is lightweight, fast to train, and sufficient to capture necessary features.

The ResNet-like model, though more complex, introduces skip connections and BatchNorm, which are more beneficial in deeper networks or more challenging datasets.

On simple datasets, such extra layers can act as a form of regularization, slightly hindering performance.


Conclusion:

For simple datasets like FashionMNIST, a basic CNN is more efficient and effective.

ResNet-style architectures are better suited for deeper models and more complex tasks, where their design can truly shine.