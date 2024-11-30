import streamlit as st
import pandas as pd
from streamlit_agraph.config import Config, ConfigBuilder
from streamlit_agraph import agraph, Node, Edge, Config
import json


json_data = [
    {
        "title": "Calculator",
        "attributes": [

        ],
        "methods": [
            {
                "title": "multiply",
                "parameters": "(self, a, b)"
            },
            {
                "title": "divide",
                "parameters": "(self, a, b)"
            }
        ]
    }
]



nodes = []
edges = []

for cls in json_data:
    class_title = cls['title']
    # Create a node for the class
    class_node = Node(id=class_title, label=class_title, size=25, color='blue')
    nodes.append(class_node)

    # Iterate through the methods of the class
    methods = cls.get('methods', [])
    for method in methods:
        method_title = method['title']
        # Create a node for the method
        method_node = Node(id=method_title, label=method_title, size=15, color='green')
        nodes.append(method_node)
        # Create an edge from the method to the class
        edge = Edge(source=method_title, target=class_title, label='belongs_to', type='straight', color='grey')
        edges.append(edge)


config = Config(
    width=800,
    height=600,
    directed=True,
    physics=True,
    hierarchical=True,
    nodeHighlightBehavior=True,
    highlightColor="#F7A7A6",  # Color when hovering over nodes
    collapsible=False
)

st.title("Class and Methods Visualization")

agraph(nodes=nodes, edges=edges, config=config)




'''
nodes.append(Node(id="Spiderman", 
                   label="Peter Parker", 
                   size=25, 
                   shape="square",
                   color="#6fa8dc")
            ) # includes **kwargs
nodes.append( Node(id="Captain_Marvel",
                   label="Captain Marvel",
                   size=25,
                   shape="diamond",
                   image="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_captainmarvel.png") 
            )
edges.append( Edge(source="Captain_Marvel", 
                   label="friend_of", 
                   target="Spiderman", 
                   # **kwargs
                   ) 
            ) 

config = Config(width=1200,
                height=1200,
                directed=True, 
                physics=True, 
                hierarchical=True,
                # **kwargs
                )

return_value = agraph(nodes=nodes, 
                      edges=edges, 
                      config=config)
'''