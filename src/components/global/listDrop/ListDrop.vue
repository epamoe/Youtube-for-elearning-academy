<template>
    <span class="trgsMenuAll">
        {{current.name}}<img @click="displaying" src="./img/arrow.svg"/>
        <span :style="{display: Display}" class="trgsDropDown">
            <span @click="select(all)" :style="{color:all.selected}">{{all.name}}<span></span></span>
            <span v-for="(cat,index) in categories" :key="index"
                :style="{color:cat.selected}"
                @click="select(cat)"
            >
            <span>{{cat.name}}</span>({{cat.numb}})</span>
        </span>
    </span>
</template>
<style src="./listDrop.css">
</style>
<script src = "./listDrop.js">
</script>
