# exercise 5.1.6
import numpy as np
from sklearn import tree
import graphviz
import os
os.chdir("C:\\Users\\andre\\Documents\\Machine Learning\\02450Toolbox_Python")
os.getcwd()
# requires data from exercise 5.1.4
from ex5_1_5 import *

# Fit regression tree classifier, Gini split criterion, pruning enabled
dtc = tree.DecisionTreeClassifier(criterion='gini', min_samples_split=100)
dtc = dtc.fit(X,y)

# Export tree graph for visualization purposes:
# (note: you can use i.e. Graphviz application to visualize the file)
#out = tree.export_graphviz(dtc, out_file='tree_gini_Wine_data.dot', feature_names=attributeNames)
out1 = tree.export_graphviz(dtc, out_file='tree_gini_Wine_data.dot', feature_names=attributeNames)
graph = graphviz.Source(out1)
graph.render('dtree_render',view=True)
#src=graphviz.Source.from_file('tree_gini_Wine_data.gvz')
#src.render('.\\tree_gini_Wine_data.gvz', view=True)
print('Ran Exercise 5.1.6')
