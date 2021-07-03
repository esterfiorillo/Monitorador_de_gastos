<template>
    <div class="transaction-bar">
    <div class = "transaction-form">
        <input class="transaction-description" type="text" name="description" placeholder="Digite aqui sua transação">
        <input class="transaction-category" type="text" name="categoria" placeholder="Categoria">
        <input class="transaction-value" type="text" name="value" placeholder="Valor (R$)">
        <button class="button button1"> Adicionar </button>
      </div>
    </div>
</template>

<script>
export default {
    
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