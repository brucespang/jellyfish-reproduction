import sys
import os
import subprocess
import time

import mininet
import mininet.clean
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import lg, info
from mininet.link import TCLink, Link, TCIntf
from mininet.node import Node, OVSKernelSwitch, RemoteController
from mininet.topo import Topo
from mininet.util import waitListening,custom

def graph_to_topo(graph):
    """
    Builds a mininet Topology for a graph

    Parameters
    ----------
    graph : nx.Graph

    Returns
    -------
    mininet.Topo
    """

    raise Exception("Not implemented")

def make_mininet(graph):
    """
    Constructs a mininet instance for a graph

    Parameters
    ----------
    graph : nx.Graph
        a graph generated by jellyfish.graphs

    Returns
    -------
    mininet.net.Mininet
    """
    topo = graph_to_topo(graph)

    # pox controller
    pox = RemoteController("c1", ip="127.0.0.1", port=6633)
    
    return Mininet(topo=topo, controller=pox, autoSetMacs=True)

def run(graph):
    """
    Runs the mininet CLI for a graph

    Parameters
    ----------
    graph : nx.Graph
      a graph generated by jellyfish.graphs
    """
    lg.setLogLevel('info')

    mininet.clean.cleanup()
    net = make_mininet(graph)
    
    net.start()
    CLI(net)
    net.stop()
