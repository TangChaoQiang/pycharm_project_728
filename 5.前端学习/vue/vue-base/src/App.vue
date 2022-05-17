<template>
  <div id="app">
    <input type="text" v-model="input_data">
    <button @click="add_data()">添加</button>
    <ul>
      <li v-for="data in list_data" :key="data.id">{{data}}</li>
    </ul>
  </div>
</template>

<script>
export default {
  data(){
  return {
    list_data:["tang1", "tang2", "tang3"],
    input_data:''
  }
},
  methods:{
    add_data(){
      if (this.input_data){
        this.list_data.push(this.input_data)
      }
      else
        alert("請添加有效字符")
      this.input_data=''
    }
  },
  components: {
  }
}
function sayHi(params) {
  
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
