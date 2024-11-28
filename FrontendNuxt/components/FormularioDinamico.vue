<template>
  <div>
    <h1>Registro</h1>
    <form @submit.prevent="register">
      <input v-model="name" placeholder="Nombre" required />
      <input v-model="email" type="email" placeholder="Email" required />
      <input v-model="phone" placeholder="Teléfono" required />
      <button type="submit">Registrar</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const name = ref('')
const email = ref('')
const phone = ref('')

const register = async () => {
  try {
    await axios.post('http://localhost:8000/users/', { name: name.value, email: email.value, phone: phone.value })
    alert('Registro exitoso. Por favor, verifica tu email.')
  } catch (error) {
    console.error('Error en el registro:', error)
  }
}
</script>
