
# 梯度下降与误差曲面核心段落解析

### 1. 神经网络的函数逼近能力与参数设定
In the previous chapter we saw that neural networks are a very broad and flexible class of functions and are able in principle to approximate any desired function to arbitrarily high accuracy given a sufficiently large number of hidden units.

Moreover, we saw that deep neural networks can encode inductive biases corresponding to hierarchical representations, which prove valuable in a wide range of practical applications.

We now turn to the task of finding a suitable setting for the network parameters (weights and biases), based on a set of training data.

### 2. 基于梯度的误差函数优化
As with the regression and classification models discussed in earlier chapters, we choose the model parameters by optimizing an error function.

We have seen how to define a suitable error function for a particular application by using maximum likelihood.

Although in principle the error function could be minimized numerically through a series of direct error function evaluations, this turns out to be very inefficient.

Instead, we turn to another core concept that is used in deep learning, which is that optimizing the error function can be done much more efficiently by making use of gradient information, in other words by evaluating the derivatives of the error function with respect to the network parameters.

This is why we took care to ensure that the function represented by the neural network is differentiable by design.

Likewise, the error function itself also needs to be differentiable.

### 3. 反向传播算法的高效导数计算
The required derivatives of the error function with respect to each of the parameters in the network can be evaluated efficiently using a technique called backpropagation, which involves successive computations that flow backwards through the network in a way that is analogous to the forward flow of function computations during the evaluation of the network outputs.

### 4. 泛化能力与正则化的重要性
Although the likelihood is used to define an error function, the goal when optimizing the error function in a neural network is to achieve good generalization on test data.

In classical statistics, maximum likelihood is used to fit a parametric model to a finite data set, in which the number of data points typically far exceeds the number of parameters in the model.

The optimal solution has the maximum value of the likelihood function, and the values found for the fitted parameters are of direct interest.

By contrast, modern deep learning works with very rich models containing huge numbers of learnable parameters, and the goal is never simply exact optimization.

Instead, the properties and behaviour of the learning algorithm itself, along with various methods for regularization, are important in determining how well the solution generalizes to new data.

### 5. 权重空间与误差曲面的几何直观
Our goal during training is to find values for the weights and biases in the neural network that will allow it to make effective predictions.

For convenience we will group these parameters into a single vector w, and we will optimize w by using a chosen error function E(w).

At this point, it is useful to have a geometrical picture of the error function, which we can view as a surface sitting over ‘weight space’, as shown in Figure 7.1.

### 6. 驻点与梯度的数学性质
First note that if we make a small step in weight space from w to w + δw then the change in the error function is given by

δE ≈ δwᵀ∇E(w) (7.1)

where the vector ∇E(w) points in the direction of the greatest rate of increase of the error function.

Provided the error E(w) is a smooth, continuous function of w, its smallest value will occur at a point in weight space such that the gradient of the error function vanishes, so that

∇E(w) = 0, (7.2)

as otherwise we could make a small step in the direction of −∇E(w) and thereby further reduce the error.

Points at which the gradient vanishes are called stationary points and may be further classified into minima, maxima, and saddle points.

### 7. 误差曲面的非线性与等效极小值
We will aim to find a vector w such that E(w) takes its smallest value.

However, the error function typically has a highly nonlinear dependence on the weights and bias parameters, and so there will be many points in weight space at which the gradient vanishes (or is numerically very small).

Indeed, for any point w that is a local minimum, there will generally be other points in weight space that are equivalent minima.

For instance, in a two-layer network of the kind shown in Figure 6.9, with M hidden units, each point in weight space is a member of a family of M!2ᴹ equivalent points.

### 8. 全局极小值与局部极小值
Furthermore, there may be multiple non-equivalent stationary points and in particular multiple non-equivalent minima.

A minimum that corresponds to the smallest value of the error function across the whole of w-space is said to be a global minimum.

Any other minima corresponding to higher values of the error function are said to be local minima.

The error surfaces for deep neural networks can be very complex, and it was thought that gradient-based methods might become trapped in poor local minima.

In practice, this seems not to be the case, and large networks can reach solutions with similar performance under a variety of initial conditions.

### 9. 误差函数的局部二次近似与泰勒展开
Insight into the optimization problem and into the various techniques for solving it can be obtained by considering a local quadratic approximation to the error function.

The Taylor expansion of E(w) around some point w̃ in weight space is given by

E(w) ≈ E(w̃) + (w - w̃)ᵀb + ½(w - w̃)ᵀH(w - w̃) (7.3)

where cubic and higher terms have been omitted.

Here b is defined to be the gradient of E evaluated at w̃

b ≡ ∇E|w=w̃ (7.4)

The Hessian is defined to be the corresponding matrix of second derivatives

H(w̃) ≡ ∇∇E(w)|w=w̃ (7.5)

If there is a total of W weights and biases in the network, then w and b have length W and H has dimensionality W × W.

From (7.3), the corresponding local approximation to the gradient is given by

∇E(w) ≈ b + H(w - w̃). (7.6)

For points w that are sufficiently close to w̃, these expressions will give reasonable approximations for the error and its gradient.

### 10. 海森矩阵与二阶导数信息
The Hessian matrix, denoted as H, plays a crucial role in understanding the local curvature of the error surface. While the gradient provides the direction of steepest ascent, the Hessian tells us how the gradient itself changes as we move through weight space. In the context of the quadratic approximation, the eigenvalues of the Hessian determine the shape of the local error surface: positive eigenvalues indicate directions of positive curvature (local minima), while negative eigenvalues indicate directions of negative curvature (saddle points or maxima). Computing the full Hessian is often computationally prohibitive for large networks, but approximations or partial second-order information can still be valuable for advanced optimization algorithms.

### 11. 优化算法的实践考量
In practice, the choice of optimization algorithm depends on the scale of the problem and the available computational resources. First-order methods like stochastic gradient descent (SGD) and its adaptive variants (e.g., Adam, RMSprop) are widely used because they only require gradient computations and scale well to large datasets and high-dimensional parameter spaces. Second-order methods, while theoretically offering faster convergence near optima, are rarely used in their pure form for deep learning due to the high cost of computing and storing the Hessian matrix. However, the theoretical insights gained from second-order analysis, such as the conditioning of the Hessian, inform the design of preconditioners and adaptive learning rate schedules that effectively approximate second-order behavior at a fraction of the computational cost.