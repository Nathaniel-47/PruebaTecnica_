<template>
    <div>
      <h1>Generar Ganador</h1>
      <button @click="generateWinner">Generar Ganador</button>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
    methods: {
      async generateWinner() {
        try {
          const response = await axios.get('/api/generate-winner/')
          alert(response.data.message)
        } catch (error) {
          console.error(error)
        }
      }
    }
  }
  </script>
  