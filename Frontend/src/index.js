import React from "react"
import {render} from "react-dom"
import {
	BrowserRouter as Router,
	Switch,
	Route
} from "react-router-dom"

import Navbar from './components/Navbar.js'
import "../static/css/style.css";


const Index = (props) => ([<Navbar isLoggedIn={isLoggedIn}/>]);
const LogIn = (props) => ([<Navbar isLoggedIn={isLoggedIn}/>]);
const SignUp = (props) => ([<Navbar isLoggedIn={isLoggedIn}/>]);

const container = document.getElementById("app");
render(
	<Router>
		<Switch>
			<Route exact path='/' component={Index}/>
			<Route exact path='/login' component={LogIn}/>
			<Route exact path='/signup' component={SignUp}/>
		</Switch>
	</Router>


	, container);