<template>
  <div id="app">
    <hello></hello>
  </div>
</template>

<script>
var Hello = require('./components/Hello.vue'):

export default {
  name: 'app',
  components: {
    Hello
  }
}
</script>

<style media="screen">
  * {
    margin:0px;
    padding:0px;
  }
  body {
    background: black;
  }
</style>
