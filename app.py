import streamlit as st
import pandas as pd
from streamlit_agraph.config import Config, ConfigBuilder
from streamlit_agraph import agraph, Node, Edge, Config
import json, os

#os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"


with open('codebase.json', 'r') as file:
    json_data = json.load(file)

nodes = []
edges = []

graph_result = None

if 'return' not in st.session_state:
    st.session_state['return'] = None
    st.session_state['selected_node'] = None

if 'node_color' not in st.session_state:
    st.session_state['node_color'] = None

method_color = "white"

for module_name, module_content in json_data.items():
    for parent in module_content:
        print(parent)
        # method belonging to no class
        if parent['category'] == "function":
            method_title = parent['title']
            # create a node for the method
            if st.session_state['return']:
                if st.session_state['selected_node'] and st.session_state['node_color'] and st.session_state['selected_node'] == method_title:
                    method_color = st.session_state['node_color']
                    st.session_state['node_color'] = None
                    st.session_state['selected_node'] = None
            method_node = Node(id=method_title, label=method_title, size=15, color=method_color)
            method_color = "white"
            nodes.append(method_node)
        elif parent['category'] == "class":
            class_title = parent['title']
            # create a node for the class
            class_node = Node(id=class_title, label=class_title, size=40, color='blue', shape="diamond")
            nodes.append(class_node)

        # check for subclasses
        if 'inner_classes' in parent:
            if len(parent['inner_classes']) != 0:
                subclasses = parent.get('inner_classes', [])
                for subclass in subclasses:
                    sub_title = subclass['title']
                    # create a node for the subclass and connect to parent class
                    subclass_node = Node(id=sub_title, label=sub_title, size=40, color='blue', shape="diamond")
                    nodes.append(subclass_node)
                    edge = Edge(source=sub_title, target=class_title, type='straight', color=method_color)
                    edges.append(edge)

                #find methods of each subclass
                methods = subclass.get('methods', [])
                for method in methods:
                    method_title = method['title']
                    # create a node for the method
                    if st.session_state['return']:
                        if st.session_state['selected_node'] and st.session_state['node_color'] and st.session_state['selected_node'] == method_title:
                            method_color = st.session_state['node_color']
                            st.session_state['node_color'] = None
                            st.session_state['selected_node'] = None
                    method_node = Node(id=method_title, label=method_title, size=15, color='blue')
                    method_color = "white"
                    nodes.append(method_node)
                    # create an edge from the method to the class
                    edge = Edge(source=method_title, target=sub_title, type='straight', color=method_color)
                    edges.append(edge)


        # iterate through the methods of the parent class
        methods = parent.get('methods', [])
        for method in methods:
            method_title = method['title']
            # create a node for the method
            if st.session_state['return']:
                       if st.session_state['return']:
                            if st.session_state['selected_node'] and st.session_state['node_color'] and st.session_state['selected_node'] == method_title:
                                method_color = st.session_state['node_color']
                                st.session_state['node_color'] = None
                                st.session_state['selected_node'] = None
            method_node = Node(id=method_title, label=method_title, size=15, color=method_color)
            method_color = "white"
            nodes.append(method_node)
            # create an edge from the method to the class
            edge = Edge(source=method_title, target=class_title, type='straight', color="white")
            edges.append(edge)


config = Config(
    width=800,
    height=600,
    directed=True,
    physics=True,
    hierarchical=True,
    nodeHighlightBehavior=True,
    textColor="FFFFFF",
    highlightColor="#F7A7A6",  # color when hovering over nodes
    collapsible=False
)

st.title("TestBuddy")

#st.write(f"previous state {st.session_state['selected_node']}")
graph_result = agraph(nodes=nodes, edges=edges, config=config)

## update when graph node is clicked
#if 'graph_result' not in st.session_state:
#    st.session_state['selected_node'] = None

if graph_result:
    st.session_state['selected_node'] = graph_result
    st.switch_page('pages/method.py')