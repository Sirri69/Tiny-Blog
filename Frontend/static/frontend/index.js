import React, {Component} from "react"
import {render} from "react-dom"


const App = ()=> "<H1> Hi <H1/>";

const container = document.getElementById("app");
render(<App />, container);