import matplotlib.pyplot as plt

SCATTER_SIZE=2
DEFAULT_FIGURE_SIZE=(12,12)

def figure_size():
    plt.figure(figsize=DEFAULT_FIGURE_SIZE)

def print_map(data, show=True, color=None, size=SCATTER_SIZE, alpha=0.5, x=None, y=None):
    if show:
        figure_size()
        
    plt.axis('equal')
    
    if 'label_prioridade' in data.columns:
        groups = data.groupby('label_prioridade')
        for name, group in groups:
            c = group['cor'] if color == None else color
            label = group.iloc[0].loc['label']
            plt.scatter(group[x], group[y], s=size, alpha=alpha, c=c, label=label)
    else:
        c = data['cor'] if color == None else color
        plt.scatter(data[x], data[y], s=size, alpha=alpha, c=c)
        
    if show:
        plt.show()
        
def legend_for_map():
    # Sort labels of legend
    handles, labels = plt.gca().get_legend_handles_labels()
    labels, handles = zip(*sorted(zip(labels, handles), key=lambda t: t[0]))
    legend = plt.legend(handles, labels, fontsize=14)


    for handle in legend.legendHandles:
        handle._sizes = [50]
