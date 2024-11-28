<template>
    <div>
      <h1>Verificar Email</h1>
      <form @submit.prevent="verifyEmail">
        <input v-model="email" type="email" placeholder="Email" required />
        <input v-model="password" type="password" placeholder="Contraseña" required />
        <button type="submit">Verificar</button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import axios from 'axios'
  
  const email = ref('')
  const password = ref('')
  
  const verifyEmail = async () => {
    try {
      await axios.post('http://localhost:8000/verify/', { email: email.value, password: password.value })
      alert('Email verificado. Cuenta creada exitosamente.')
    } catch (error) {
      console.error('Error en la verificación:', error)
    }
  }
  </script>
  