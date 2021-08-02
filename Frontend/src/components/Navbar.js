import { Menu, Switch as Sw  } from 'antd';
import React ,{ useState } from 'react';
import { HomeOutlined, QuestionOutlined, LoginOutlined, SettingOutlined } from '@ant-design/icons';
import 'antd/dist/antd.css';


var rightStyle = {position: 'absolute', top: 0, right: 0};
const { SubMenu } = Menu;

function onChange(checked) {
  console.log(`switch to ${checked}`);
  if (checked == true){
  		document.head.innerHTML  += '<link rel="stylesheet" id="dark" type="text/css" href="/static/css/antd.dark.min.css">';
  	}
  	if (checked == false){
  		let temp = document.getElementById('dark');
  		let k = temp.remove();
  	}
}


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
		</Menu>,
		<Menu mode="horizontal" style={rightStyle}>
			<SubMenu key="Submenu" icon={<SettingOutlined />} title="">

				<Menu.Item key="5">
				<Sw subMenuCloseDelay={0.25} checkedChildren="Dark" unCheckedChildren="Light" onChange={onChange}/>
				</Menu.Item>

			</SubMenu>
		</Menu>

	];

	if(props.isLoggedIn == false){
		
		elems.push(
			<Menu mode="horizontal" style={rightStyle}>
				<Menu.Item key="LogIn" icon={<LoginOutlined />}>
					<a href='/login'>
					Login
					</a>
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