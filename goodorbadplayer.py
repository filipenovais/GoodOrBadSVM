import pandas as pd
import numpy as np
from sklearn import svm
import matplotlib.pyplot as plt
import seaborn as sns; sns.set(font_scale=1.2)

# Read csv file
data = pd.read_csv('data.csv')

# Scatter plot
sns.lmplot('Playing', 'Learning', data=data, hue='Skill', fit_reg=False, legend_out=False, scatter_kws={"s": 70})
plt.legend(loc='upper right')
xmin, xmax, ymin, ymax = plt.axis()

# Choose features for the model
features = data[['Playing','Learning']].values
type_label = np.where(data['Skill']=='Good', 1, 0)

# Fit the SVM model
model = svm.SVC(kernel='linear')
model.fit(features, type_label)
#print(features)
#print(type_label)

# Get the separating hyperplane
w = model.coef_[0]
a = -w[0] / w[1]
xx = np.linspace(xmin, xmax)
yy = a * xx - (model.intercept_[0]) / w[1]
#print(model.coef_)

if 1:
    # Choose the right support_vectors to plot this scatter!!!!!
    #print(model.support_vectors_)

    # Calculate the parallels to the separating hyperplane that pass through the support vectors
    b = model.support_vectors_[2]
    yy_down = a * xx + (b[1] - a * b[0])
    b = model.support_vectors_[-2]
    yy_up = a * xx + (b[1] - a * b[0])

    # Plot the hyperplane and look at the margins and support vectors
    sns.lmplot('Playing', 'Learning', data=data, hue='Skill', fit_reg=False, legend_out=False, scatter_kws={"s": 70})
    plt.legend(loc='upper right')
    plt.plot(xx, yy, linewidth=2, color='black')
    plt.plot(xx, yy_down, 'k--')
    plt.plot(xx, yy_up, 'k--')
    plt.scatter(model.support_vectors_[:, 0], model.support_vectors_[:, 1], s=80, facecolors='none');
    axes = plt.gca()
    axes.set_ylim([ymin,ymax])
    plt.show()

# Classify good or bad player based on the model
def goodorbad(Playing, Learning):
    if(model.predict([[Playing, Learning]]))==0:
        print('\nYou\'re looking at a Bad Player!')
    else:
        print('\nYou\'re looking at a Good Player!')

    sns.lmplot('Playing', 'Learning', data=data, hue='Skill', fit_reg=False, legend_out=False, scatter_kws={"s": 70})
    plt.legend(loc='upper right')
    plt.plot(xx, yy, linewidth=2, color='black')
    plt.plot(Playing, Learning, 'yo', markersize='9');
    axes = plt.gca()
    axes.set_ylim([ymin, ymax])
    plt.show()

goodorbad(6,2)