<template>
    <div class="transaction-bar">
    <form class = "transaction-form" method="post">
        <input class="transaction-description" type="text" v-model="description" name="description" placeholder="Digite aqui sua transação">
        <input class="transaction-category" type="text" v-model="category" name="categoria" placeholder="Categoria">
        <input id="__value" class="transaction-value" type="text" v-model="value" name="value" placeholder="Valor (R$)">
        <button type="button" @click="postMethod" class="button button1"> Adicionar </button>
      </form>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    props: {
      postURL: {type: String},
    },
    methods: {
      postData(data) {
        console.log("Postando!")
        axios.post(this.postURL, data)
          .then(() => {
            console.log("Postado!")
            window.location.reload()
          })
          .catch((error) => {
            console.log(error);
            window.location.reload()
          });
      },

      postMethod: function() {
        if (this.descricao == "" || this.valor == "" || this.categoria == "")
          return;

        const payload = {
          descricao: this.description,
          valor: this.value,
          categoria: this.category,
          timestamp:  new Date().getTime()
        }
        console.log("Criando payload!")
        console.log(payload)
        this.postData(payload)
      },
    }
}
</script>

<style>

.button {
  border: none;
  color: white;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  transition-duration: 0.4s;
  cursor: pointer;
}

.button1 {
  background-color: #0080ab; 
  color: white; 
}

.button1:hover {
  background-color: #25c3ff;
  color: white;
}

.transaction-form {
  margin: auto;
  margin-bottom: 40px;
  background-color: #5abbbd;
  width: 600px;
  height: 50px;
  display: flex;
  border: 1px black;
}

.transaction-form:focus {
    outline-color: black;
    outline-style: inset;
}

.transaction-description {
  width: 50%;
  font-family: sans-serif;
  font-size: 17px;
  color: #7c7c7c;
}

.transaction-value {
  width: 20%;

  font-family: sans-serif;
  font-size: 17px;
  color: #7c7c7c;
}

.transaction-category {
  width: 30%;
  font-family: sans-serif;
  font-size: 17px;
  color: #7c7c7c;
}

</style>