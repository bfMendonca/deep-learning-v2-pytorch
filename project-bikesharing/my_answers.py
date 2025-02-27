import numpy as np


class NeuralNetwork(object):
    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):
        # Set number of nodes in input, hidden and output layers.
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes

        # Initialize weights
        self.weights_input_to_hidden = np.random.normal(0.0, self.input_nodes**-0.5, 
                                       (self.input_nodes, self.hidden_nodes))

        self.weights_hidden_to_output = np.random.normal(0.0, self.hidden_nodes**-0.5, 
                                       (self.hidden_nodes, self.output_nodes))
        self.lr = learning_rate

        
        # Note: in Python, you can define a function with a lambda expression,
        # as shown below.
        self.activation_function = lambda x : 1.0/(1.0+np.exp(-x))
        
        self.activation_function_derivative = lambda x : x*(1-x)

    def train(self, features, targets):
        ''' Train the network on batch of features and targets. 
        
            Arguments
            ---------
            
            features: 2D array, each row is one data record, each column is a feature
            targets: 1D array of target values
        
        '''
        n_records = features.shape[0]
        delta_weights_i_h = np.zeros(self.weights_input_to_hidden.shape)
        delta_weights_h_o = np.zeros(self.weights_hidden_to_output.shape)
        
        for X, y in zip(features, targets):            
            # Implement the forward pass function below
            final_outputs, hidden_outputs = self.forward_pass_train(X)  

            # Implement the backproagation function below
            delta_weights_i_h, delta_weights_h_o = self.backpropagation(final_outputs, hidden_outputs, X, y, 
                                                                        delta_weights_i_h, delta_weights_h_o)
        
        self.update_weights(delta_weights_i_h, delta_weights_h_o, n_records)


    def forward_pass_train(self, X):
        ''' Implement forward pass here 
         
            Arguments
            ---------
            X: features batch

        '''
        #### Implement the forward pass here ####
        ### Forward pass ###
       
    
        hidden_inputs = X
        hidden_outputs = self.activation_function( np.dot( hidden_inputs, self.weights_input_to_hidden ) )
        
        final_inputs = hidden_outputs
        final_outputs = np.dot( final_inputs, self.weights_hidden_to_output )
        
        return final_outputs, hidden_outputs

    def backpropagation(self, final_outputs, hidden_outputs, X, y, delta_weights_i_h, delta_weights_h_o):
        ''' Implement backpropagation
         
            Arguments
            ---------
            final_outputs: output from forward pass
            y: target (i.e. label) batch
            delta_weights_i_h: change in weights from input to hidden layers
            delta_weights_h_o: change in weights from hidden to output layers

        '''
        #### Implement the backward pass here ####
        ### Backward pass ###

        # Output layer error is the difference between desired target and actual 
        error =(y - final_outputs)
        output_error_term = error

        hidden_error = np.dot( output_error_term, self.weights_hidden_to_output.T )
        hidden_error_term = hidden_error*self.activation_function_derivative( hidden_outputs )
       
        #delta_weights_i_h += np.dot( X.T, hidden_error_term )
        #delta_weights_h_o += np.dot( hidden_outputs.T, output_error_term )
        
        delta_weights_i_h += hidden_error_term * X[:, None ]
        delta_weights_h_o += output_error_term * hidden_outputs[:, None]
        
        return delta_weights_i_h, delta_weights_h_o

    def update_weights(self, delta_weights_i_h, delta_weights_h_o, n_records):
        ''' Update weights on gradient descent step
         
            Arguments
            ---------
            delta_weights_i_h: change in weights from input to hidden layers
            delta_weights_h_o: change in weights from hidden to output layers
            n_records: number of records

        '''
        
        # update hidden-to-output weights with gradient descent step
        self.weights_input_to_hidden += self.lr*delta_weights_i_h / n_records 
        
        # update input-to-hidden weights with gradient descent step
        self.weights_hidden_to_output += self.lr*delta_weights_h_o / n_records 
       

    def run(self, features):
        ''' Run a forward pass through the network with input features 
        
            Arguments
            ---------
            features: 1D array of feature values
        '''
        
        #### Implement the forward pass here ####       
        
        final_outputs, hidden_outputs = self.forward_pass_train( features )
        
        return final_outputs
       

#########################################################
# Set your hyperparameters here
##########################################################
iterations = 2000
learning_rate = 1.1
hidden_nodes = 10
output_nodes = 1
