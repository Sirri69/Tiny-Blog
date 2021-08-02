import React from "react"
import {render} from "react-dom"

import {
	BrowserRouter as Router,
	Switch,
	Route
} from "react-router-dom"

import Navbar from "./components/Navbar.js"
import Post from "./components/Post.js"

import "antd/dist/antd.css";

var isLoggedIn = true;
const Home = (props) => ([<Navbar isLoggedIn={isLoggedIn}/>,
						<Post/>,
							]);

const container = document.getElementById("app");
render(
	<Router>
		<Switch>
			<Route exact path='/home' component={Home}/>
		</Switch>
	</Router>


	, container);


console.log('Test');