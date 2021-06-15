import { Menu } from 'antd';
import React ,{ useState } from 'react';
import { HomeOutlined, QuestionOutlined, LoginOutlined } from '@ant-design/icons';
import 'antd/dist/antd.css';

function Navbar(props){
	const [current, setCurrent] = useState(['Home']);
	var elems = [
		<Menu selectedKeys={current} mode="horizontal">
			<Menu.Item key="Home" icon={<HomeOutlined />}>
				<a href='/'>
					Home
				</a>
			</Menu.Item>
			<Menu.Item key="About" icon={<QuestionOutlined />}>
				About
			</Menu.Item>
		</Menu>
	];

	if(props.isLoggedIn == false){
		const rightStyle = {position: 'absolute', top: 0, right: 0}
		elems.push(
			<Menu mode="horizontal" style={rightStyle}>
				<Menu.Item key="LogIn" icon={<LoginOutlined />}>
					Login
				</Menu.Item>
			</Menu>
			);
	}

	return(
		elems
		);
}

export default Navbar;

Navbar.defaultProps = {
	isLoggedIn: false
}