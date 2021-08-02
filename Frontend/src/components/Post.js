import { Card } from 'antd';
import React, { useEffect, useState } from "react";
import { Switch } from 'antd';

// export var check = useState(true);


function Post(props) {
	
	return(
		<Card title="Default size card" extra={<a href="#">More</a>} style={{ margin: "2.3vw 5.5vw 0vw 5.5vw" }}>
			<p>Card content</p>
			<p>Card content</p>
			<p>Card content</p>
		</Card>
		)
}




export default Post;
const app = document.getElementById('app');