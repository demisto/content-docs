const path = require('path')
const MonacoWebpackPlugin = require('monaco-editor-webpack-plugin')
const MONACO_DIR = path.resolve(__dirname, './node_modules/monaco-editor')

module.exports = function (context, options) {
  return {
    name: 'monaco-editor',
    configureWebpack(config, isServer) {
      return {
        module: {
          rules: [
            {
              test: /\.css$/,
              include: MONACO_DIR,
              use: ['style-loader', 'css-loader']
            },
            {
              test: /\.ttf$/,
              use: ['file-loader']
            }
          ]
        },
        plugins: [new MonacoWebpackPlugin()]
      }
    }
  }
}
