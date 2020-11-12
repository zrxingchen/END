const HtmlWebpackPlugin = require("html-webpack-plugin")
const path = require("path")
const webpack = require('webpack')

module.exports = {
    mode:"development",
    entry:"./src/index.js",
    output:{
        filename:'bundle.js',
        path:path.resolve(__dirname,'dict')
    },
    module:{
        rules:[
            {test:/\.js$/,use:"babel-loader"},
            {test:/\.css$/,use:["style-loader","css-loader"]},
            {test:/\.(png|jpg|gif|jpeg)$/,use:'file-loader'},
            {test:/\.(ttf|woff|woff2|eot|otf)$/,use:"file-loader"}
            
        ]
    },
    plugins:[
        new HtmlWebpackPlugin({
            template:"./src/index.html"
        }),
        new webpack.HotModuleReplacementPlugin()
    ],
    devServer:{
        host:"127.0.0.1",
        port:"8080",
        hot:true,
        open:true,
        contentBase:'./dict'
        
    }

}