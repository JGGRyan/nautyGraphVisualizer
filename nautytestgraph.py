import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors

# Load graphs from your specific path
graphs = nx.read_graph6(r"C:\Projects\nautytesting\graph.g6")

# Global min/max for normalized color legends
vmin, vmax = 0, 1

for i, G in enumerate(graphs):  # iterate over all graphs
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    pos = nx.spring_layout(G, seed=42)  # consistent layout

    # --- Property 1: Degree ---
    degrees = [G.degree(n) for n in G.nodes()]
    cmap = cm.Reds
    norm = colors.Normalize(vmin=vmin, vmax=vmax)
    nx.draw(G, pos=pos, ax=axes[0], node_color=degrees, cmap=cmap, node_size=800, with_labels=False)
    labels_degree = {n: f"{n}\n{degrees[n]:.0f}" for n in G.nodes()}  # node number + specific subplot metric
    nx.draw_networkx_labels(G, pos=pos, labels=labels_degree, ax=axes[0], font_color='black')
    axes[0].set_title("Degree")
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=axes[0])
    cbar.set_ticks([0, 1])
    cbar.set_ticklabels(["Min", "Max"])

    # --- Property 2: Clustering coefficient ---
    clustering = list(nx.clustering(G).values())
    cmap2 = cm.Greens
    norm2 = colors.Normalize(vmin=0, vmax=1)
    nx.draw(G, pos=pos, ax=axes[1], node_color=clustering, cmap=cmap2, node_size=800, with_labels=False)
    labels_clust = {n: f"{n}\n{clustering[n]:.2f}" for n in G.nodes()} # node number + specific subplot metric
    nx.draw_networkx_labels(G, pos=pos, labels=labels_clust, ax=axes[1], font_color='black')
    axes[1].set_title("Clustering")
    sm2 = plt.cm.ScalarMappable(cmap=cmap2, norm=norm2)
    sm2.set_array([])
    cbar2 = fig.colorbar(sm2, ax=axes[1])
    cbar2.set_ticks([0, 1])
    cbar2.set_ticklabels(["Min", "Max"])

    # --- Property 3: Betweenness centrality ---
    betw = list(nx.betweenness_centrality(G).values())
    cmap3 = cm.Blues
    norm3 = colors.Normalize(vmin=0, vmax=1)
    nx.draw(G, pos=pos, ax=axes[2], node_color=betw, cmap=cmap3, node_size=800, with_labels=False)
    labels_betw = {n: f"{n}\n{betw[n]:.2f}" for n in G.nodes()} # node number + specific subplot metric
    nx.draw_networkx_labels(G, pos=pos, labels=labels_betw, ax=axes[2], font_color='black')
    axes[2].set_title("Betweenness")
    sm3 = plt.cm.ScalarMappable(cmap=cmap3, norm=norm3)
    sm3.set_array([])
    cbar3 = fig.colorbar(sm3, ax=axes[2])
    cbar3.set_ticks([0, 1])
    cbar3.set_ticklabels(["Min", "Max"])

    plt.suptitle(f"Upper number is node ID, Lower number is subplot metric value \n\n Graph {i}")
    plt.tight_layout()
    plt.show(block=False)

    # Wait for Enter or exit if window closed
    try:
        input("Press Enter to show next graph (or close the window to exit)...")
        if not plt.fignum_exists(fig.number):
            print("Figure closed. Exiting.")
            break
    except KeyboardInterrupt:
        print("Interrupted. Exiting.")
        break

    plt.close(fig)