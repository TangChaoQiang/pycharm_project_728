# vue-base

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).


## Vue开发环境构建
###相关环境
1. Node:https://nodejs.org/en/
2. npm镜像
    cnpm:npm install -g cnpm --registry=https://registry.npm.taobao.org
3. webpack:构建工具
4. 开发工具:vsCode: https://code.visualstudio.com/5高亮现实:扩展→>搜索:Vetur
### 搭建Vue环境
1. 安装vuecli工具
```js
npm install -g @vue/cli
vue create 项目名
```

## Vue的基础知识
1. 模版语法
    1. 插值
        1. 文本: {{变量名}}
        2. 原始HTML: v-html
        3. 属性:v-bind:attr
        4. 模版语法使用限制:每个绑定都只能包含单个表达式
    2. 指令
    3. 缩写
        1. v-bind:缩写 > :
