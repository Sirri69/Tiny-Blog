import { Card } from 'antd';
import React, { useEffect, useState } from "react";
import { Switch } from 'antd';
import axios from "axios";

// export var check = useState(true);


function Post(props) {
	const [data, setData] = useState([]);
	useEffect(() => {
		axios.get('https://api.npoint.io/229c7f19b01068baedf7').then(res => {
			console.log(res.data);
			setData(res.data);
		});
	},[]);

	var elems = data.map((dict, id) => <Card title={dict.title} style={{ margin: "2.3vw 5.5vw 0vw 5.5vw" }} 
		cover={
      <img
        src={dict.img}
      />}>
      <p> {dict.excerpt} </p>
      </Card>
      );

	return(elems);

	// return(
	// 	<Card title="Default size card" extra={<a href="#">More</a>} style={{ margin: "2.3vw 5.5vw 0vw 5.5vw" }} 
	// 	cover={
 //      <img
 //        src="https://gw.alipayobjects.com/zos/rmsportal/JiqGstEfoWAOHiTxclqi.png"
 //      />}>
	// 		<p>Card content</p>
	// 		<p>Card content</p>
	// 		<p>Card content</p>
	// 	</Card>
	// 	);
}




export default Post;
const app = document.getElementById('app');