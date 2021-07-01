<template>
    <div class="transaction-bar">
    <div class = "transaction-form">
        <input class="transaction-description" type="text" name="description" placeholder="Digite aqui sua transação">
        <input class="transaction-value" type="text" name="value" placeholder="Valor (R$)">
        <select class="transaction-category" name="category"> 
            <option value="geral">Geral</option>
            <option value="outros">Outros</option>            
        </select>
      </div>
    </div>
</template>

<script>
export default {
    
}
</script>

<style>

.transaction-form {
  margin: auto;
  margin-bottom: 40px;
  background-color: #fff;
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
  font-size: 18px;
  color: #7c7c7c;
}

.transaction-value {
  width: 30%;

  font-family: sans-serif;
  font-size: 18px;
  color: #7c7c7c;
}

.transaction-category {
  width: 20%;
  font-family: sans-serif;
  font-size: 18px;
  color: #7c7c7c;
  background: transparent;
  border: none;
}

</style>