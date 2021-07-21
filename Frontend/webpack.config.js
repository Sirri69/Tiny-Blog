module.exports = {
  'mode': 'development',
  entry:{
    index: {import: './src/index.js', dependOn: 'shared'},
    app: {import: './src/app.js', dependOn: 'shared'},
    shared: 'react'
  },
  output: {
     filename: '[name].js',
     path: 'E:\\Workplace\\Tiny-Blog\\Blog\\Frontend\\static\\frontend',
   },
  module: {
    rules: [
    {
      test: /\.js$/,
      exclude: /node_modules/,
      use: {loader: "babel-loader"}
    },
    {
      test: /\.css$/,
      use: [
      { loader: 'style-loader' },
      { loader: 'css-loader' }
      ]
    }
    ]
  }
};
