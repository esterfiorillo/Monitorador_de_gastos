<template>
    <div class="transaction-bar">
    <div class = "transaction-form">
        <input class="transaction-form__input" type="text" name="transaction" placeholder="Digite aqui sua transação">

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
  height: 44px;
  border-radius: 2px;
}

.transaction-form__input {
  width: 100%;
  height: 100%;
  font-family: sans-serif;
  font-size: 18px;
  color: #7c7c7c;
}

</style>