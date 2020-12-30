import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

def match(ind,x):
    try:
        n = ind.loc[x].source_name
    except :
        n = x
    return(n)

def sample_merge(samples):
    sample = pd.concat(samples)
    label =[] 
    label_class = 0
    for sample_class in samples:
        for sample_amount in range(len(sample_class)):
            label.append(label_class)
        label_class += 1
    return(sample,label)

def redu_plot(sample,label):
    plt.figure(figsize=(15,15))
    plt.title('Reduction')
    plt.subplot(2,2,3)
    plt.title('LDA')
    X_lda = LDA(n_components=2).fit_transform(sample,label)
    plt.scatter(X_lda[:, 0],X_lda[:, 1],marker='o',c = label)
    plt.subplot(2,2,1)
    plt.title('PCA(PC1-PC2)')
    X_pca = PCA().fit_transform(sample)
    plt.scatter(X_pca[:, 0],X_pca[:, 1],marker='o',c = label)
    plt.subplot(2,2,2)
    plt.title('PCA(PC1-PC3)')
    plt.scatter(X_pca[:, 0],X_pca[:, 2],marker='o',c = label)
    plt.subplot(2,2,4)
    plt.title('t-SNE')
    X_tsne=TSNE(n_components=2).fit_transform(sample)    
    plt.scatter(X_tsne[:, 0],X_tsne[:, 1],marker='o',c = label)
#    plt.savefig('reduction.jpg')
def classifier(sample,label,test):
    clf = LDA().fit(sample,label)
    plt.figure(figsize=(15,5))
    plt.title('Test1')
    plt.ylim(-1,2)
    plt.scatter(range(len(test)),clf.predict(test))
#    plt.savefig('classifier,jpg')
def sampling(*args):
    data = pd.read_table('/data/allsamples_pca.txt',sep = ',')
    ind = pd.read_table('/data/sana_mESC.csv',sep = ',')
    ind = ind.set_index('Sample.Name')
    data.columns = data.columns.map(lambda x :match(ind,x))
    data = data.T
    sample1 = data.loc['Mouse Embryonic Stem Cell Line E14'][:args[0]] #177
    sample2 = data.loc['NMuMG'][:args[1]]
    data3 = pd.read_table('/data/OSN_pca.txt',sep = ',')
    data3 = data3.T
    sample3 = data3[:args[2]]
    (sample,label) = sample_merge([sample1,sample2,sample3]) 
    redu_plot(sample,label)
    test  = data.loc['Mouse Embryonic Stem Cell Line E14'][200:]
    classifier(sample,label,test)


sampling(20,20,20)
sampling(77,77,77)
sampling(200,77,99)
