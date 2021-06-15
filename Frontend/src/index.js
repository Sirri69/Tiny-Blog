import React from "react"
import {render} from "react-dom"
import {
	BrowserRouter as Router,
	Switch,
	Route
} from "react-router-dom"

import Navbar from './components/Navbar.js'
import "../static/css/style.css";


const App = (props) => ([<Navbar isLoggedIn={false}/>]); 
const container = document.getElementById("app");
render(
	<Router>
		<Switch>
			<Route exact path='/' component={()=><Navbar isLoggedIn={false}/>}/>
		</Switch>
	</Router>


	, container);